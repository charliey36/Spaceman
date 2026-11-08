# Spaceman game catalogue (v1.1)

> Spaceman is not a trivia app or a quiz app. It's a social journey game.
> The best moments come from conversation, stories, knowing your friends and humour the players make themselves.

Every game must:
- include the driver and all passengers
- need minimal typing and screen time
- create discussion
- work in a moving car

## Roster

| # | Game | Type | Centrepiece | Typing |
|---|---|---|---|---|
| 1 | **Crew Intel** | Knowing your friends | ⭐ | None |
| 2 | **Cosmic Answers** | Creativity and humour | ⭐ | Optional (3 one-tap quick picks) |
| 3 | **What Happens Next?** | Story and prediction | ⭐ | None |
| 4 | **Estimation Station** | Discussion and a number | ⭐ | One number |
| 5 | **Black Box** | Bluffing and deduction | ⭐ | None (answers are spoken) |
| 6 | **Risk It** | Risk and comebacks | | None |
| 7 | **Road Challenge** | The road itself | Surprise interruption | None |
| 8 | **The Spaceman Bluff** | Crew vs Spaceman | Recurring | None |
| — | **Corrective Action** | Crew vs Spaceman, together | Special event | One shared number |
| — | **Rescue Mission** | Free a hostage from Spaceman | Only during a hijack | None |

v1.0 adds Spaceman as an opponent (see `SPACEMAN.md`). Every game can feed Spaceman when the crew gets it wrong. Games are never chosen by hand: the mission picks them.

