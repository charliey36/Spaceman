# Crew vs Spaceman (v1.3)

Every mission now has one more player: **Spaceman** (the astronaut with the gold visor and one red eye), the mission's own AI. Players compete with each other *and* against Spaceman.

| Who | What they are |
|---|---|
| Captain | Driving. Plays everything out loud. |
| Co-Pilot | Taps things in for the Captain. Small perks. |
| Crew | Everyone else. |
| **Spaceman** | The opponent. Has credits, sits on the leaderboard, can win or lose. |

## v1.3 changes (Phase 11)

**Winning is the crew total against Spaceman.** v1.2 still compared the *best single player* with Spaceman, so a crew could finish 284 to 248 and be told "Spaceman Retains Control". Now:

| At the end | Result |
|---|---|
| Crew total > Spaceman's total | 🏆 **The crew has taken control.** The highest-scoring free player is crowned **Journey Spaceman** (ties broken at random). |
| Otherwise | **Spaceman Retains Control.** The recap still names the crew's best player. |

`Engine.crewWins(S)` decides the result; `Engine.winner(S)` returns the Journey Spaceman, or `null` when Spaceman wins.

**Hostages move credits.** A captured player's credits leave the crew total and count for Spaceman while they're held (crew 100, Megan 40, Spaceman 50 → crew 60, Spaceman 90). The hijack card says so in one line ("Crew −40 · Megan's credits → Spaceman +40"), the VS banner shows the new totals, and Spaceman's chip shows "+40 held". When the captive is freed their credits come back.

**Rescue fund.** Anyone except the captive can give 2, 5 or 10 credits towards a rescue target (30, rising 10 with every ransom, to 70). The card shows `15 / 30`, then `30 / 30 ✅` and the captive walks free. The biggest donor gets +2 and everyone who chipped in finds a power-up.

**Spaceman reacts.** Capturing someone triggers one of 20 spoken lines ("Megan has joined my side. Frankly, she seems more competent than the rest of you."), then Commander Atlas replies. Roasts grew from 98 to 180 lines, with new pools for capture, the Co-Pilot, the whole crew and Spaceman Fury, and sharper last-place, leaderboard and failure lines. Discussion prompts grew from 54 to 94: debates, hypotheticals, ridiculous situations and social questions built to start stories.

**Spaceman is one against the whole crew**, so everything it earns is multiplied by crew size (×1.7 with 3 players up to ×2.2 with 5 or 6; ×0.85 of that in Simulation Mode). **Spaceman Fury**: while the crew total is more than 1.2× Spaceman's (+10), its gains count ×2.2 on top. The banner turns red ("Fury ×2.2") and Spaceman says so. This is the board-game catch-up rule pointed at the opponent: it stays threatening all mission and wins about one mission in five.

**Milestones** now draw from 22 outcomes (up from 8), never the same one twice in a row: credits (jackpot, lottery, tailwind), losses (fuel leak, Spaceman barrage, road tax), power-ups (supply run, supply pod, pickpocket), power-up theft (locker raid), Shields for everyone, Afterburners (double next win for the bottom half), Overdrive, Spaceman claiming the marker, a bonus event, a Seat Challenge, a Mission Promotion, a rescue mission, a rescue discount, a bounty or a hijack.

**More power-ups.** A game's outright winner finds one 30% of the time, a duel winner always does, rescuers do, and refusing Spaceman's bribe now earns a Shield.

**The Spaceman Bluff** has 52 facts, 26 true and 26 false. The new true ones sound made up and the new false ones sound right, and each mission deals true and false evenly, never three of the same in a row.

## v1.2 additions

