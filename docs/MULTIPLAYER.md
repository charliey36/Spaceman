# Multi-device architecture

**Core rule:** every player takes part from their own phone. The mission is shared, but every interaction is individual. No game should ever need a phone passed around.

## What the prototype does today

The prototype is a single web page with no server. It already uses the architecture a real build needs:

| Piece | Where | What it does |
|---|---|---|
| Mission engine | `index.html`, between `ENGINE:START` and `ENGINE:END` | Pure logic with no DOM. Owns the shared mission state, the clock, the rhythm, scoring and events. |
| Intents | `Engine.act(state, {type, by, ...})` | The only way a phone changes anything. Examples: `answer`, `vote`, `buzz`, `use`, `decide`, `tx-send`. |
| Host clock | `Engine.step(state, minutes)` | Runs on the host: timers, power-up drops, cosmic events, transmissions, timeouts. |
| Transport | `Transport.send(intent)` | Today it calls the engine in the same tab. **FUTURE:** posts the intent to the host over the network. |
| Simulated phones | Bots inside the engine | Play for every crew member who isn't on this phone. They act on their own timers, like real people. |
| Phone switcher | "Your phone" chip on the live screen | Shows the mission from any player's seat and lets you act as them. This is how to test every role in one tab. |

There is no separate driver screen any more. Every phone renders the same live view from the same state, and only the parts that belong to that seat change:

- your own answer box
- your own vote
- your own power-ups
- Captain-only judging and decisions
- the Co-Pilot's "for Captain" panel

### Roles (v0.6)

| Role | Who | What their phone does |
|---|---|---|
| Captain | The driver | Hosts the mission. Shows big buttons for anything Captain-only, but never needs touching while driving. |
| Co-Pilot | A passenger picked at random after launch. Can change hands through Mission Promotion or a Co-Pilot Challenge (see `COPILOT.md`) | Plays as themselves with small perks, *and* taps in what the Captain says out loud: trivia letters, estimates, votes, decisions, Cosmic Answers picks and guesses, "Captain has answered", and the Captain's power-ups. |
| Crew | Everyone else | Plays as themselves. |

The Captain's input is sent as an ordinary intent with `as:'captain'`. The engine accepts it only from the Captain or the current Co-Pilot (`Engine.act`). Both controls stay live, so a stopped Captain can still tap directly.

In the prototype, a simulated Captain "says" its choice. That appears on the Co-Pilot's phone as *Captain said: "B. Fly through"* and gets tapped in, either by a simulated Co-Pilot after 1–2.5 s or by you.

### Pacing profiles (v1.0)

Chosen on the Go page; stored as the mission `mode` and applied through `TEMPO` in the engine. Nobody picks games any more: the engine picks the next game itself (`nextChallengeId`), so there is no line-up and no "up next" vote.

| Pacing (`mode`) | Gap after anything (real s) | Rest between games, journey min (Simulation / Real) | Events between games | Event cycle |
|---|---|---|---|---|
| Relaxed (`chill`) | 20 | 1.5 / 4 | 1 | ×1.5 |
| **Balanced** (`party`, default) | 12 | 0.6 / 1.5 | 1 | ×1 |
| Chaotic (`competitive`) | 10 | 0 / 0.5 | 2 | ×0.75 |

Spaceman roasts join the voice queue (`roast`) and are rate-limited by `RULES.roastGap × cycle`. Why Balanced is the default: `SPACEMAN.md`.

### Pacing (v0.8)

- **Games always take priority.** While any game is running (Silent Mission included), no transmission, cosmic event, decision, power-up drop or role moment can start. They wait in the queue.
- After each game ends, nothing new starts for at least 10 real seconds.
- On-screen times for events, transmissions and decisions are in real seconds, so they feel the same in both modes.
- **Simulation Mode:** AI passengers, 10 seconds = 1 mission minute.
- **Real Journey Mode:** 1 minute = 1 minute, no AI passengers. Players pass the phone, or in the future use their own. Miles come from GPS when allowed, with at least 1.5 minutes between games.
- Toasts show one at a time, and only on the phones they concern.

