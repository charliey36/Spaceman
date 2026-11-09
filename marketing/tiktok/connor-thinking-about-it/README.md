# TikTok: "Connor is thinking about it"

`spaceman_connor_explained.mp4`: 48.6 s, 1080x1920, 30 fps, H.264 + AAC, about -14.7 LUFS. Ready to post.

Megan narrates: what Spaceman is, a Bluff round, Spaceman kidnapping her, the crew paying 20 of 30 points, then Connor refusing to pay the last 10 because she'd go back to first place. Ends on "Thank you, Connor." and the end card "Who's the Connor in your group?"

## Script

| Time (s) | On screen | Audio |
|---|---|---|
| 0.0 | Launch countdown, "5 phones joining", Mission started | Megan: "So we played this road trip game called Spaceman." |
| 3.6 | Next game: The Spaceman Bluff | "Everyone plays mini games on their own phone." |
| 6.3 | "The first computer mouse was made of wood." | "And there's an AI called Spaceman…" |
| 8.6 | Reveal: TRUE, Spaceman takes 10 | "…who steals your points when you get things wrong." |
| 11.2 | Hijack: "You've been captured" | "Then, halfway through, he kidnapped me." Spaceman: "Megan is with me now." |
| 16.0 | Rescue fund 20/30 | "To get me back, my friends had to pay 30 points." |
| 19.1 | Spotlight on Connor (36) | "20 in. 10 to go. And Connor had 36." |
| 23.1 | Connor's phone | Megan: "Connor. It's ten points." / Connor: "Yeah, but if I pay, you're back in first place." / Megan: "I've been kidnapped!" |
| 29.9 | Transmission | Spaceman: "Connor is thinking about it." (beat of silence) |
| 34.1 | Megan's phone, 😡 and 🫡 emotes | Megan: "He is not thinking about it." / Connor: "I'm thinking about it." |
| 37.9 | Ransom, Connor takes first | "He did not pay. Spaceman drained my points, and Connor took first place." |
| 42.6 | Transmission | Spaceman: "Thank you, Connor." |
| 45.2 | End card | Caption: "Who's the Connor in your group?" |

## Voices

Kokoro (open source, Apache 2.0, commercial use allowed): Megan = `bf_emma`, Connor = `bm_fable`, Spaceman = `bm_george` pitched down with a little room. Processed takes are in `voices/`. ElevenLabs takes (Callum for Spaceman, Lily for Megan, Will for Connor) can replace them on the same timings in `build/audio2.py`.

## Rebuilding

Everything is in `build/`:

1. `voices_kokoro.py` generates the raw lines (needs `pip install kokoro-onnx soundfile` plus the `kokoro-v1.0.onnx` and `voices-v1.0.bin` model files from the kokoro-onnx GitHub releases).
2. Serve the repo root on port 8771, then run `capture3.py`. It drives the real app with Playwright under virtual time, so every frame is captured at exactly 30 fps at 1080x1920. `harness.py` expects a `fonts.css` next to it that inlines Geist, Geist Mono and Unbounded (from `@fontsource/*`), so the capture uses the app's real fonts.
3. `comp2.py` composes the phone card, captions, subtitles and spotlights using `t2.json` (scenes), `c2.json` (captions) and `o2.json` (spotlights).
4. `audio2.py` mixes the voices, sound effects and music bed, then mux with ffmpeg.
