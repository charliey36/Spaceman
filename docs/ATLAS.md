# Commander Atlas (v1.2)

> The voice of Mission Control. Players should forget they're listening to software and feel like a real person is following their journey.

## Who he is

| | |
|---|---|
| **Role** | Mission Control. The host, the commentator and the crew's friend on the radio. Firmly on the crew's side against Spaceman (and a bit scared of it). |
| **Sounds like** | Male, British, mid 30s to 40s. Warm, quick, confident. A radio presenter's energy with NASA CAPCOM calm when things go wrong. |
| **Personality** | Jokes a lot, a little sarcastic, celebrates properly, remembers everything, never cruel. Says "Alright", "Right", "Okay", "Hmm", "Hold on…". Self-corrects ("That's 11 miles. Wait, no… 12."). |
| **Never** | A sat nav, a notification, an AI assistant. Never "Attention crew", never "Mission updated", never the same opener twice in a row. |

Spaceman (the opponent) keeps its own voice: smug, dry, lower. The two characters talk about each other.

## How a line is built

Every transmission is assembled live from what's happening in *this* car:

```
[radio crackle, about 8%] + [opener for his mood] + [what's actually happening, or a memory] + [sometimes a tag]
   "Stand by… right, I'm back."   "Okay, wow."   "Captain Thomas is leading. While driving. That's just showing off."   "Carry on."
```

- **14 ways to address the car**, rotated without repeats: crew, team, travellers, space cadets, explorers, mission team, people in the vehicle, legends, survivors, my favourite crew, you lot…
- **Openers by mood** (6 moods, 44 openers), **15 situations** with 64 lines, **11 memory types** with 21 templates, **10 game intros**, **11 event moments** with 30 lines, plus tags, radio lines and Captain openers. That's over 200 hand-written fragments, which combine into thousands of different transmissions. Every list is dealt like cards: nothing repeats until the list runs out.
- **Radio effects** ("Commander Atlas to Spaceman crew… do you copy?", "Signal's breaking up…") appear on about 8% of lines, with a burst of static.

## Context awareness

Atlas chooses what to talk about from the live state, weighted towards what's most interesting right now:

| Situation | Example |
|---|---|
| Just started | "We're off. Seatbelts on, snacks out, dignity optional." |
| Car hasn't moved in 5 minutes | "Are we travelling somewhere, or are we just enjoying this car park?" |
| Distance | "That's 11 miles. Wait, no… 12. Look at you go." |
| Long journey (45+ min) | "We've been out here for quite a while now. Nobody's started a rebellion yet, which is encouraging." |
| The driver is winning | "I've got to admit, the driver is carrying this mission right now." |
| A passenger is winning | "Right now Oliver is showing the rest of you how this game is played." |
| Someone's last | "I won't mention who's in last place. Actually, I will. It's Jake." |
| Close at the top | "Alright, this just got interesting. Megan and Lewis, separated by a single credit." |
| Spaceman ahead / behind | "Small problem. The evil robot is winning. Again." |
| A hostage | "Megan is still with Spaceman. Somebody, please, do something heroic." |
| A hot streak, a Co-Pilot defending, the destination | … |

## Memory

Atlas remembers the journey: disasters (−5 or worse in a game), star games (+8), exact estimates, hostages, rescues, Chance Time results, duels, comebacks (a new leader who was 8+ behind), funny moments (three 😂 on a result), streaks and streak-breakers. Six or more minutes later he brings one back, with how long ago and where that person stands now:

> "Tom, after that disaster twenty minutes ago, I can't believe you're winning."
> "Still thinking about Chance Time half an hour ago. Lewis gives half his credits to Spaceman. Absolute chaos. Loved it."

Each memory is used once.

## Mood

Atlas has six moods: **excited, curious, concerned, impressed, amused and competitive**. Events set his mood for a few minutes (a hijack makes him concerned, a rescue or a duel excited, Chance Time amused, a clean game for the crew impressed). After that he drifts back to what the leaderboard says (close race → competitive, Spaceman ahead → concerned). Mood changes **what he says** (openers) and **how he says it**: excited is faster and brighter, concerned slower and lower. Each situation also has a natural tone, so a worried opener never lands on good news.

## Delivery

| Technique | Built-in voice | ElevenLabs |
|---|---|---|
| **Pause before "Over."** | 1 second, then "Over." in a lower, settled voice | 1 second between two separately generated clips |
| **Hesitations** ("Hold on…") | 480 ms beat at every "…" | Natural from the model |
| **Mood** | Rate and pitch per mood | Stability per mood (0.35 excited → 0.45 concerned) |
| **Two characters** | Atlas gets the best British voice on the phone, Spaceman the next-best different one, a little lower | Separate voice IDs |
| **Radio sound** | Squelch, hiss bed, static bursts *around* the voice | Real processing *of* the voice: band-pass 300–3,400 Hz, presence lift at 1.8 kHz, soft saturation, compression, hiss bed |

## ElevenLabs

Mission menu → **Voice of Commander Atlas**. Paste an API key and voice IDs. Stored only in that browser.

| Setting | Value | Why |
|---|---|---|
| Model | `eleven_multilingual_v2` (editable) | Best expressiveness |
| Stability | 0.35–0.45, by mood | Lower = more emotional range |
| Similarity | 0.80 | Stays recognisably the same person |
| Style exaggeration | 0.20 | Personality without hamming it up |
| Speaker boost | On | Clarity over car noise |

Voice brief: male, British, mid 30s to 40s, warm, charismatic, confident, slight humour, radio-presenter energy. Reference points: a Radio 1 breakfast presenter's warmth, a motoring presenter's storytelling confidence, NASA CAPCOM calm.

If ElevenLabs fails (no key, network, quota, or the page blocking the request), Atlas falls back to the built-in voice and says so once. A production app should call ElevenLabs from a server so the key never sits on a phone.
