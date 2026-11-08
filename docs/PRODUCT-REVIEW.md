# Spaceman product review (Phase 10)

> Product, game design, growth and UX review of Spaceman v1.0, and what changed in v1.1 as a result.

## The verdict

Spaceman's foundation is good: one phone per player, a driver-safe Captain, a Co-Pilot seat, games built around the people in the car, and an opponent. What it lacked was **stakes that change during the journey**. Every game resolved cleanly and independently, Spaceman scored quietly in the background, and nothing that happened at minute 10 still mattered at minute 40. Tension in the best party games comes from *ongoing* jeopardy (someone is the impostor, someone is holding the bomb, someone is in first and about to get hit by a blue shell). v1.1 adds that layer: Spaceman can now **take a crew member hostage**, choices **come back later**, the Co-Pilot seat is **defended like king of the hill**, and every 10 miles something big happens.

## The core question: why Spaceman instead of music?

Music is free, needs no setup, and asks nothing of anyone. Spaceman can only beat it by giving the car something music can't:

1. **A shared story about the people in the car.** "Nobody knew Connor's dream holiday" or "Megan got kidnapped by Spaceman and Lewis swapped places with her" are stories about *these friends*. Music never produces that.
2. **A villain.** Spaceman gives the car a common enemy to laugh at, and a reason to cheer together.
3. **Something to take home.** The recap and Memories turn a drive into an artefact you can share.

Spaceman should also **coexist with music**, not replace it: games are short, the voice cuts in like a radio host, and there's breathing room between games. The aim is "the radio show your car hosts", not "turn the music off and play a game".

---

## Research: what makes social games work

| Product | What creates the feeling | What it looks like inside Spaceman |
|---|---|---|
| **Jackbox (Quiplash, Fibbage, Drawful)** | Phones as controllers; the players write the jokes; reveals as a show; everything learnable in under 30 seconds; comebacks via rising stakes; playful sabotage. Jackbox's creative director: "We set players up to be the stars of the show." | Cosmic Answers prompts are now *about the crew* ("What would Captain Thomas get arrested for?"). The players bring the punchline. Power Surge and milestone overdrive double the stakes late on. |
| **Psych / Fibbage** | Bluffing your friends is funnier than answering trivia. | The Spaceman Bluff keeps the true/false format. Next step: let players write fake facts for each other (backlog). |
| **Kahoot** | The leaderboard between rounds; music and timers; podium reveal. | Spaceman's verdict on every result, the live Crew vs Spaceman banner, three-round Estimation podiums. |
| **Cards Against Humanity / What Do You Meme** | A rotating judge; the room is the content; edgy, but the edge comes from players. | Cosmic Answers keeps a judge (the Captain hears answers read aloud). Prompts invite cheeky answers about each other without the prompt itself being crude. |
| **Werewolf / Mafia / The Resistance / Secret Hitler** | Hidden information, accusation, and talking *is* the game. Elimination creates stories. | Black Box (find the glitch). Hijack is the elimination beat without removing anyone: the captive keeps playing, but earns for the enemy. |
| **Among Us** | Emergency meetings force everyone to talk; trivially easy controls; it exploded through streamers (about 84 million mobile downloads in September 2020). | Rescue Missions are the "emergency meeting": the whole crew stops and works together, out loud. |
| **Codenames** | Cooperative tension: one shared answer and everyone argues. | Corrective Action (one shared number) and Rescue Missions (crew majority). |
| **Exploding Kittens** | Dread that builds every turn. | The hijack ransom grows every 5 minutes, so the crew feels the clock. |
| **Heads Up!** | One phone, a physical, silly moment, and the app records the players' faces, which made a share loop. | Recap and reveal screens designed to be filmed. Next: an auto-generated "mission trailer" clip (backlog). |
| **Mario Kart** | Rubber-banding and the blue shell keep the leader nervous and the last-placed player hopeful. The director on the blue shell: without it "it feels like something's missing… sometimes life isn't fair". | Spaceman targets the **leader** with hijacks and audits. Underdog Signal, jackpots and Spaceman Malfunction spill credits to the back of the field. Bounties put a price on whoever is first. |
| **BeReal / Gas** | A ritual tied to a moment, and social reveals about friends spread fast. Both faded: BeReal fell from about 15 million to under 6 million daily users in five months once the novelty went and the product stopped changing. | Spaceman's "moment" is the journey itself, which recurs naturally. The risk is the same novelty fade, so content depth and new formats matter more than feature count. |

