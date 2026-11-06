# The Co-Pilot seat (v0.7)

**Design goal:** being Co-Pilot should feel like getting the golden piece in Frustration. It should be valuable, exciting and transferable, and never overpowered. When 🎲 Mission Promotion appears, players should think "come on… give me the 6", not "oh great, extra admin".

## Assignment

- The Co-Pilot is **not** chosen before launch. The Go page just explains the role.
- The first thing that happens after launch is a **🛰 Co-Pilot Assigned** event. A reel of passenger avatars spins and lands on one, with a sparkle burst and the line "Seb Wright has been selected as Co-Pilot." It also lists the perks.
- Only passengers can be Co-Pilot, never the Captain.

## Perks

These are deliberately small. There is no score multiplier.

| Perk | Detail |
|---|---|
| **+1 on every challenge win** | Added once when the Co-Pilot wins a challenge outright: most fastest answers in Quickfire Trivia, closest in Estimation Station, first to spot in a Spot Challenge, or the chosen writer in Cosmic Answers. Votes and Silent Missions are shared results, so they don't count. Example: challenge reward +5, Co-Pilot reward +6. |
| **3 power-up slots** | Instead of 2. |
| **Free Shield** | Given on taking the seat. It's used up by the next asteroid or other negative hit. If the new Co-Pilot is already shielded, it arrives as a Shield power-up instead. |
| **Supply drop priority** | Supply drops weight the Co-Pilot ×1.3. Subtle on purpose. |

The Co-Pilot still taps in the Captain's spoken answers. That job now comes with a reason to want it.

## Changing hands

**🎲 Mission Promotion** (about every 7–8 journey minutes, at most one between two challenges)
- A random passenger is chosen. Never the Captain, never the current Co-Pilot.
- The chosen player taps **Roll the dice** on their own phone. It auto-rolls after 10 seconds. Everyone else watches the die shake.
- **1–4:** no promotion. **5:** +5 bonus points. **6:** 🛰 New Co-Pilot. The previous Co-Pilot stands down, and the new one gets the perks with a celebration.

**🛰 Co-Pilot Challenge** (rare: at most once every 45–65 journey minutes, and only after the Co-Pilot has held the seat for 10+ minutes)
- The current Co-Pilot answers one trivia question in 12 seconds on their own phone.
- **Right:** they keep the seat. **Wrong or timed out:** the seat opens, a reel spins across the other passengers and someone new takes it.

**What changes hands.** When the seat moves, the role's perks move with it:
- The old Co-Pilot loses the role's Shield if it hasn't been used yet. A Shield they bought with a power-up stays with them.
- Anything in the old Co-Pilot's third power-up slot moves to the new Co-Pilot.
- The new Co-Pilot gets the 3-slot limit and a free Shield.

Role moments get their own slot in the event queue, next to one event and one voice moment between two challenges, and still with at least 10 real seconds between events.

**🎲 Lucky Roll** (v0.8)
- The power-up rolls a real die: a roll of 1–5 gives +2 to +6 points as before.
- A **6** gives +6 *and* promotes the roller to Co-Pilot. The roller sees a dice animation straight away, and everyone else sees a "🎲 Lucky Roll · 🛰 New Co-Pilot" reveal once the current game ends.
- The Captain can't leave the driver's seat, and a Co-Pilot who rolls a 6 just keeps the seat.

## Keeping it fair

The Captain can never hold the seat, so the Co-Pilot's perks would quietly come out of the Captain's chances. To balance that, **the driver's seat starts every mission with a Shield.**

Full results are in `BALANCE.md`. In summary:

| | 4 players, 45 min | 5 players, 45 min | 6 players, 45 min |
|---|---|---|---|
| Fair share | 25.0% | 20.0% | 16.7% |
| Captain | 25.6% | 20.8% | 18.7% |
| First Co-Pilot | 30.0% | 24.1% | 20.3% |
| Passengers who never hold the seat | 21.1% | 17.5% | 14.6% |
| Old v0.6 rules: Co-Pilot as admin, no perks | 21.7% | 16.9% | 14.5% |

- A good Co-Pilot has a slight edge (+3 to +5 points).
- A player who never gets the seat still wins about 85% as often as a fair share.
- Without perks the role is a burden (about −3 points), which is exactly the "extra admin" feeling this phase removes.

Things I tested and rejected:
- **+1 on every round win** (each trivia question, vote majority) was worth about 5 points on its own. Too strong.
- **The free Shield** was worth about 5 points while the seat rarely moved. More frequent promotions spread it around.
- **No Captain Shield** dropped the Captain to about 19% in 4-player missions.

## Recap

The mission recap has a **🛰 Final Co-Pilot** card under Journey Spaceman. It shows:
- minutes in the seat and how they got it (assigned at launch, promoted, or took the open seat)
- the full hand-over history
- every Mission Promotion roll

Old journeys without Co-Pilot data skip the card.

## Statistics: stored now, shown later

Each journey stores:

```js
j.copilot   // final Co-Pilot id
j.coLog     // [{id, from, to, how:'start'|'promotion'|'reassigned'}], times in journey minutes
j.promos    // [{id, roll, t}]
```

Each account accumulates `user.coStats` from those (`trackCoPilot()`):

| Field | Meaning |
|---|---|
| `assignments` | Times the seat landed on you, by any route |
| `promoted` | Times you became Co-Pilot by rolling a 6 |
| `longestStreak` | Longest continuous time in the seat (minutes) |
| `promosWon` | Mission Promotion rolls of 5 or 6 |
| `promosRolled` | Mission Promotion rolls taken |
| `finalCopilot` | Missions you finished as Co-Pilot |
| `minutes` | Total minutes as Co-Pilot |
| `v` | Schema version |

These are only kept for the signed-in account today. In the real multi-device app, the room server writes the same fields for every player at mission end. The data is enough for future badges ("Seat Thief: promoted 5 times") and Wrapped stats.

## Tuning

All values live at the top of the engine:

- **`PT`:** `coWinBonus`, `coWinMode`, `coSlots`, `coShield`, `coSupply`, `promoBonus`, `capShield`
- **`RULES`:** `promo`, `struggle`, `role`
- **`CYCLE`:** how often promotions are offered

Re-run `node tools/balance-sim.js 4000 final` after changing any of them.
