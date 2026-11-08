# Competitive balance

**Question:** with equally skilled, equally engaged players, does the Captain (driver), the Co-Pilot or a Crew member have a built-in advantage in becoming Journey Spaceman?

**v1.1 update (hijacks, milestones, Seat Challenges):** Role fairness holds (Simulation Mode, 300 missions per row, Balanced): the Captain wins 23.7% / 28.3% / 30.7% with 4 players at 20 / 45 / 60 minutes (fair 25%), 20.3% / 25.7% / 19.7% with 5 (fair 20%) and 19.0% / 17.0% / 19.3% with 6 (fair 16.7%). The Captain sits a few points above fair in some longer missions (4 players, 60 minutes: +5.7 points), which is outside sampling noise and worth watching in real play. In Real Journey Mode the Co-Pilot seat changes hands about 1.5–1.9 times an hour (v1.0: about 2.3, mostly from random promotion dice). More of the changes are now earned: there are about 2.3–2.5 Seat Challenges an hour, and promotions dropped from four to two per 30-minute cycle. Spaceman's win rate is in `SPACEMAN.md` (35–47% in Real Journey Mode). Use `tools/balance-sim.js` for role fairness; the Real Journey numbers come from a simple driver that steps the engine at one real second per step and counts events.

**v1.0 update (Crew vs Spaceman):** Spaceman is now an opponent (`SPACEMAN.md`). Role fairness is measured on the best crew member (`Engine.topCrew`), because a mission can now end with no Journey Spaceman. Balanced pacing, 1,000 missions per row: the Captain wins 27.3% (4 players, 45 min; fair 25%), 23.6% (4p, 60 min), 19.7% (5p, 45 min; fair 20%) and 18.6% (6p, 45 min; fair 16.7%). **Known gap:** in 20-minute missions the Captain sits 2–4 points below fair (20.6% at 4p), because three-round Estimation Station and the Bluff put more hidden lock-ins in a short mission and the Captain always answers last. It evens out by 45 minutes; worth watching in real play. Spaceman retains control in 11–30% of missions depending on crew size and length.

**v0.9 update:** the catalogue is now the seven core games (`GAMES.md`). In 2,000-mission runs the Captain wins 23.6% (4 players, 20 min), 26.2% (4p, 45 min), 17.0% (6p, 20 min) and 16.9% (6p, 45 min) against fair shares of 25% and 16.7%. The first Co-Pilot wins 20–29% and players who never hold the seat 14–23%. A Captain's +1 per game won was tested and rejected: it pushed the Captain to 28.6% in short 4-player missions. In hidden-answer games the Captain answers out loud last. What Happens Next? pays the star the predictors' average, so the Captain (who never stars) isn't disadvantaged.

**v0.8 update:** Quickfire Trivia no longer rewards speed. Everyone locks in privately and every correct answer is +3, so the answer-time allowances are gone. Worst Singer and Services Prophet were removed. Lucky Roll can now promote a passenger to Co-Pilot on a 6. Re-check at 3,000 missions, 4 players, 45 min: Captain 24.2% (fair 25%), first Co-Pilot 28.6%, never held the seat 21.1%. Estimation Station now always pays 🥇 +5 and 🥈 +2. In 300 test missions every game awarded a winner, and no event or transmission ever interrupted a game.

**Answer (v0.7):** the Captain and a typical passenger are both within about 2 points of a fair share. The Co-Pilot seat is now a deliberate, slight advantage of 3–5 points for whoever holds it. Run-to-run noise is about ±1 point.

## v0.7: the dynamic Co-Pilot seat (2,500 missions per row)

Since v0.7 the Co-Pilot is assigned at random after launch and can change hands (`COPILOT.md`). So passengers are split by their history with the seat, and `p0` is always the Captain.

| Players | Mission | Captain | Each passenger | Fair share | First Co-Pilot | Final Co-Pilot | Never held the seat | Seat changes |
|---|---|---|---|---|---|---|---|---|
| 4 | 20 min | 25.3% | 24.9% | 25.0% | 27.4% | 27.4% | 23.4% | 0.19 |
| 4 | 45 min | 25.6% | 24.8% | 25.0% | 30.0% | 29.6% | 21.1% | 0.48 |
| 4 | 60 min | 25.4% | 24.9% | 25.0% | 28.3% | 27.2% | 21.9% | 0.81 |
| 5 | 20 min | 21.8% | 19.5% | 20.0% | 22.8% | 23.8% | 18.1% | 0.18 |
| 5 | 45 min | 20.8% | 19.8% | 20.0% | 24.1% | 25.0% | 17.5% | 0.48 |
| 5 | 60 min | 22.8% | 19.3% | 20.0% | 22.5% | 24.0% | 17.0% | 0.81 |
| 6 | 20 min | 18.0% | 16.4% | 16.7% | 18.4% | 18.8% | 15.8% | 0.19 |
| 6 | 45 min | 18.7% | 16.3% | 16.7% | 20.3% | 22.8% | 14.6% | 0.50 |
| 6 | 60 min | 17.4% | 16.5% | 16.7% | 19.9% | 20.2% | 14.6% | 0.80 |

