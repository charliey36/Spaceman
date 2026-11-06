# Game design roadmap (internal planning note)

## Long-term note (v0.9)

**From now on, development should focus on:**
- improving the existing games
- adding depth to the existing games
- making every game unmistakably *Spaceman*

**Avoid adding lots of extra mini-games.** The catalogue is now seven games (see `GAMES.md`): Crew Intel, Cosmic Answers, What Happens Next?, Estimation Station, Black Box, Risk It and Road Challenge. New ideas should first be tested as a *variation or layer* on one of these before they're considered as a new game.

Spaceman should be remembered because **"the games create stories"**, not because "there are lots of games".

Depth ideas for the existing games (not committed):
- **Crew Intel:** results feed friendship levels ("You know Megan 82%"). Questions unlock as friendships level up.
- **What Happens Next?:** the star's choices become recap story lines and a "most predictable" award.
- **Black Box:** the glitch can bluff with a second, harder pair.
- **Risk It:** a "Final Approach" double-stakes round near the destination.
- **Cosmic Answers:** the Captain's favourites are saved to Memories.

---


**Status:** the v0.8 planning below led to the v0.9 roster. Secret Assignment remains a candidate. It's parked, not committed, in line with the long-term note above.

## Why this note exists

Spaceman's game catalogue needs a dedicated design phase.

The mission systems, social systems, friendship systems and progression systems are getting strong: shared missions, the Co-Pilot seat, events, recaps, levels and memories. **The games themselves don't yet feel innovative enough.** Most are good versions of familiar formats: trivia, estimation, I-spy, a Quiplash-style writing game. They work, but they aren't yet the reason someone opens Spaceman instead of playing a car game they already know.

This should become its own initiative, not something added to each phase.

## Current catalogue (v0.8)

| Game | Keep? | Why |
|---|---|---|
| Cosmic Answers | ✅ Keep | Creativity and humour. The Captain plays by judging and guessing out loud. |
| Quickfire Trivia | ✅ Keep | Now hidden lock-in with a reveal, so there's no copying and no driver disadvantage. |
| Estimation Station | ✅ Keep | Best conversation starter in the set. Discussion first, then a clear podium. |
| Spot Challenge | ✅ Keep | Uses the road itself. Settled out loud, so it's very driver-friendly. |
| Silent Mission | ⚠️ Review | Short and funny, but it's a rule, not a game. Candidate to become a modifier. |
| Worst Singer, Services Prophet | ❌ Removed in v0.8 | Pure votes and popularity contests created little interaction. |
| Secret Assignment | ❓ Not in the build | Listed as a keeper in the Phase 7 brief, but no such game exists in the prototype. Strong candidate for the design phase (below). |
| Name That Intro | 🎵 Planned | Blocked by Spotify's developer policy. See `SPOTIFY.md`. |

## What the design phase should focus on

1. **Unique social gameplay.** Games that only work with *these* people in *this* car. They should use what the crew knows about each other, not general knowledge.
2. **Driver inclusion.** Every game is fully playable by voice. The Captain never needs the screen. The Co-Pilot role (entering the Captain's answers) is available, but a great game shouldn't depend on it.
3. **Conversation generation.** The best rounds spark talking that carries on after the round ends. Measure "seconds of talking after the reveal", not just taps.
4. **Competitive mechanics.** Comebacks, bluffing, risk and reward. No game decided purely by speed, popularity or luck.
5. **Mission integration.** Games that feed and are fed by mission systems: events, power-ups, the Co-Pilot seat, miles, destination, time of day.
6. **Original game design.** At least one signature game that is clearly Spaceman's own.

## Design principles (draft)

- **One phone per player, one shared story.** Private input, public reveal.
- **Voice first.** If a round can't be played with eyes on the road, it isn't a Spaceman game.
- **Under 3 minutes per round,** then at least 10 seconds of breathing room.
- **Reveal moments over timers.** Lock in, then reveal everything together.
- **Small, readable scoring.** Point values a player can predict, with clear 🥇/🥈 moments.
- **No pure votes or popularity contests.** Votes only as part of a bigger mechanic, such as bluffing.
- **Every game should end in a line worth remembering** in the recap.

## Candidate concepts (not committed)

| Concept | Core idea | Hits |
|---|---|---|
| **Secret Assignment** | Each player privately gets a mission, e.g. "Get someone to say 'roundabout'" or "Make the Captain laugh". Others try to spot who had which assignment at the end. | Social, bluffing, long-running, driver-friendly |
| **Crew Knowledge** | Questions about the crew ("What would Megan order at the services?"). The subject answers privately, everyone else predicts. | Social, conversation, uses friendships |
| **Route Bets** | Predict things about the road ahead: the next car colour, the miles to the next services, the ETA. Settled by the journey itself. | Mission integration, real-journey only |
| **Mission Log Debate** | Spaceman picks a funny moment from the mission log and the crew argues the verdict. The Captain rules. | Conversation, uses mission history |
| **Two Truths, One Asteroid** | Classic bluffing, with a cosmic-event twist when someone is caught. | Competition, humour |
| **Silent Mission as a modifier** | Instead of its own game, a "silent round" layered onto another game. | Simplifies the catalogue |

## Process for the design phase

1. **Brief.** Agree the principles above and success measures (talk time, laughs, replay requests, driver involvement).
2. **Paper test.** Play 6–8 concepts on real drives with cards and a phone timer. No code.
3. **Score each concept** against the six focus areas, from 1 to 5.
4. **Prototype the top 3** in the existing engine. Each game is one `kind` plus a UI card, so the engine needs no structural changes.
5. **Balance-check each one** with `tools/balance-sim.js`, so the Captain, Co-Pilot and Crew stay fair.
6. **Ship one signature game first,** then iterate.

## Engine hooks already in place

- `MISSIONS` entry with `kind`, weight `w` and `interrupt` for surprise games
- `startCh` and `finishCh`, and `chWinners` for the Co-Pilot bonus
- Captain intents via the Co-Pilot (`as:'captain'`)
- The event queue (games always take priority, 10-second cooldown)
- The mission log and recap, so a game can write the line that ends up in Memories