- **Commander Atlas** now voices Mission Control, so Spaceman has a rival in the car's ear. Atlas is on the crew's side; Spaceman calls him "adorable". Spaceman's own chatter moved to a *banter* roast pool. See `ATLAS.md`.
- **Party mechanics** (see `PARTY.md`): Chance Time can swap credits *with Spaceman*; duels that nobody wins pay Spaceman; the **bribe** pays Spaceman 8 when accepted; surges and Final Approach's double credits double Spaceman's gains too.
- **Spaceman's Bonus** at the end: +8 for every hostage it took and every bribe accepted, revealed alongside the crew's Bonus Awards.

## Spaceman's character (v1.1)

Spaceman is the mission's AI: it used to run Mission Control and now wants to win. It's the host, the rival, the commentator and the troublemaker in one.

| Trait | How it shows |
|---|---|
| **Smug, dry, British** | "Noted. Logged. Filed under disappointing." Spoken in a slower, lower *smug* voice. |
| **A sore loser** | When the crew does well: "You're learning. I hate it." |
| **Theatrical about money** | "Thank you for your generous donation." "Ka-ching." |
| **Secretly fond of the crew** | "For the record, Captain Thomas is a perfectly adequate Captain. That's the nicest thing I've said all day." |
| **Never cruel** | Teases decisions, scores and habits. Never looks, bodies, intelligence or anything personal. |
| **Has a look** | A black tactical suit, a gold mirrored visor and one red scanning eye. |
| **Has a catchphrase** | Every transmission ends, after a beat, with "Over." |

**Where it speaks:**
- **A verdict after every game:** one line on the results card (and spoken), chosen from what happened: a big haul, a clean game for the crew, a new leader, an exact estimate, a star performance, a disaster, a rescue. That's 11 situations and 50+ lines.
- **Roasts** (rate-limited transmissions), now context-aware: they can quote the target's credits, the gap to the leader, the miles driven and the minutes played. 9 → 12 triggers, 63 → 90+ lines.
- **Mission Control chatter** in Spaceman's voice: leaderboard comments, mission updates, threats about the next milestone.
- **The recap:** a parting line, smug if Spaceman won, sore if it lost.

## The Spaceman Hijack (v1.1)

**Problem:** in v1.0 Spaceman scored quietly and won 11–30% of missions. It never felt threatening.