Same missions with no Co-Pilot perks (`noperks`, 1,500 per row; the Captain Shield stays on):

| Players, 45 min | Captain | First Co-Pilot | Never held the seat |
|---|---|---|---|
| 4 | 30.0% | 21.7% | 24.7% |
| 5 | 24.9% | 16.9% | 19.6% |
| 6 | 19.9% | 14.5% | 16.7% |

What this shows:
- **Without perks the seat is a burden.** About 3 points below fair, because tapping in the Captain's answers costs time. That's the "extra admin" problem.
- **With perks it's a slight edge.** About 3–5 points above fair. No multiplier, so it never decides the winner.
- **The Captain stays fair.** The Captain can never hold the seat, so the driver starts each mission with a Shield. Without it the Captain fell to about 19% in 4-player missions. With it, the Captain sits at fair in 4-player games and 1–3 points above in 5–6 player games.
- **Players who never hold the seat** win about 85% as often as a fair share. A great player can still win without it.
- **Perk values measured** in 4-player, 45-minute missions: +1 per *round* win about 5 points (so it now counts once per challenge win), free Shield about 5, third slot about 1, supply priority under 1.

Seat changes look low at prototype pace (a 45-minute demo mission lasts 7.5 real minutes, with about 3 promotion rolls). On a real drive, journey time runs in real time, so more promotions fit in.

```bash
node tools/balance-sim.js 2500 final
node tools/balance-sim.js 1500 noperks
node tools/balance-sim.js 1500 noshield   # Co-Pilot without the free Shield
node tools/balance-sim.js 1500 bonus2     # try +2 per win
```

## v0.6 baseline: fixed Co-Pilot, no perks

## Method

`tools/balance-sim.js` loads the real mission engine from `index.html` (the code between `ENGINE:START` and `ENGINE:END`) and plays full missions with an equally skilled bot in every seat:

- `p0` is always the Captain. In the v0.6 runs `p1` was a fixed Co-Pilot. Since v0.7 the engine assigns and moves the seat itself, as in a real mission.
- Trivia: every bot knows each answer with the same probability (65%) and takes 2.5–9 seconds to answer.
- The Captain says the answer out loud and the Co-Pilot taps it in, which adds 1–2.5 seconds. If the Co-Pilot is busy doing that, their own answer waits.
- Estimates are equally noisy for everyone, whether entered directly or by the Co-Pilot.
- Votes, Cosmic Answers picks and guesses, and Captain decisions are random.
- Spot Challenge winners are random across the whole car, Captain included.
- Power-ups are used a few minutes after they arrive. Point Thief always targets the leader.
- The simulation steps in 1.2-second slices of real time (0.02 journey minutes), at the prototype's pace of 10 real seconds per journey minute.

```bash
node tools/balance-sim.js 4000 final     # current rules
node tools/balance-sim.js 3000 noallow   # no answer-time allowance for the Captain or Co-Pilot
node tools/balance-sim.js 3000 allow1.5  # try a different Captain allowance (seconds)
node tools/balance-sim.js 3000 co0.5     # try a different Co-Pilot allowance (seconds)
```

### Results: v0.6 rules (4,000 missions per row)

| Players | Mission | Captain | Co-Pilot | Each Crew | Fair share | Avg points (Captain / Co-Pilot / Crew) |
|---|---|---|---|---|---|---|
| 4 | 20 min | 25.5% | 24.1% | 25.2% | 25.0% | 7.6 / 7.4 / 7.5 |
| 4 | 45 min | 26.1% | 24.0% | 24.9% | 25.0% | 17.1 / 16.6 / 16.8 |
| 4 | 60 min | 25.4% | 25.1% | 24.8% | 25.0% | 22.6 / 22.2 / 22.2 |
| 5 | 20 min | 20.6% | 19.0% | 20.1% | 20.0% | 6.6 / 6.4 / 6.5 |
| 5 | 45 min | 20.6% | 19.6% | 19.9% | 20.0% | 15.3 / 15.0 / 15.0 |
| 5 | 60 min | 18.9% | 20.2% | 20.3% | 20.0% | 19.9 / 19.8 / 19.9 |
| 6 | 20 min | 17.4% | 16.7% | 16.5% | 16.7% | 5.9 / 5.8 / 5.8 |
| 6 | 45 min | 17.3% | 16.1% | 16.7% | 16.7% | 13.9 / 13.5 / 13.6 |
| 6 | 60 min | 16.2% | 16.5% | 16.8% | 16.7% | 18.3 / 17.8 / 18.0 |

The leader changes hands about 2 times in a 20-minute mission and 5–8 times in 45–60 minute missions.

## Role bias found and removed

