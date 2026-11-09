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

## "This needs a paid plan": what it really means (v1.5)

**The message was ours, not ElevenLabs's.** Spaceman had one catch-all that turned HTTP 402, and any reply mentioning *payment, paid plan, subscription* or *upgrade*, into "needs a paid plan", and threw away ElevenLabs's own text. Several different refusals landed there. The old code also called every 403 "Invalid API Key". Spaceman has **no plan checks or feature gates of its own**; it only reports what ElevenLabs answers.

| Component | Needs a paid plan? |
|---|---|
| Endpoint `POST /v1/text-to-speech/{voice_id}` (plain text to speech; no streaming, Conversational AI or Agent endpoint) | No |
| Model `eleven_multilingual_v2` (default), Flash v2.5, Turbo v2.5 | No (they use credits) |
| Output `mp3_44100_128` | No (192 kbps MP3 needs Creator or higher; Spaceman doesn't use it) |
| **Voice Library voices** | **Can be.** ElevenLabs says some are limited to paid plans (the owner restricted it, or it has a credit multiplier). Premade voices and your own voices are not. |
| A model the account can't use (`model_access_denied`) | Possibly. Spaceman falls back automatically. |

So with a free account, a valid key and a **premade or own voice**, generation should succeed. If the voice came from the shared Voice Library, that voice is the most likely thing ElevenLabs refuses.

### What you now see on any failure

Settings → Voice shows ElevenLabs's own answer: **HTTP status, error code, error type, message, request ID, endpoint, model, voice ID**, plus (after Test Voice) an account check: plan tier and credits, what the voice is (premade, cloned, library) and which models the account lists. Those lookups need extra key permissions; if the key lacks them they are reported as skipped, never as errors.

| ElevenLabs answer | Headline |
|---|---|
| `invalid_api_key`, `missing_api_key`, 401 | ❌ Invalid API Key |
| `insufficient_permissions`, `missing_permissions` | ❌ API key is missing a permission (names it) |
| `insufficient_credits`, `quota_exceeded` | ❌ Out of ElevenLabs credits |
| `voice_not_found`, 404 | ❌ Voice Not Found |
| `voice_access_denied`, "library voices… upgrade" | ❌ This voice isn't accessible to this ElevenLabs account |
| `model_access_denied`, `unsupported_model`, `model_not_found` | ❌ Model not accepted (then automatic fallback) |
| `feature_not_available`, `subscription_required`, other 402 | ❌ ElevenLabs says this needs a paid plan (with its exact message) |
| other 403 | ❌ ElevenLabs refused the request (403) |

**Automatic model fallback.** If ElevenLabs refuses the model (or gives an unexplained plan error), Spaceman retries once or twice with `eleven_multilingual_v2`, Flash v2.5 or Turbo v2.5 (only those the account lists, when the list is readable). Whichever works is remembered for that key, voice and model, shown in Settings ("refused, using … instead") and used for later lines. A voice problem never triggers a model change.

## "Failed to fetch" (v1.6)

"Failed to fetch" means ElevenLabs **never answered**, so the key and voice were never checked. Spaceman now works out why and says so:

| Headline | Meaning | Fix |
|---|---|---|
| 🚫 Blocked by this page's security policy | The page's Content-Security-Policy (`connect-src`) forbids calling `api.elevenlabs.io`. Typical of a sandboxed or embedded page. | Open Spaceman from a normal web address (GitHub Pages, your own host) or a local server, or use a proxy (`SPACEMAN_CONFIG.elevenLabsBase`). |
| ❌ … (response blocked) | `api.elevenlabs.io` is reachable but the reply was blocked: an ad or privacy extension, a filter, or a proxy without CORS headers. | Private window with extensions off. |
| ❌ … (no connection) | No route to the server at all: offline, VPN, firewall, DNS. | Another network or device. |

## Library voices on a Free plan (confirmed on a real account, v1.7)

A real Test Voice run returned **HTTP 402 `paid_plan_required`: "Free users cannot use library voices via the API."** for voice `21m00Tcm4TlvDq8ikWAM` (Rachel). That proved the key, the network and the endpoint all worked; the only problem was the voice. Rachel is a Voice Library voice, and library voices need a paid plan through the API. (That ID was also the example in earlier docs and the field placeholder, which was misleading. Both are replaced.)

Use a voice from **your own account** instead: ElevenLabs → Voices → *My Voices* → ⋯ → *Copy voice ID*. The Voice settings sheet also has **Fill in free British voices**, which enters George (`JBFqnCBsd6RMkjVDRZzb`, warm British male, suits Atlas) and Daniel (`onwK4e9ZLuTAKqWW03F9`, deeper British male, suits Spaceman). They are premade voices, which Free accounts can use. If Test Voice says "Voice Not Found", copy a voice ID from My Voices instead.

## v1.8 (Phase 14): proxy mode and the "response blocked" cause

**Root cause.** "Request failed (response blocked)" means the browser refused to hand the response (or the request) to the page. The app can only see this as a generic `TypeError`. Real causes, in the order we found them:
1. The page's own Content-Security-Policy forbids `connect-src` to `api.elevenlabs.io`. This is the case inside a claude.ai artifact frame. It is not fixable from inside the artifact.
2. A browser/network layer between the phone and ElevenLabs (VPN, content blocker, school or work network) drops cross-origin calls to `api.elevenlabs.io`.
3. Missing or wrong CORS preflight handling, which only happens on a custom proxy.

ElevenLabs itself does allow browser calls (the earlier 402 `paid_plan_required` came from its servers, so the path works from GitHub Pages). Direct browser calls also mean the key sits in every phone, so the app now supports a proxy.

**Proxy architecture:** App → Cloudflare Worker (`worker/elevenlabs-proxy.js`) → ElevenLabs → audio back. The Worker holds `ELEVENLABS_API_KEY`, only forwards TTS and read-only account paths, caps text at 600 characters and allows only listed origins. The page then talks to one origin you control.

**Set up (about 5 minutes):**
1. `cd worker && npm i -g wrangler && wrangler login`
2. `wrangler secret put ELEVENLABS_API_KEY` (paste your key)
3. `wrangler deploy`, then copy the `https://spaceman-elevenlabs-proxy.<you>.workers.dev` URL.
4. Put it in `config.json` as `"elevenLabsBase"` and push. Every device now uses the proxy with no key and no setup.

In proxy mode the key field is not needed, ElevenLabs is on by default, and test diagnostics run through the proxy too (`/health` on the Worker confirms it is up).

**Voices.** Atlas = Daniel (`onwK4e9ZLuTAKqWW03F9`, calm, authoritative British male). Spaceman = Callum (`N2lVS1w4EtoT3dr4eOWO`, gravelly, theatrical), run slower, less stable and more stylised so it sounds menacing. Both are free premade voices on `eleven_multilingual_v2`, with automatic fallback to Flash/Turbo. Override with `"voices": {"atlas": "…", "sm": "…"}` in `config.json`. These IDs are from memory, so use **Test Voice** to confirm they exist on your account.