### Pacing (v0.6)

All major events go through one queue in the engine: challenges, spot challenges, cosmic events, Captain decisions, transmissions and power-up drops.

- Only one runs at a time.
- At least **10 real seconds** separate the end of one from the start of the next. This is measured in real time (`S.rt`), not journey time.
- Between two challenges there is at most one event and one voice moment (two events if they're piling up). Waiting items gain priority over time, and stale chat prompts are dropped.
- During a Silent Mission only passive events (cosmic events, power-up drops) can play. Discussion prompts, Captain questions and transmissions wait.

## Production design

### Authority

- **The Captain's phone is the mission host as far as players are concerned.** It starts the mission, its GPS measures distance, and it holds the Captain controls.
- **The room's state should be authoritative in the cloud.** A phone in a moving car loses signal in tunnels and sleeps when it overheats. If the driver's phone were the only source of truth, everyone else would freeze whenever it dropped.
- **Recommended setup:** a realtime room per mission (for example Cloudflare Durable Objects, PartyKit or Supabase Realtime) running the same `Engine` code. The Captain's phone also runs a local copy, so the mission keeps going offline and catches up when it reconnects.

### Messages

```text
phone → room   { kind:'intent', missionId, seat, seq, type, ...payload, sentAt }
room → phone   { kind:'state', missionId, version, view }       // a full view for that seat
room → phone   { kind:'patch', missionId, version, ops:[...] }  // small diffs between full views
room → phone   { kind:'signal', type:'tx'|'drop'|'toast'|'haptic', ... }
```

- Each intent carries the sender's seat. The room rejects anything the seat isn't allowed to do, using the same checks `Engine.act` already makes. For example, only the Captain can `pick`, `guess` or `decide`, and the Captain can't `answer` or `buzz`.
- Each player gets a **redacted view**:
  - Answers stay hidden until the Captain is picking, and authors stay hidden until the reveal.
  - Other players' power-ups show as a count, not by type.
  - Queued transmissions only appear to the sender.

### Joining

1. The Captain taps **Start mission**, and a room is created with a 4-letter code and a QR code.
2. Passengers scan the code or tap a notification from a crew mate who is already in the room.
3. Each phone claims a seat tied to its account. Guests join through a web link with no install (App Clip or Instant App) and pick a name. That becomes the existing guest and claim-miles flow.
4. Miles together only count for phones that report being in the same car. Compare coarse GPS against the host every few minutes.

### Speed fairness (Quickfire Trivia)

- Phones send `sentAt` timestamps corrected by a clock offset measured when they join (an NTP-style ping exchange). The room ranks answers by corrected time, so whoever has the fastest signal doesn't automatically win.
- A Captain answer tapped in by the Co-Pilot gets a 2.25-second allowance. The Co-Pilot's own answer gets 0.75 seconds when they had to type the Captain's first. Both values are calibrated in `BALANCE.md`.
- The Spot Challenge has no buzzer at all. The car agrees out loud who saw it first, and anyone taps the winner.

### Reconnection

- Phones keep the last `version`. On reconnect they ask for patches since then, or a full view.
- Intents that fail to send are queued and retried with the same `seq`, so nothing is applied twice.
- If the Captain's phone goes offline, the mission keeps running in the room. The Captain controls show "Captain offline" and decisions auto-resolve after their timeout, as the prototype already does.

### Safety

- The Captain never has to touch the phone. They answer out loud and the Co-Pilot taps it in.
- When the Captain's phone detects driving speed, its controls could lock and show only "Say it out loud. Your Co-Pilot taps it in." This is a future option. Today both paths stay open, as the brief asks.

## Next steps

1. Move the engine into its own module shared by the client and the room.
2. Build the room with full views per seat, then add patches.
3. Add the join flow (code, QR, seat claim) and the phone list with real connection status.
4. Add clock-offset sync and fair buzz settlement.
5. Add offline mode on the Captain's phone, then reconcile when it reconnects.