**Speed questions were the only source of role bias.** When the Captain answers out loud, the Co-Pilot still has to tap it in. Without any correction, that delay cost the Captain a noticeable share of wins:

| Rule set | 4 players, 45 min | 5 players, 45 min | 6 players, 45 min |
|---|---|---|---|
| No allowance: Captain | 20.9% (fair 25%) | 16.5% (fair 20%) | 12.6% (fair 16.7%) |
| No allowance: each Crew | 27.2% | 21.1% | 17.8% |
| **Current: Captain** | **26.1%** | **20.6%** | **17.3%** |
| **Current: each Crew** | **24.9%** | **19.9%** | **16.7%** |

**The fix: an answer-time allowance.**
- A Captain answer tapped in by the Co-Pilot counts as **2.25 seconds** earlier.
- The Co-Pilot's own answer counts as **0.75 seconds** earlier, but only when they had to tap the Captain's in first.

Values tested:

| Captain allowance | Co-Pilot allowance | Captain wins, 4p / 5p / 6p, 45 min |
|---|---|---|
| 0 s | 0 s | 20.9% / 16.5% / 12.6% |
| 1.5 s | 1.5 s | 22.4% / 18.9% / 14.4%. The Co-Pilot won slightly more than fair. |
| 1.75 s | 1.75 s | 22.9% / 17.6% / 15.2% |
| **2.25 s** | **0.75 s** | **26.1% / 20.6% / 17.3%** |

The allowance only matters in Quickfire Trivia. Every other challenge either has no speed element (Estimation Station, votes, Silent Mission) or is settled out loud (Spot Challenge).

## Why the other systems are already fair

1. **The Captain plays every challenge.** In v0.5 the Captain mirrored a random passenger's points (×1.1). That rule is gone. With a Co-Pilot tapping in their answers, the Captain now earns points the same way as everyone else.
2. **Cosmic Answers is symmetric.** The writer of the chosen answer gets +5, and a Captain who guesses the author correctly gets +5. With W writers, the Captain's chance of guessing right (1/W) equals any one writer's chance of being picked.
3. **The Co-Pilot gets no extra points.** The role is a responsibility, not a reward. Their only cost is time in speed questions, and the allowance covers that.
4. **The Spot Challenge has no buzzer.** The car agrees out loud who saw it first, so reaction speed and phone handling don't matter.
5. **Captain questions and decisions are for glory, not points.** Decision outcomes land on random crew members, Captain included.
6. **Events lean the right way.** Asteroids are weighted towards leaders and supply drops towards whoever is behind.

## Point values

| Source | Points |
|---|---|
| Quickfire Trivia | Fastest correct +4 · any other correct +1 |
| Estimation Station | Closest +5 · runner-up +2 · bang on (within 2%) +2 more |
| Spot Challenge | First to spot +3 |
| Cosmic Answers | Chosen writer +5 · Captain guesses author +5 |
| Votes | Pick with the majority +3 |
| Silent Mission | If someone cracks, everyone else +3. If nobody does, everyone rolls +2 to +4. |
| Asteroid Field | Direct hit −6 to −8 · Strike −3 to −5 · Near miss: no damage |
| Supply Drop / Solar Flare | +3 to +8 / +2 to +5 |
| Captain decisions | Minor +2 to +4 · Major +5 to +10 · Dents −3 to −6 |
| Lucky Roll / Point Thief | +2 to +6 / steals 2–5 |

**Deduction safety (unchanged).** The engine never shows "−0":

- A player at 0 sees "Would have lost 6 but was already at 0".
- A partial hit shows "−2, all they had (5 incoming)".
- Point Thief can't target anyone on zero.

## Pacing check

The same simulation checks the event queue. In 300 five-player, 45-minute missions at prototype pace:

- Two major events never ran at the same time.
- The shortest gap between events was exactly 10 real seconds.
- A typical mission had about 6–7 challenges (including 2 Spot Challenges), 4 transmissions, 2 cosmic events, 2 power-up drops and a Captain decision.

## Levers if real play feels off

| Symptom | Lever |
|---|---|
| Captains win speed questions too often or too rarely | `PT.proxyAllow` (Captain) and `PT.copilotAllow` (Co-Pilot) |
| Missions feel too busy | Raise `RULES.gap` above 10 seconds, or remove items from `CYCLE` |
| Not enough chat | Move `talk` or `chatter` earlier in `CYCLE`, or raise `RULES.stale` |
| Events feel too punishing | Narrow `PT.direct` and `PT.strike` |
| Leader runs away | Increase the asteroid leader weighting, or widen `PT.supply` |

## Limits

- Bots have equal skill. Real crews won't, and that's fine: the aim is no built-in role advantage, not equal outcomes.
- A real Co-Pilot's tapping speed will vary. Log real timings in testing and recalibrate the allowances.
- Points from Cosmic Answers depend on the Captain's taste. Anonymity helps, but it can't remove that.
