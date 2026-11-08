# Transmission voice: planning notes

**Goal:** Mission Control should sound like another person riding in the car. It should be warm and quick, a little dry, and good with names. **Human first, radio effect second.** The radio texture is seasoning. It must never make the voice harder to understand.

## What the prototype does now (v1.1)

| Technique | How it's done in the browser |
|---|---|
| **The full stop before "Over."** | Every transmission ends with "Over.", spoken as its own utterance after a **one-second pause**, slower (×0.9) and lower (×0.9), like someone letting go of the talk button. "Mission Control out" and "Over and out" were retired so the sign-off is always the same, recognisable word. |
| **Phrase-level pauses** | Sentences are separate utterances (300 ms gaps, 420 ms after a question). Long sentences (70+ characters) also break at commas, colons and dashes with 170 ms breaths. |
| **Moods** | Each line is spoken with a baseline: *smug* for Spaceman's roasts and verdicts (×0.94 rate, ×0.9 pitch), *host* for Mission Control and readings (brighter), *neutral* otherwise. |
| **Emphasis** | Words written in capitals (JACKPOT, EXACT) are spoken on their own, slower and higher, after a short beat. |
| **Natural drift** | Each phrase gets a tiny random pitch change (±3%), so long lines don't sound flat. The first phrase starts slightly slower. Questions lift at the end, exclamations speed up. |
| **Radio processing** | A squelch and tone open the channel. A faint band-limited hiss with the odd crackle runs under the voice and fades out with a click. (Browsers can't filter `speechSynthesis` itself, so the radio feel is built around the voice, never on top of it.) |
| **Voice choice** | Natural/Neural/Online voices first, then Premium/Enhanced, with a preference for a British male voice for Spaceman where one exists. |
| **Openers** | Spaceman varies how it starts ("Ahem.", "Right.", "Hello, crew.", "This is Spaceman.") so it never opens the same way twice in a row. |

The next step is still a neural voice with real emotion control (below). Everything above carries over: the pause before "Over." and the moods map directly onto SSML breaks and style tags.

## Earlier behaviour (v0.6)

Browser speech is the stand-in until a neural voice is wired in. Within that limit:

| Improvement | How |
|---|---|
| Best voice on the device | Voices are scored: "Natural", "Neural" and "Online" voices first, then "Premium" and "Enhanced", then Google UK English, then other en-GB voices. Novelty voices are excluded. |
| Real pauses | Each sentence is a separate utterance, with about 300 ms between sentences, about 420 ms after a question and a short beat before "Over." |
| Natural lift | Questions get a slightly higher pitch. "Over." is said slower and lower, like a sign-off. |
| Names said properly | A small pronunciation map (Zac → "Zack", Seb → "Sebb", Ollie → "Olly"). This becomes a per-user setting later. |
| Written for the ear | Symbols and emoji are removed ("£20" → "20 pounds", "&" → "and"). Openers vary ("Right then, crew.", "Quick one for the whole car."), so it doesn't open with "Incoming transmission" every time. |
| Radio second | The squelch is quieter and shorter, and there's a soft click at the end. The voice itself is not filtered. |
| Content | About 55 discussion prompts, 19 Captain questions and 27 passive Mission Control lines. Each mission deals them without repeats. |

The limit is that the browser can't add emotion, emphasis or reliable name pronunciation, and voices differ on every phone.

## What makes a voice sound human

1. **Script.** Most robotic-sounding speech comes from writing for the eye. Rules for every transmission:
   - Short sentences and contractions.
   - The name early ("Megan, Mission Control has a question").
   - One idea per sentence.
   - A real sign-off.
2. **Context-aware delivery.** Modern TTS models read the meaning of a line and adjust tone. They need to know *what kind* of line it is. Spaceman already knows this: chatter, a discussion prompt, a Captain question, a crew message or a distress signal.
3. **Pronunciation.** Names are the most common failure. They need a dictionary that players control.
4. **Emotion and emphasis.** Use the provider's own controls (below) rather than hacks.
5. **Pacing.** About 150–165 words per minute, with breaths between sentences.

## Provider options, researched November 2026

| Option | What helps us | Watch out for |
|---|---|---|
| **ElevenLabs (Eleven v3, v4)** | Audio tags in brackets direct delivery, such as `[laughs]`, `[sighs]` or `[whispers]`. Ellipses add pauses and capitals add emphasis. Pronunciation dictionaries use alias or phoneme rules. v4 accepts IPA wrapped in slashes. Speed control ranges from 0.7 to 1.2. | v3 and v4 don't support SSML `<break>` tags, so pauses come from punctuation and text. Phoneme tags only work on `eleven_flash_v2`. Dictionaries are case-sensitive. |
| **OpenAI `gpt-4o-mini-tts`** | An `instructions` parameter controls affect and tone, for example "warm, amused British Mission Control officer, slightly deadpan". There are 13 voices. Audio streams as 24 kHz PCM. | Less fine-grained control over pronunciation. Instructions shape the whole clip, not single words. |
| **Hume Octave** | Marketed as context-aware TTS that infers emotion from the text and takes acting instructions. | I couldn't open Hume's TTS documentation. Verify the feature set and terms first. |
| **Browser `speechSynthesis`** | Free, offline and instant. | Quality varies by device. No emotion and no reliable pronunciation. Keep it as the fallback only. |

Also worth knowing: Hume's **Audio Decisions API** returns probabilities for questions about a clip, such as how natural it sounds on a five-point scale. It could screen candidate voices and scripts automatically before people test them. Check pricing and terms first.

Check current pricing, rate limits and terms before choosing. They change often.

## Recommended design

```text
transmission (kind, text, names, target)
  → script writer        adds opener and sign-off by kind, replaces symbols, splits sentences, marks emphasis
  → delivery profile     by kind:
                           chatter = dry and amused
                           discussion = upbeat
                           Captain question = mock-serious
                           crew message = deadpan newsreader
                           distress = urgent
  → pronunciation        per-crew dictionary (alias, or IPA where supported)
  → neural TTS (server)  returns a clean, unfiltered clip; cached by text + profile + voice
  → radio chain (phone)  light filter at 25–40% mix, squelch in and out, faint noise bed
  → speaker              ducks the car's music while speaking
```

**Delivery profiles.** One shared voice, five profiles. For OpenAI, each profile is an `instructions` string. For ElevenLabs, it's a set of audio tags plus a stability and speed setting. Example chatter line:

> `[dry] Sensors show the snack supply dropping faster than expected... [beat] Megan, we're looking at you. Over.`

**Pronunciation.**
- Ask "How do you say your name?" once during profile setup. The player can type a sound-alike spelling or record themselves saying it.
- Store it as an alias, plus IPA where the provider supports it, and share it with every crew the player joins.
- Test each name in the chosen voice when it's saved.

**Radio second.** The current plan (band-pass 300 Hz–3.4 kHz) sounds like a phone line. That's too much for a "person in the car". Instead:
- Wide band-pass (about 180 Hz–6 kHz), light saturation and gentle compression.
- Mixed in at 25–40%, with a clean voice underneath.
- Squelch in (about 160 ms), squelch out (about 90 ms) and a pink-noise bed at about −36 dB.
- A "weak signal" preset (more filter, more noise) only for distress signals and black holes.

```text
clean clip ─┬────────────────────────────────────────────── dry (60–75%) ─┐
            └→ highpass 180 Hz → lowpass 6 kHz → soft clip → compressor → wet (25–40%) ─┴→ out
squelch-in · pink noise bed gated with the voice · squelch-out
```

## Practical points

- **Latency:**
  - Render each clip as soon as the queue schedules the transmission, not when it plays.
  - The 10-second gap between events and players' 2–12 minute delay on queued messages give a natural head start.
  - Fixed prompts are pre-rendered for every profile and shipped with the app.
- **Cost control:**
  - Cache by text, profile and voice. Discussion prompts and chatter are a fixed list.
  - Only player messages and lines containing names need rendering live.
- **Offline:** if a clip isn't ready, use the browser voice with the same script and lines. Always show the text on screen.
- **Moderation:**
  - Player messages are spoken aloud in a car full of people, so filter abuse before rendering.
  - The Captain can mute player transmissions.
- **Safety:** never speak during a Silent Mission. Duck the music, not the navigation.

## How to judge it

- Blind test in a real car with 4–5 people: browser voice vs two neural voices, same 20 lines. Rate "sounds like a person" and "understood every word" from 1 to 5.
- Ship only a voice that scores 4 or more on both, with the radio effect on.

## Milestones

1. Done in v0.6: script writer rules, sentence pacing, name map and lighter radio, using browser voices.
2. Delivery profiles and pre-rendered neural clips for all fixed lines.
3. Per-player pronunciation in profile setup.
4. Server rendering for player messages, with caching and moderation.
5. Radio chain applied to neural clips. A signature Mission Control voice.

## Sources

- [ElevenLabs: Eleven v3 prompting best practices](https://elevenlabs.io/docs/best-practices/prompting/eleven-v3)
- [ElevenLabs: pronunciation](https://elevenlabs.io/docs/best-practices/prompting/pronunciation)
- [ElevenLabs Help: how audio tags work with Eleven v3](https://help.elevenlabs.io/hc/en-us/articles/35869142561297-How-do-audio-tags-work-with-Eleven-v3)
- [Pipecat docs: OpenAI TTS (`gpt-4o-mini-tts` instructions, voices, streaming)](https://docs.pipecat.ai/api-reference/server/services/tts/openai)
- [OpenAI Cookbook: steering text-to-speech](https://developers.openai.com/cookbook/examples/voice_solutions/steering_tts)
- [AI News: Hume's Octave TTS understands context](https://www.ainews.com/p/hume-s-octave-tts-understands-context-outperforms-elevenlabs)
- [Hume: Audio Decisions API](https://dev.hume.ai/docs/text-to-speech-tts/acting-instructions)