### What creates each feeling

| Feeling | Mechanism (from the research) | In Spaceman v1.1 |
|---|---|---|
| **Laughter** | Player-made content about each other; reveals; a character to mock | Crew-centred Cosmic prompts, Crew Intel reveals, Spaceman's roasts and verdicts |
| **Tension** | Hidden information plus a ticking cost | Hidden lock-ins, hostage ransom ticks, Seat Challenges, gambles |
| **Chaos** | Rules that change mid-game; take-that effects | Bounties, Power Surges, audits, black holes, decisions with risky branches |
| **Excitement** | Big swings late; jackpots | Milestones every 10 miles, double-credit games, Bet it or Bank it |
| **Competition** | A visible leaderboard and someone to beat | Leaderboard with Spaceman in it, VS banner, the leader is Spaceman's target |
| **Memorable moments** | Something happens to *someone*, with a name attached | "Lewis took Megan's place as Spaceman's captive", decision callbacks later in the trip |
| **Replayability** | Combinatorial content, different people each time | 48 Cosmic prompts with names filled in, 28 Captain decisions with random outcomes, 5 story callbacks, 100+ Spaceman lines |
| **Virality** | A short, filmable reveal and a character people quote | Spaceman's voice lines, the recap's outcome card, hostage drama |

---

## Gameplay audit

Ranked from strongest to weakest, as it stood in v1.0.

| Rank | Game or system | Verdict | Why | Decision |
|---|---|---|---|---|
| 1 | **Crew Intel** | Strongest | Only works with these people. Fully driver-safe. Creates instant conversation ("You don't know my favourite takeaway?!"). | **Keep.** Fixed: the subject's own answer no longer shows on their screen. Next: feed friendship levels. |
| 2 | **Black Box** | Strong | Social deduction plus talking out loud. The Captain is a great detective. | **Keep.** Needs 4+ players; consider a 3-player variant. |
| 3 | **Crew vs Spaceman** | Weak → strong | Spaceman scored invisibly, rarely won (11–30% of missions) and never *did* anything. | **Evolved:** Hijack, rescue missions, audits, bounties, a personality, and Spaceman now winning about 35–47% of missions. |
| 4 | **Cosmic Answers** | Good, held back | Prompts were general and tame ("worst crisp flavour"), so the funny came from the prompt, not the players. | **Evolved:** 48 prompts, most about named crew members, built for cheeky answers. |
| 5 | **What Happens Next?** | Good, unsafe | The Captain had to read four endings while driving. | **Evolved:** the Captain's screen shows no text; Spaceman reads the endings aloud on the Co-Pilot's phone and the Captain says a letter. |
| 6 | **Captain's Decisions** | Weak → strong | Only four, with fixed outcomes. The Captain rarely influenced the mission. | **Evolved:** 28 decisions, gambles with branching outcomes, consequences that come back later, about three per 30 minutes. |
| 7 | **Risk It** | Good | Real tension from stakes. | **Keep.** |
| 8 | **Estimation Station** | Good | Best conversation starter. Three rounds can feel long on short trips. | **Keep.** Watch length in real play. |
| 9 | **Road Challenge** | Fine | Uses the road itself; low skill but quick. | **Keep** as an interruption. |
| 10 | **The Spaceman Bluff** | Fine | Fun reveals, but general knowledge isn't social. | **Keep** at moderate frequency. Its format now powers Rescue Missions. |
| 11 | **Secret Assignments** | Not built | Listed in the brief, but never existed in the build. | **Recommend** as the next signature game (see backlog). |

