# Party-board research → real-time Spaceman (v1.2)

> Goal: Spaceman should feel less like "a collection of mini-games" and more like **a real-time social Mario Party road trip**. We don't copy turns, boards or dice. We copy the *emotional moments* and translate them into a journey that runs in real time.

## What we studied

| Game | What makes it exciting |
|---|---|
| **Mario Party** (series, incl. Superstars and Jamboree) | Coins and Stars, but the drama comes from the board, not the minigames. **Chance Time** sends coins or Stars between two random players. In Mario Party 1 and 2 it's three blocks: giver, action, receiver; actions include give, take and *swap*. **Bonus Stars** are revealed at the very end, so the leader on the final turn can still lose. Most games award three, picked at random from a bigger pool. **The Last Five Turns** (Mario Party 5) has the last-placed player spin a roulette that changes the rules for the finale: triple-value spaces, all red spaces becoming Bowser spaces, five Stars appearing at once. Boo steals; Bowser punishes; duels put two players head to head. |
| **Wii Party: Board Game Island** | Fast swings: ladders up, chutes down, and late-game events that throw players around. Every round ends with the minigame result moving pieces, so the board position, not the score, is the story. Reviews praise it as a family game "with luck", and criticise how much luck it has. |
| **Fortune Street** | A slow-burn economy: shops, investment and stocks. Momentum compounds: once you own a district, every visit pays you. Comebacks come from other players landing on *your* shops. It's thrilling when it's personal ("you bought MY street?") but long and maths-heavy. |
| **Party Project** | An indie, browser-playable Mario Party-like (30+ boards, 100+ minigames, about 30-minute sessions). Notable for leaning into a **"Final Five"** finale and quick, short sessions, which proves the format works without a console. |
| **Pummel Party** | The party board stripped back to betrayal: items exist to hurt your friends, and the fun is the outrage. |

## The mechanics, and how they feel

| Mechanic | Where it comes from | Why it works | Risk |
|---|---|---|---|
| **Comebacks** | Bonus Stars, Last Five Turns, blue shells | Nobody is ever out of it, so nobody checks out | Too much and winning feels pointless |
| **Randomness** | Chance Time, dice, item blocks | Gives the losing player hope and the leader fear | Pure luck feels unfair if it decides everything |
| **Chaos** | Chance Time swaps, Bowser | Big, loud, *shared* moments everyone reacts to | Fatigue if constant |
| **Steals** | Boo, Chance Time, items | Personal, so it creates rivalries and stories | Can feel mean |
| **Role changes** | 1v3 minigames, teams, Bowser Party | Different alliances every few minutes | Confusing if unexplained |
| **Momentum shifts** | Last Five Turns, Stars changing price, hot streaks | The story has acts: a rise, a fall, a finale | — |
| **Catch-up** | Last-place roulette, bonus coins for losers | Last place gets agency instead of pity | Must not reward losing on purpose |
| **Social reactions** | Everything above, out loud on the sofa | The *room* is the content | Needs time to breathe between moments |

**The big lesson:** the minigames are the excuse, the board is the game. Mario Party's most memorable moments almost never happen *inside* a minigame. They happen around it, to a named player, in front of everyone.

## Translated into Spaceman (implemented)

