# ElevenLabs voices: setup, diagnostics and audit (v1.4)

## Setup (2 minutes)

1. In ElevenLabs create an API key (Developers → API Keys). It only needs **Text to Speech: Access**. Set a credit limit on it.
2. Copy a voice ID (Voices → My Voices → ⋯ → *Copy voice ID*). A voice from the shared library must be added to *My Voices* first. Pasting the voice URL also works.
3. In Spaceman open **You → Settings → Voice of Commander Atlas**, paste the key and voice ID(s), and tap **▶ Test Voice**.
4. Test Voice uses what is typed in the form (no Save needed), generates two real lines ("Mission Control test successful. Over." and, if set, a Spaceman line), plays them and shows **✅ Connected** or the exact problem. On success it saves and switches ElevenLabs on.

There are **no environment variables**: Spaceman is a static page. Settings live in this browser (`localStorage` key `spaceman.el`, last result in `spaceman.el.last`). To keep the key off phones, host a small proxy that adds the key and set `window.SPACEMAN_CONFIG = {elevenLabsBase: 'https://your-proxy.example'}` before the app loads. Spaceman will call `{base}/v1/text-to-speech/{voice}`.

## What was wrong (audit findings)

| # | Root cause | Fix |
|---|---|---|
| 1 | **Test button used the *saved* settings, not what was typed.** With nothing saved it spoke with the browser voice and looked broken. | Test Voice reads the form, validates, saves, and plays real ElevenLabs audio. |
| 2 | ElevenLabs only worked if "Use ElevenLabs" was ticked **and** Save pressed, with no feedback either way. | Status panel shows On/Off, which voice is speaking, and why. A passing test switches it on. |
| 3 | **One failed request disabled ElevenLabs for the whole session** (`EL.failed`), with only a vague toast. | Failures are classified. Permanent ones (bad key, missing permission, no such voice, no credits, bad model) pause ElevenLabs until settings change. Temporary ones (rate limit, outage, offline) cool down for 20 s, retry once, then recover by themselves. |
| 4 | Errors were reduced to `ElevenLabs 401`. | Every error names the cause and the fix (below). |
| 5 | Only a trailing `Over.` was split off. "Over and out." and "Mission Control out." were read inline with no beat. | All three sign-offs become their own clip, 1.0 s after the message. |
| 6 | Phones keep audio locked until a tap, and transmissions fire on timers. | The first touches wake the AudioContext; if audio is still blocked the status says so. |
| 7 | Latency: the voice only started requesting audio when the line was due, so there were 1–3 s of silence. | Lines are generated ahead while the transmission animation plays. |
| 8 | The radio chain (300–3,400 Hz band-pass plus saturation) made voices thin, which hurts a voice that should feel like a person in the car. | **Radio effect** setting: *Light* (default), *Full radio* (old sound), *None*. |
| 9 | Cache key ignored model and settings. | Key = voice + model + settings + text, cleared on every save. Old voices can never replay. |

## Error messages

| Situation | What Settings shows |
|---|---|
| No key / no voice ID / model malformed / voice ID not 15–32 letters and digits | Local message, no request sent |
| 401 `invalid_api_key` | ❌ Invalid API Key |
| 401 `missing_permissions` | ❌ API key is missing a permission (set Text to Speech to Access) |
| 404 / `voice_not_found` | ❌ Voice Not Found |
| `quota_exceeded` | ❌ Out of ElevenLabs credits |
| 402 / plan | ❌ This needs a paid ElevenLabs plan |
| 429 | ⏳ Rate limit (retried once, then built-in voice for 20 s) |
| 422 model | ❌ Model not accepted |
| 5xx | ❌ ElevenLabs is unavailable |
| Offline | ❌ No internet connection |
| Network blocked (ad blocker, VPN, page security policy) | ❌ ElevenLabs Request Failed |
| 200 but not audio / empty / undecodable | ❌ ElevenLabs Request Failed |
| Browser holding audio | 🔇 Tap anywhere once |

Whenever ElevenLabs fails, the line is spoken by the built-in voice, a toast explains why (at most once per 30 s per cause), and **Settings → Voice → Diagnostics** keeps the log (requests, status codes, sizes, timings, playback). The key is never logged, only `sk_…abcd (39 chars)`.

## Voice quality defaults

| Setting | Value | Why |
|---|---|---|
| Model | `eleven_multilingual_v2` (picker also offers Flash v2.5, Turbo v2.5, v3) | Best quality for short lines. Flash is fastest and cheapest. v3 is most expressive but slower. |
| Stability | 0.38–0.50 by Atlas's mood | ElevenLabs' "natural" band: lively without wobbling. Excited lines sit lower, curious and concerned higher. |
| Similarity | 0.75 | Close to the voice, with fewer artefacts than 0.8+. |
| Style | 0.2 (Multilingual v2 only) | A little character, little latency cost. |
| Speaker boost | on (Multilingual v2 only) | |
| Speed | 0.96 (smug) to 1.04 (excited) | Spaceman slower and dry, Atlas brighter. |
| v3 | stability 0.5, no speed or style | v3 only accepts 0 / 0.5 / 1. |

## Human delivery

- "Hold on… right." is two clips with a real 0.35 s beat, not one flat read.
- A sign-off is generated on its own, then played one full second after the message, so "Over." lands as a decision.
- Mood changes stability and speed. Punctuation, ellipses and questions are left for the model to perform.
- Spaceman and Atlas use separate voice IDs. Changing an ID applies to the next transmission, with no restart.

## Verified (mocked ElevenLabs API, 56 checks)

This environment cannot reach api.elevenlabs.io, so the suite (`tools/` scratch `el_test.py`) runs the real app in Chromium against a mock of the documented endpoint and error shapes: typed-values Test, both voices, separate "Over.", 1.0 s gap, transmissions and roasts using the right voice and not browser speech, voice change applied instantly, cache reuse and invalidation, all failure modes above (named, built-in fallback, no hammering, recovery after changing the key), 429 retry, ElevenLabs off, no key in logs, no page errors. A real-account check is one tap: **Test Voice**.