**Replaced:** the random Co-Pilot assignment (now a Qualification Roll), and the one-question Co-Pilot defence (now a Seat Challenge between two players).

---

## Commercial viability audit

### Why would somebody install it?
Because a friend in the car asked them to. Spaceman's install moment is **in the car, from a friend's invite**, not the App Store. That makes the join flow the most important screen in the product: a link or QR code, no account, playing within 20 seconds. Assumption challenged: *"people will discover Spaceman and then plan a trip"*. They won't. Trips come first, and Spaceman is pulled in by one enthusiastic person.

### Why would somebody invite friends?
Because it doesn't work alone. Every player needs a phone, so each session recruits 2–5 new users. That's a strong viral coefficient, *if* joining is effortless. Every second of friction at join time multiplies by the number of passengers.

### Why would people keep using it?
This is the weakest point. **Road trips are infrequent.** Most groups take a handful a year. Assumption challenged: *"daily active use is the goal"*. It isn't. The realistic loop is:
- **Within a trip:** the mission (now with long-running stakes, so it holds attention for an hour or more).
- **Between trips:** Memories, the recap, friendship levels, and stats ("Megan has been captured 4 times").
- **Habitual use cases:** commutes and car-shares, school runs with teenagers, uni students going home, festival and holiday drives, stag and hen trips.

Retention should be measured **per trip** (did the group start Spaceman on its next journey?), not per day.

### Why would people make TikToks with it?
Short, filmable, quotable moments: Spaceman roasting a named friend out loud, a hostage swap, the end-of-mission "Spaceman Retains Control" card, a ridiculous Cosmic Answer read out in the car. See the virality audit below.

### Why would it become a car-journey essential?
If it replaces "Are we nearly there yet?" Spaceman makes the journey *the game*: miles drive milestones, the driver is the Captain, the destination is the finish line. Essential products have a ritual. Spaceman's is "start Spaceman when the engine starts".

### Business model options (not decided)

| Option | Fit | Notes |
|---|---|---|
| **Free with a paid "Mission Pass"** per trip or per month | Good | Matches the infrequent, high-intent use. The host pays, the crew plays free. |
| **Content packs** (Stag Do, Family, Festival, Spicy) | Good | Cosmic prompts, decisions and roasts are now data-driven and easy to package. |
| **Subscription** | Weak | Low frequency makes monthly value hard to prove. |
| **Partnerships** (services brands, car brands, CarPlay) | Later | "Spaceman suggests a stop" is valuable to service stations, but must never feel like an advert. |

### Key risks
1. **Driver safety and perception.** The product must never ask the driver to look or tap. v1.1 makes What Happens Next? fully voice-led for the Captain. Store reviewers and parents will judge this harshly.
2. **Cold start.** It needs 3+ phones. A "one phone, pass it round" mode would widen the market.
3. **Motion sickness.** Screen-heavy games in moving cars make passengers ill. The more Spaceman is played by voice, the better.
4. **Novelty fade** (the BeReal lesson). Content depth and new formats, not more games.

---

## Engagement audit

| Loop | v1.0 | v1.1 |
|---|---|---|
| **Moment to moment** | Games, then a quiet gap | Spaceman's verdict after every game, more events, Captain decisions every ~10 minutes in real time |
| **Across the mission** | Scores accumulate | Hostages with growing ransom, bounties, story callbacks, the seat changing hands, milestones every 10 miles |
| **End of mission** | Crew vs Spaceman result | Plus hostage count, rescues and Spaceman's parting line |
| **Between trips** | Memories, levels | Unchanged. Next: stats about Spaceman ("Times captured", "Rescues led") |

Measured in Real Journey Mode (simulated, 4 players, 60 minutes): about **17 games, 6 Captain decisions, 6 cosmic events, 3 milestones, 1.3 hostage situations, 2.5 Seat Challenges and 6 Spaceman roasts per hour**. The crew rescues about four in five hostages; the rest pay their way out, get released or are still held at the end.

---

## TikTok virality audit