| Board moment | Spaceman, in real time | Details |
|---|---|---|
| **Chance Time** | 🎰 **Chance Time** (cosmic event) | Three slots spin and land one after another on every phone: a giver, an action (gives 5, gives 10, gives half, **swaps credits with**) and a receiver. **Spaceman is in the pool**, so the crew can swap with Spaceman, or hand it a fortune. |
| **Duels** | ⚔️ **Duel** (cosmic event) | Someone from the bottom half calls out the top passenger. Same question on both phones; the **fastest** right answer takes 5 from the other. Both wrong: Spaceman takes 2 from each. The Captain is never in a duel (driving). |
| **Boo / betrayal** | 🤫 **Spaceman's bribe** (cosmic event) | One passenger's phone, privately: "Take 6 now, I'll take 8." Everyone else sees *"Spaceman is whispering to someone. Act natural."* The leaderboard moves and the car starts guessing. **Revealed in the recap**: "Megan took Spaceman's bribe at minute 23 🗡". |
| **Teams / 1v3** | 🤝 **Alliances** (cosmic event, 4+ players) | Random pairs for the next game. The team whose players win the most credits between them gets +3 each. Yesterday's rival is today's partner. |
| **Hot streaks** | 🔥 **On fire** | Win two games in a row and you're on fire (🔥 on the leaderboard). Your next win pays +3, and whoever ends a streak of 2+ gets +3 as **Streak Breaker**. Atlas notices both. |
| **Last Five Turns** | 🏁 **Final Approach** (mission menu, when you're nearly there) | Last place spins a roulette: double credits until the end · four Bonus Awards instead of three · everyone but the leader +5 · Spaceman loses half its credits · Chance Time right now. |
| **Bonus Stars** | ⭐ **Bonus Awards** (end of mission) | Three random awards from eight (Game Star, Unlucky Star, Hero, Spaceman's Favourite, High Roller, Master Thief, On Fire, Late Surge), +6 each, ties share. **Revealed one by one before the result**, and they decide it. Spaceman gets its own bonus too (+8 for every hostage it took and every bribe accepted). |
| **The room reacting** | 😂 😱 👏 🔥 **Reactions** | Tap on any game result. Emojis float up on every phone. Three 😂 on a result makes it a "funny moment" Commander Atlas will bring up later. |
| **Bowser** | 👨‍🚀 **Spaceman** (already) | Hijacks, audits, road tax and roasts. v1.2 adds surges that double Spaceman too. |

Already in place from v1.1 and kept: milestones every 10 miles (the closest thing to "landing on a space"), bounties, power surges, underdog signals, hostages and rescues, Seat Challenges, 28 Captain decisions with gambles.

**Prototype note:** the bribe is private on screen only. In the current host-authoritative prototype every phone receives the full mission state, so a determined player with developer tools could see who was offered it. A production build should send private events only to their recipient.

## What we deliberately did *not* copy

- **Turns and dice movement.** A car journey is continuous. Everything above is an event that interrupts real time, not a turn.
- **Fortune Street's economy.** Investing and stocks are brilliant but maths-heavy and slow to explain, the opposite of what a moving car needs. A light version (backing another player for the next game) is in the backlog.
- **Pure luck deciding the result.** Bonus Awards reward things players *did*. Chance Time is fate, but it happens mid-journey, not at the finish.

## Validation (simulated, Real Journey Mode, 60 minutes)

| Crew | Spaceman wins | Bonus Awards change the top crew member | Captain is the best crew member (fair share) |
|---|---|---|---|
| 3 players | 31–35% | 19–29% | 22% (33%) |
| 4 players | 24–30% | 19–29% | 28% (25%) |
| 5 players | 39–47% | 19–29% | 20–26% (20%) |
| 6 players | 37–44% | 19–29% | 13% (17%) |

About 150 missions per row; samples this size move by ±5 points. In roughly **one mission in four, the Bonus Awards change who finishes top**, which is the Mario Party feeling. The Captain now gets +1 for each game they win in crews of 5 or fewer (`capWinBonus`), which brings the driver close to a fair share in Real Journey Mode (3 players is still a little low: the Captain can't play Duels).

## Sources

- [Chance Time](https://www.mariowiki.com/Chance_Time), Super Mario Wiki
- [Bonus Star](https://mariowiki.com/Coin_Star), Super Mario Wiki
- [Mario Party 5's Last 5 Turns event](https://mariopartylegacy.com/2011/07/mario-party-5s-last-5-turns-event/), Mario Party Legacy
- [Fortune Street](https://www.mariowiki.com/Fortune_Street), Super Mario Wiki
- [Party Project](https://char64.itch.io/partyproject), itch.io
- [Wii Party review](https://www.nintendolife.com/reviews/2010/10/wii_party_wii), Nintendo Life
- [Pummel Party](https://store.steampowered.com/app/880940/Pummel_Party/), Steam