**Design:** Spaceman takes a hostage. It aims for the **leader** (like Mario Kart's blue shell), so the hijack is also a comeback mechanic.

| While captured | Effect |
|---|---|
| **Skim** | The captive keeps playing, but Spaceman keeps **half of everything they win**. |
| **Ransom ticks** | Every 5 journey minutes (scaled by pacing), Spaceman takes 2, then 4, 6 and 8 credits from the captive. From the third tick, everyone else pays 2 as well: the whole ship suffers. |
| **Release** | After the fourth tick, Spaceman gets bored and lets them go, keeping a quarter of their credits. |
| **Shields** | Don't help. "Shields can't stop a tractor beam." |

**Ways out:**

| Way out | How | Reward |
|---|---|---|
| **🛟 Rescue Mission** (2–4 minutes after the capture, then every 3–5 minutes) | Spaceman asks three true-or-false questions. Everyone except the captive answers. The crew needs **more than half** of all answers right. The captive can shout answers; Spaceman can't stop them talking. | The captive goes free, Spaceman loses 6 (12 if it came from a milestone), and everyone who got one right gets +2. A failed rescue pays Spaceman 5. |
| **Pay to escape** | The captive pays 6 + 3 per ransom so far, or a quarter of their credits if that's more. It all goes to Spaceman. | Free immediately. A real risk/reward call. |
| **Swap** | Any other player can take the captive's place, once per hijack. | +3 for bravery, and they inherit the ransom clock. |

**What triggers a hijack:** a milestone (more likely when the leader is ahead of Spaceman), a surprise tractor-beam cosmic event, a crew losing streak (three games in a row feeding Spaceman), and some risky Captain decisions (distress signal, escape pod, tractor beam warning). Only one hostage at a time. Milestone, cosmic and losing-streak hijacks wait until minute 9.

**On screen:** the VS banner turns red ("🚨 Megan's captured"), the captive's leaderboard chip gets a red dashed ring and "Captured", and tapping either opens the hostage sheet: how long, how much has been skimmed, when the next ransom lands, and the escape options.

## Milestones (v1.1)

Every **10 miles** (GPS miles in Real Journey Mode), something big happens. One of:

| Milestone | Effect |
|---|---|
| **Milestone Jackpot** | Everyone gets 2–4. Whoever is last gets 5–8. |
| **Overdrive** | The next game pays double credits. |
| **Supply Run** | A power-up for everyone with a free slot. |
| **Road Tax** | Everyone with 8+ credits pays Spaceman 3. |
| **Bounty on the Leader** | Beat the leader in the next game and take 4 of their credits. If nobody does, the leader gets +3. |
| **Bank It or Bet It** | A Captain decision: everyone +2 now, or a coin flip between everyone +6 and Spaceman +12. |
| **Hijack** | Spaceman captures the leader. |
| **Rescue** | If someone is already captured, a rescue starts at once, worth double. |

## Surprise events (v1.1)

New cosmic events join asteroids, supply drops, solar flares, black holes and hijacked crates:

| Event | Effect |
|---|---|
| **Bounty Posted** | A price on the leader for the next game. |
| **Power Surge** | Every credit in the next game is doubled. |
| **Underdog Signal** | Last place gets +4 and a Shield. |
| **Spaceman Audit** | The leader pays Spaceman 15% (at least 3). |
| **Spaceman Malfunction** | Spaceman loses a third of its credits, and they spill to the two lowest-placed players. |
| **Tractor beam** | A surprise hijack (shown as the hijack card). |

Captain decisions now number 28, most with a gamble (a chance of a big win or a backfire), and five of them come back later in the trip as **story callbacks** ("The aliens you rescued are back with gifts").

## Pacing in v1.1

Balanced now allows two events between games (Chaotic three). In Real Journey Mode, a simulated hour with 4 players has about 17 games, 6 Captain decisions, 6 cosmic events, 3 milestones, 1.3 hostage situations and 2.5 Seat Challenges. Surprises that wait too long in the queue are dropped, so nothing stale ever fires.

## Balance (v1.1, historical; v1.3 numbers are in `BALANCE.md`)

Spaceman then retained control in **35–47%** of missions (Real Journey Mode, 60 minutes, 150 simulated missions per row): 3 players 38%, 4 players 35%, 5 players 39%, 6 players 47%. It's a real opponent that the crew beats more often than not. To stop bigger crews simply handing Spaceman more wrong guesses, the per-wrong-guess payment now scales with crew size (full value up to 4 players, ×4/n above that).

In Simulation Mode (time compressed, so fewer games fit between events) the rate is 24–59%, rising with crew size and mission length; treat those numbers as a stress test, not the real experience.

## Winning

At the end of the mission:

- **The crew total beats Spaceman's total** → *"The crew has taken control of the mission."* The best free player becomes 🏆 **Journey Spaceman**.
- **Otherwise** → **Spaceman Retains Control**. *"The crew failed to seize command."* Nobody is crowned. The recap still names the best crew member.

(v1.3. Before that, the best single player had to beat Spaceman, which produced wrong results. See "v1.3 changes" above.) `Engine.crewWins(S)` decides it, `Engine.winner(S)` returns the Journey Spaceman, `Engine.topCrew(S)` always returns the best crew member.

## Always on screen

- **The VS banner** sits under the mission header for the whole mission: **Crew total** vs **Spaceman**, with one line underneath: "Megan leads Spaceman by 5", "Spaceman leads you by 3" or "level". Tap it to see Spaceman's log.
- **The leaderboard** includes Spaceman as a chip, slotted in by score.
- **Every game's results card** shows "Spaceman +N this game" when Spaceman scored during it.
- **Asteroid rows** show the part Spaceman kept ("Spaceman +3").

## How Spaceman earns (never at random)

Spaceman only scores from something the crew can see happen. Every gain is logged with a reason (`S.smLog`), shown in the Spaceman sheet and the mission log.

| Trigger | Spaceman gains | Notes |
|---|---|---|
| Crew Intel: nobody knew the answer | +5, plus +2 per wrong guess | Triggers a roast ("Perhaps introductions are in order.") |
| Crew Intel / What Happens Next?: some guesses wrong | +2 per wrong guess | |
| What Happens Next?: nobody saw it coming | +3, plus +2 per wrong guess | |
| Estimation Station: crew's best guess was way off | +4 per round | More than 40% off, or 15+ years off for a year question |
| Estimation Station: Spaceman's own guess | 🥇 +5 / 🥈 +2 | Spaceman locks in a number every round, like a player |
| Black Box: the glitch escapes | +4 | Plus +2 per wrong vote |
| Cosmic Answers: low participation | +2 per missing answer | |
| Risk It: failed gambles | 75% of the credits lost | |
| Asteroids and dents | 75% of the credits lost | "Spaceman has targeted Lewis." |
| The Spaceman Bluff: wrong answer | Everything the player loses (5) | |
| Road Challenge: nobody spots it | +3 | |
| Corrective Action fails | +6 | |

## Fighting back

| How | Effect |
|---|---|
| 📦 **Hijacked Supply Crate** (cosmic event, only once Spaceman has 4+ credits) | One or two players (lower scorers are likelier) take 3–6 credits each from Spaceman |
| 🛡️ **Corrective Action** (special event, once per 30-minute cycle) | The whole crew agrees on one number (within 25%, or 5 years). Success: Spaceman −8. Failure: Spaceman +6. |
| 🦹 **Credit Thief** (power-up) | Can now target Spaceman as well as players. Bots target Spaceman when it's ahead of the leader. |
| Simply scoring | Every credit a player earns closes the gap. |

## The Spaceman Bluff

A recurring game (weight 2.2, about as common as Estimation Station). Two rounds.

1. Spaceman states a strange fact: *"There are more aeroplanes underwater than submarines in the sky."*
2. Everyone locks in **TRUE** or **FALSE**, hidden until everyone's in (30 s). The Captain says theirs last; the Co-Pilot taps it in.
3. Reveal: the answer, a one-line explanation, and every player's result.

| Answer | Credits |
|---|---|
| Right | +5 |
| Wrong | −5, transferred to Spaceman (never below zero; a Shield blocks it) |

A flat −5 was chosen over −10% of current credits: it's predictable, it hurts the leader and the last player equally, and it can be said out loud. There are 24 facts, with no repeats within a mission.

## Estimation Station: now three rounds

Estimation Station now plays **3 rounds** back to back (about 7 minutes in total), with an 8-second podium reveal after each. Spaceman guesses each round too, and the final card lists the winner of every round ("Lewis won 2 of 3 rounds. Spaceman won 1.").

## Roast transmissions

Spaceman talks. Lines arrive as transmissions marked **From: Spaceman** and are read aloud if voice is on.

| Trigger | Example |
|---|---|
| Nobody knew a Crew Intel answer | "Reminder: friendships are supposed to involve knowing things about each other." |
| Someone loses 5+ credits at once | "Connor has now lost more credits than a cryptocurrency investor." |
| Someone is 10+ behind the leader | "Lewis is currently treating the leaderboard like a sightseeing destination." |
| The crew has a bad streak (3 rounds feeding Spaceman) | "I have reviewed the data and can confirm this crew shares exactly one collective brain cell." |
| Spaceman is ahead of the leader | "Mission status update: I am carrying this entire operation." |
| The leader is 8+ ahead of Spaceman | "Fine. Megan is doing well. I've made a note of it. A permanent note." |
| A hijacked crate, Corrective Action | "Teamwork. Disgusting. Well done." |

**Never annoying:**
- At most one roast every 6 journey minutes (9 in Relaxed, 4.5 in Chaotic), and never two in the queue.
- No line repeats within a mission (63 roast lines across 9 triggers, plus Spaceman lines in Mission Control chatter).
- Roasts tease decisions and scores, never a person's looks, voice, intelligence or anything personal. Every line is written to be laughed at by the person it's about.

Simulated missions get between 0.2 and 1.4 roasts each.

## Games are never chosen by hand

The game picker is gone, both before the mission (the line-up) and during it (the "Up next" choice). The mission picks the next game; between games the screen says *"Spaceman is choosing what happens next."* The Go page explains Crew vs Spaceman and lists every game in the rotation instead.

## Pacing

Set on the Go page when creating a mission.

| Pacing | Rest between games (Real Journey) | Events between games | Event cycle | For |
|---|---|---|---|---|
| Relaxed | 4 min | 1 | ×1.5 slower | Long drives, tired crews, more conversation |
| **Balanced** (default) | 1.5 min | 2 (v1.0: 1) | ×1 | Most journeys |
| Chaotic | 0.5 min | 3 (v1.0: 2) | ×0.75 faster | Short, loud journeys |

Simulation Mode uses shorter rests (1.5 / 0.6 / 0 journey minutes) so a demo moves quickly. Every pacing also waits 10–20 real seconds after anything ends before the next thing starts.

### Why Balanced is the default

- **Driver attention.** The Captain plays everything by voice, but every game still asks for a decision. Chaotic stacks those decisions back to back, which is the wrong default for someone driving. Balanced leaves a breather after every game.
- **Group conversation.** The best moments in playtesting come *after* a reveal. Balanced keeps a minute or so of nothing between games so those conversations can happen; Chaotic cuts them off.
- **Mission immersion.** Relaxed can go 4+ minutes with nothing on screen, long enough for the phone to be forgotten. Balanced keeps Spaceman present without being constant.
- **Event fatigue.** Balanced allows one event between games and one Spaceman roast every 6 minutes at most. That's enough for Spaceman to feel alive and not enough to feel like notifications.

Relaxed and Chaotic are one tap away for crews who know what they want. Existing users are moved to Balanced once with this update.

## Balance in v1.0 (historical; see "Balance (v1.1)" above for current numbers)

*How often Spaceman retains control* (no crew member finishes above it). Balanced: 1,000 missions per row; Relaxed and Chaotic: 600.

| Crew | Mission | Relaxed | **Balanced** | Chaotic |
|---|---|---|---|---|
| 4 players | 20 min | 15.7% | **11.3%** | 4.3% |
| 4 players | 45 min | 16.2% | **18.3%** | 14.2% |
| 4 players | 60 min | 19.2% | **21.7%** | 12.8% |
| 5 players | 45 min | 19.2% | **24.6%** | 17.3% |
| 6 players | 45 min | 21.8% | **28.8%** | 20.2% |
| 6 players | 60 min | 33.8% | **30.3%** | 20.5% |

The crew usually takes control, but Spaceman wins roughly one mission in four or five. It wins more often with bigger crews (more people to get things wrong) and on longer journeys, and less often in Chaotic, where more games mean more chances for one player to pull clear. Role fairness for the Captain and Co-Pilot is covered in `BALANCE.md`.

Run it yourself: `node tools/balance-sim.js 300 final index.html party` (the last argument is the pacing: `chill`, `party` or `competitive`).

## Tuning knobs

All in `PT` and `RULES` in `index.html`:

- `smWrong` (2): what each wrong guess feeds Spaceman. The main dial for Spaceman's win rate (1 → ~12%, 2 → ~20%, 3 → ~32% at 45 minutes).
- `smShare` (.75): the share of Risk It, asteroid and dent losses Spaceman keeps.
- `bluffWrong` (5), `fixWin` / `fixLose` (8 / 6), `hijack` ([3, 6]).
- `RULES.roastGap` (6): journey minutes between roasts, scaled by pacing.