| What gets filmed | Why | Status |
|---|---|---|
| Spaceman roasting a named friend in a radio voice | A character with catchphrases, about a real person | v1.1: stronger personality, radio voice, 100+ lines |
| "Spaceman has captured Megan" and the swap | Drama with a name attached | v1.1 |
| The end card: "Spaceman Retains Control" | A clear win or lose screen | v1.0 |
| Cosmic Answers read aloud | Player-made comedy | v1.1: crew-centred prompts |
| A 15-second auto-made mission trailer | The Heads Up lesson: the app makes the video | **Backlog** (biggest growth lever) |

Recommendations: design the reveal screens to look good in portrait video (big type, one idea per screen; already the case), add a share button on the recap that exports a vertical card, and give Spaceman a recognisable sign-off ("Over.") that people imitate.

---

## Recommendations

### Implemented in v1.1 (highest confidence)
1. **Spaceman Hijack and Rescue Missions.** Spaceman captures the leader; half their winnings go to Spaceman; the ransom grows every 5 minutes; the crew rescues them with a three-question true/false mission, or someone heroically swaps places, or the captive pays to escape.
2. **Milestones every 10 miles:** jackpots, overdrive, road tax, bounties, supply runs, the Bank It or Bet It gamble, hijacks and rescues.
3. **More spontaneous events:** Bounty Posted, Power Surge, Underdog Signal, Spaceman Audit, Spaceman Malfunction, plus story callbacks from earlier decisions.
4. **28 Captain decisions** with gambles, branching outcomes and consequences.
5. **Co-Pilot Qualification Roll** at launch and **Seat Challenges** (king of the hill with defender's advantage, defence streaks and a revenge right for the last Co-Pilot).
6. **Spaceman's personality**, a verdict after every game, and a more human radio voice with a one-second pause before "Over."
7. **New tactical astronaut avatars** and a recognisable gold-visor Spaceman.
8. **Fixes:** typing survives other players submitting; Crew Intel never shows the subject's answer; bot Co-Pilots always answer their defence in time.

### Next (high value, more work)
1. **Join by QR code or link with no account**, and a one-phone pass-round mode.
2. **Mission trailer**: a 15-second vertical recap clip with Spaceman's voice line.
3. **Secret Assignments**: each passenger gets a secret mission ("get the Captain to say 'roundabout'"), revealed at the end. Spaceman awards points for completed ones.
4. **Player-written bluffs**: Fibbage-style fake answers in the Spaceman Bluff.
5. **A neural voice for Spaceman** (see `VOICE.md`) when the app has a backend.

### Later
- Content packs and a Mission Pass.
- CarPlay / Android Auto audio-only mode.
- Friendship levels fed by Crew Intel results.

---

## Sources

- [The Product Genius Behind Jackbox Games](https://www.jasonshen.com/the-product-genius-behind-jackbox-games/), Jason Shen
- ["We set players up to be the stars of the show." Brooke Breit, Jackbox Games](https://roomescapeartist.com/2024/10/22/comedy-collaboration-brooke-breit-creative-director-jackbox-games-repod-s8e4/), Room Escape Artist
- [How Among Us became a mega hit thanks to Amazon's Twitch](https://www.cnbc.com/2020/10/14/how-among-us-became-a-mega-hit-thanks-to-amazon-twitch.html), CNBC
- ["Sometimes life isn't fair": Mario Kart director defends blue shell](https://gamedeveloper.com/design/-sometimes-life-isn-t-fair-i-mario-kart-i-director-defends-blue-shell-game-design), Game Developer
- [How BeReal missed its moment](https://platformer.substack.com/p/how-bereal-missed-its-moment), Platformer
- [Heads Up! game show from the Ellen DeGeneres app](https://www.tubefilter.com/2015/04/14/hln-ellen-degeneres-heads-up-app-game-show/), Tubefilter
- [Experimenting with speechSynthesis](https://www.smashingmagazine.com/2017/02/experimenting-with-speechsynthesis), Smashing Magazine
