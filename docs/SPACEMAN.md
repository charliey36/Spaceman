# Crew vs Spaceman (v1.0)

Every mission now has one more player: **👨‍🚀 Spaceman**, the mission's own AI. Players compete with each other *and* against Spaceman.

| Who | What they are |
|---|---|
| Captain | Driving. Plays everything out loud. |
| Co-Pilot | Taps things in for the Captain. Small perks. |
| Crew | Everyone else. |
| **Spaceman** | The opponent. Has credits, sits on the leaderboard, can win or lose. |

## Winning

At the end of the mission:

- **A player finishes above everyone else AND above Spaceman** → 🏆 **Journey Spaceman**. The recap says *"The crew has taken control of the mission."*
- **Otherwise** → 👨‍🚀 **Spaceman Retains Control**. *"The crew failed to seize command."* Nobody is crowned. The recap still names the best crew member and how far behind Spaceman they finished.

`Engine.winner(S)` returns the winner only if they beat `S.sm`. `Engine.topCrew(S)` always returns the best crew member (used for the recap and balance tools).

## Always on screen

- **The VS banner** sits under the mission header for the whole mission: **Crew total** vs **Spaceman**, with one line underneath: "Megan leads Spaceman by 5", "Spaceman leads you by 3" or "level". Tap it to see Spaceman's log.
- **The leaderboard** includes Spaceman as a chip, slotted in by score.
- **Every game's results card** shows "👨‍🚀 Spaceman +N this game" when Spaceman scored during it.
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
| **Balanced** (default) | 1.5 min | 1 | ×1 | Most journeys |
| Chaotic | 0.5 min | 2 | ×0.75 faster | Short, loud journeys |

Simulation Mode uses shorter rests (1.5 / 0.6 / 0 journey minutes) so a demo moves quickly. Every pacing also waits 10–20 real seconds after anything ends before the next thing starts.

### Why Balanced is the default

- **Driver attention.** The Captain plays everything by voice, but every game still asks for a decision. Chaotic stacks those decisions back to back, which is the wrong default for someone driving. Balanced leaves a breather after every game.
- **Group conversation.** The best moments in playtesting come *after* a reveal. Balanced keeps a minute or so of nothing between games so those conversations can happen; Chaotic cuts them off.
- **Mission immersion.** Relaxed can go 4+ minutes with nothing on screen, long enough for the phone to be forgotten. Balanced keeps Spaceman present without being constant.
- **Event fatigue.** Balanced allows one event between games and one Spaceman roast every 6 minutes at most. That's enough for Spaceman to feel alive and not enough to feel like notifications.

Relaxed and Chaotic are one tap away for crews who know what they want. Existing users are moved to Balanced once with this update.

## Balance (simulated missions with equally skilled bots)

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