Removed from rotation: Quickfire Trivia (general knowledge isn't social; its questions now power the rare Co-Pilot Challenge), Silent Mission, and the vote games removed in v0.8.

**Every game:**
- opens with a 4-second intro card, and Mission Control announces it if voice is on
- runs while every other event waits
- ends with a results card that writes a line to the mission log, so it appears in Memories

**The Captain rule.** In any game with hidden answers, the Captain answers out loud *last*, once everyone else has locked in, so speaking can't influence anyone. The Co-Pilot taps it in, and their panel only appears after they've locked in their own answer. The Captain can also tap directly if stopped.

---

## 1. Crew Intel ⭐

**Launch briefing.** When the mission starts, before the first game, every player (Captain, Co-Pilot and Crew) privately answers **3 one-tap questions** about themselves: dream holiday, favourite takeaway, ideal superpower and so on. There are 29 light, personal questions; nothing serious, political or sensitive. Each player gets different questions. The Captain answers before setting off. The briefing ends when everyone is done (40 s in Simulation Mode, 150 s in Real Journey Mode).

**Round.**
1. A player is selected. Whoever has been the subject least goes next, so everyone gets a turn, Captain included.
2. One of their stored answers becomes the question, e.g. "What's Connor's dream holiday? Japan / USA / Australia / Italy".
3. Everyone else locks in a guess. Guesses stay hidden until all are in, or 45 seconds pass.
4. Reveal: the right answer, with avatars on the option each person picked.

**v1.1 privacy fix:** the subject's own answer is never shown on any screen before the reveal, not even their own. Their phone just says it's about them and to keep a poker face, so nobody can glance at it, which matters most when the subject is the Captain with a mounted phone.

| Scoring | Points |
|---|---|
| Each correct guess | +5 |
| Selected player, per correct guess | +3 (3 right = +9) |

It rewards both knowing people and being known. **Next:** feed results into friendship levels ("You know Megan 82%").

## 2. Cosmic Answers ⭐

**v1.1:** 48 prompts, most about the people in the car, with real names filled in: "What would Captain Thomas get arrested for?", "The text Megan would send to the group chat by mistake", "Who in this car would sell the others out to Spaceman first, and for what?". The best answer should come from the players, not the prompt, so prompts set up a target and get out of the way. The quick picks are cheeky too, and use the same names. Safe by design: habits, decisions and silly hypotheticals, never looks, bodies or anything genuinely personal.

- Mission Control gives a prompt. Passengers write a secret answer, or tap one of 3 **quick picks** (no typing).
- The Captain (judge) hears the answers read out (by voice or the Co-Pilot), picks a favourite and guesses who wrote it.
- **Scoring:** chosen writer +5. Captain guesses the author: +5.

## 3. What Happens Next? ⭐

1. A scenario stars one passenger: "Connor finds a £20 note on the floor at the services." It comes with four endings.
2. **The star** privately taps what they'd really do. **Everyone else** (Captain included, by voice, last) predicts it.
3. Reveal: "What happened next: Connor found £20… and bought everyone snacks. 2 of 3 saw it coming."

| Scoring | Points |
|---|---|
| Each correct prediction | +4 |
| The star | The predictors' average, rounded (2 of 3 right → +3) |

**Driver-safe (v1.1):** the Captain's screen shows no endings at all, just "Eyes on the road. Just listen." When everyone else has locked in, Spaceman reads the scenario and the four endings out loud on the Co-Pilot's phone ("Captain. Lewis is offered a free sample… A. Takes one. B…. A, B, C or D?"). The Captain says a letter and the Co-Pilot taps it. Either of them can replay the reading. Letter-only buttons are there for when the car is parked. If the Captain doesn't answer, they simply don't score: there's no penalty and nothing goes to Spaceman.

Only passengers star, because the Captain's choice would have to be said aloud. The star's average-based score keeps it fair for the Captain. There are 16 scenarios, with no repeats within a mission.

## 4. Estimation Station ⭐ (3 rounds)

- **Three rounds** back to back. Each round is one question nobody really knows. The car talks it through, then everyone locks in a number (the Captain says theirs last).
- **Spaceman guesses too.** Its number appears on the podium like anyone else's, and it can win.
- **Scoring per round:** 🥇 closest +5 (ties share), 🥈 second closest +2, everyone else 0. If the crew's best guess is way off (more than 40%, or 15+ years), Spaceman also gets +4.
- After each round, an 8-second podium shows the answer, each guess, how far off it was and the points. The final card lists the winner of each round.

## 5. Black Box ⭐ (4+ players)

1. **Read** (15 s): each passenger privately sees a question. One random passenger, *the glitch*, gets a slightly different one ("Best thing to take on a road trip?" vs "Worst thing…"). The glitch doesn't know.
2. **Talk** (up to 60 s): go round the car; every passenger answers **out loud**. The Captain is the detective and just listens.
3. **Vote:** everyone, Captain included, taps who they think the glitch is.

| Scoring | Points |
|---|---|
| Each voter who finds the glitch | +3 |
| The glitch, if fewer than half find them | +3 (escapes) |

The reveal shows both questions. There are 18 question pairs.

## 6. Risk It

- Two rounds of "higher or lower?" against a number built from verified facts (the Estimation Station question bank). Example: "How many keys are on a piano? Higher or lower than 64?"
- Argue it out, then pick a stake and an answer:

| Stake | Right | Wrong |
|---|---|---|
| Safe | +1 | 0 |
| Bold | +3 | −2 |
| All in | +6 | −5 |

- Losses never go below zero. The usual "would have lost X" text applies.
- Results show the biggest win and the biggest ouch.

## 7. Road Challenge (replaces Spot Challenge; Road Prophecy dropped)

- A surprise interruption, at most once every 30 journey minutes: "🚗 First to spot: a yellow car / Tesla / horse / police car…" (20 targets).
- Shout it out. The car agrees who was first, and anyone taps the winner: **+3**.
- If nobody sees one, "Not seeing one? New target" appears after a minute. It closes quietly after 6 minutes.
- No countdowns, no tracking, no location logic. **Decision:** a single, lightweight Road Challenge. A prediction system ("Road Prophecy") would have needed countdowns and tracking, against the journey-first goal.

## 8. The Spaceman Bluff

- Two rounds. Spaceman states a strange fact ("Goldfish only have a three-second memory."). Everyone locks in **TRUE** or **FALSE**, hidden until everyone's in. The Captain says theirs last.
- Reveal: the answer, a one-line explanation, and each player's result.
- **Scoring:** right +5. Wrong −5, and the lost credits go to Spaceman.
- 24 facts, no repeats within a mission.

## Rescue Mission (v1.1, only during a hijack)

- Spaceman is holding a crewmate (see `SPACEMAN.md`). Three true-or-false rounds from the Bluff fact bank.
- Everyone except the captive answers; the captive can shout answers out loud.
- **More than half of all answers right:** the captive is free, Spaceman loses 6, and everyone who got one right gets +2. **Otherwise:** Spaceman +5, and another chance comes in 3–5 minutes.
- No credits are lost for wrong answers. It's a team effort.

## Corrective Action (special event)

- Arrives like Road Challenge, at most once per 30-minute cycle: "Crew vs Spaceman".
- One question with a number answer. The whole crew talks it through and **anyone submits one shared answer** (60 s).
- **Within 25%** (or 5 years): Spaceman loses 8. **Miss:** Spaceman gains 6.

---

## Fairness (equally skilled simulated players, 2,000 missions per row)

| Mission | Captain | Fair share |
|---|---|---|
| 4 players, 20 min | 23.6% | 25% |
| 4 players, 45 min | 26.2% | 25% |
| 6 players, 20 min | 17.0% | 16.7% |
| 6 players, 45 min | 16.9% | 16.7% |

The Co-Pilot keeps a slight edge (+2 to +5 points), as designed. Full tables are in `BALANCE.md`.
