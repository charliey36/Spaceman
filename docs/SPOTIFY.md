# Spotify in Spaceman

Two parts: **Phase 12 music integration** (built, described first) and **Name That Intro** (still blocked, kept below).

## Phase 12: Spotify integration and music personality

### What's built

| Area | Where | Notes |
|---|---|---|
| Connect / disconnect / reconnect | `Spotify` module, You → Music, Spotify sheet | Authorization Code + PKCE (S256). No client secret anywhere. |
| Status | You → Music, mission menu, music bar | "Spotify Connected", "Connect Spotify", "Reconnect Spotify", "Spotify unavailable", "Spotify access blocked" |
| 🎵 Share Spotify Data | `settings.spotifyShare`, default **off** | Off = the engine never receives your profile or songs, so no music roasts, no music Crew Intel, no profile, no now-playing for the crew. Turning it off mid-journey removes you at once (`music-set` with `p:null`). |
| Data | `u.spotify.profile` | Top artists (10, plus genres counted across the top 20), top tracks (10), recently played (50: name, artist, hour), refreshed at most every 30 min or on demand. Playback state is polled every 12 s during a journey, only while the page is visible, and kept in memory only. |
| Mission music bar | `musicBarHTML()` above the tray | Album art, track, artist, whose aux, Spotify mark, links back to the track on Spotify. Falls back to tasteful one-line states. |
| Profiles | You page, friend sheets | Top genres, artists and tracks, with link-backs and attribution. |
| Commentary and roasts | `MUSIC` catalogue + `musicCands()` in the engine | Genre-family lines, top artist and track, repeat listening, artist loyalty, variety, late-night plays, sad-song count, pair overlap, zero overlap, genre clash, the odd one out, crew favourite. Never repeated within a mission. |
| Song reactions | `songIn()` | Same song again, artist runs, aux hogging, "that's in Megan's top artists", crew anthem, "nobody here likes this". Rate-limited. |
| Music Crew Intel | `musicQ()` | "Which artist is in Megan's top artists?", "Which genre does Connor listen to most?", top tracks. Only about a sharing player; decoys come from the rest of the crew first. |
| Aux King | `S.aux`, `musicRecap()` | Tracks songs introduced, artists played and music moments. Awards: Aux King, Repeat Offender, Most Questionable Taste, Hidden Music Expert. |
| Journey recap / memories | `musicRecapHTML()` | Most played song and artist, crew favourite artist, Aux King, music moments, music awards. |
| Demo provider | `SAMPLE_MUSIC`, `DEMO_ME` | "Try the demo" works with no Spotify account. Sample friends get simulated profiles (Lewis has opted out; guests have none) so crew features can be tried with one phone. |

### Setting up real sign-in

1. Create an app at developer.spotify.com/dashboard and tick **Web API**.
2. Under **Settings → Redirect URIs**, add these exactly, then **Save**:

   | Where | Redirect URI |
   |---|---|
   | Production (GitHub Pages) | `https://charliey36.github.io/Spaceman/` |
   | Local testing | `http://127.0.0.1:8000/` (or register `http://127.0.0.1/` with no port, and Spotify accepts any port) |

   Letter case, the trailing `/`, `https` and the port all count. `localhost` isn't accepted. Don't add a `/callback` path: the app is a single page, so Spotify sends people back to the page itself.
3. Put the Client ID in `SPOTIFY_CONFIG.clientId` in `index.html`, or paste it into **You → Music → Spotify app settings**.
4. Development Mode: the app owner needs Premium, and only 5 allow-listed users can sign in (**User Management**). Anyone else gets "Spotify access blocked".
5. To test locally, run `python3 -m http.server 8000 --bind 127.0.0.1` in the project folder and open `http://127.0.0.1:8000/`. Opening `index.html` as a file can't work with Spotify.

Scopes: `user-top-read`, `user-read-recently-played`, `user-read-currently-playing`, `user-read-playback-state`. Nothing that writes.

### Configuration ("environment variables")

There's no build step, so configuration lives in `SPOTIFY_CONFIG` at the top of the Spotify module:

| Setting | Purpose | Override |
|---|---|---|
| `clientId` | Spotify app Client ID (public, not a secret) | Pasted in the app, or `window.SPACEMAN_SPOTIFY_CLIENT_ID` |
| `redirectUris[host]` | The one Redirect URI used on that host | Advanced field in the app, or `window.SPACEMAN_SPOTIFY_REDIRECT_URI` |

Any other host uses its own address in a fixed form: `index.html` removed and a trailing `/` added. No client secret exists or is needed.

### OAuth fix (v1.3.1): root cause of "redirect_uri: Not matching configuration"

- **Cause:** the app built `redirect_uri` from whatever address the page happened to be open at (`location.origin + location.pathname`). GitHub Pages serves the app at `/Spaceman/`, `/spaceman/`, `/Spaceman/index.html` and `/spaceman/index.html`, so the same app sent four different values. Spotify matches character for character, so anything not registered exactly failed after login.
- **Why people got stuck:** a failed redirect means Spotify never sends anyone back, so the half-finished attempt was never cleaned up. Once a Client ID was saved, the Spotify sheet stopped showing the Redirect URI and settings, so there was no way to see or fix the mismatch. Spotify remembers its own login, so every retry failed again instantly.
- **Fix:** one fixed Redirect URI per host (`SPOTIFY_CONFIG`). The same value is stored with the attempt and reused for the token exchange. A tab that comes back without an answer is detected (per-tab sessionStorage marker), cleaned up, and gets a "Spotify connection failed" sheet with the reason, the Redirect URI it sent, Try again, app settings and Reset. Retries after a failure or disconnect send `show_dialog=true`, so a different account can be chosen.
- **Logging:** every step (`authorize`, `callback`, `token exchange`, `refresh`, `failed`) goes to the browser console as `[Spotify] …`, and the last 40 steps appear under **Connection log** in the Spotify sheet. Codes, tokens and the PKCE verifier are never logged.

### Production notes

- Tokens sit in `localStorage` under `spaceman.spotify.v1`, separate from the account record, and are deleted on disconnect along with the stored profile. In production, move the refresh token server-side (a backend-for-frontend), and add a privacy policy explaining exactly what is read and kept.
- 401 → one silent refresh; 429 → back off for `Retry-After`; 403 → "access blocked"; a refresh that returns no new refresh token keeps the old one.
- Only the sharing player's own phone talks to Spotify. Other phones only see what the engine sends, via `music-set` and `song` intents, so the multiplayer room never holds anyone's tokens.

### ⚠️ Spotify Developer Policy: read before shipping

Some of the brief conflicts with Spotify's Developer Policy as written:

| Feature | Policy risk | Switch |
|---|---|---|
| Counts and percentages from listening ("played X 14 times", "60% of top artists"), the odd one out, Repeat Offender, Most Questionable Taste, Hidden Music Expert | Prohibits analysing Spotify content or the service, including deriving user metrics and building user profiles | `MUSIC_DERIVED = false` turns all of these off and keeps plain facts (top genre, top artist, shared artist) |
| Music Crew Intel | "Do not create a game, including trivia quizzes" | Set `RULES.music.intel = 0` |
| LLM-written roasts | No feeding Spotify content into ML/AI models | Not used: every line is a hand-written template |
| Attribution | Spotify marks and link-backs required next to Spotify content | Done: logo plus "Music data from Spotify", and items link to Spotify |
| Disconnect | Easy disconnect, delete the data | Done |

**Recommendation:** fine for a private prototype with your 5 Development Mode testers. Before any public launch, ship with `MUSIC_DERIVED = false` and music Crew Intel off, or get written approval from Spotify. Extended access is now only for established, scalable apps, so plan for Development Mode limits either way.

---

# Name That Intro with Spotify: planning notes

**Status: removed from active gameplay in v0.6 and shown only as a planned-feature placeholder. Blocked by Spotify's Developer Policy. Don't build this on Spotify without written approval.**

## The idea

1. The host connects Spotify and picks a playlist, their Liked Songs or a shared crew playlist.
2. Spaceman picks a random track and plays its first 5 seconds.
3. Everyone guesses on their own phone.
4. The fastest correct answer wins the round and the points.

## Why it's blocked

| Issue | Detail |
|---|---|
| **Games are prohibited** | Spotify's Developer Policy says: "Do not create a game, including trivia quizzes." A song-guessing game is exactly that. Developers have asked about this many times on the Spotify for Developers forum, and the rule hasn't changed. |
| **Playback needs Premium** | Controlling playback (Web Playback SDK or the Start/Resume Playback endpoint) only works for Premium accounts. Mobile-only Premium plans don't work with the Web Playback SDK. |
| **No more 30-second previews** | Since 27 November 2024, `preview_url` and several endpoints are restricted to older apps. New apps can't use previews as a workaround. |
| **Development mode is tiny** | Since February–March 2026, development mode needs a Premium account, allows 5 test users per Client ID and only one Client ID per developer. |
| **Extended access is selective** | Since 15 May 2025, extended access is only for "established, scalable and impactful" use cases that support Spotify's platform strategy. |
| **Commercial use** | The Web Playback SDK can't be used in commercial projects without Spotify's prior written approval. |

## If Spotify ever approves it: technical shape

- **Auth:** OAuth with PKCE on the host's phone. Scopes: `user-read-playback-state`, `user-modify-playback-state`, `playlist-read-private`, `user-library-read`.
- **Playlist:** fetch track IDs on the host, shuffle, and never show titles to the crew before the reveal.
- **Playback:** play on the car's active Spotify device with `PUT /me/player/play` (`uris` and `position_ms: 0`), then pause after 5 seconds.
- **Guessing:**
  - Multiple choice: 4 titles on each phone, built from the same playlist.
  - Or free text with fuzzy matching.
  - Or the existing buzzer flow, with a passenger confirming answers.
- **Timing:** the room timestamps the start of playback. Each phone's guess time comes from clock-offset-corrected `sentAt`, the same as buzzer rounds in `MULTIPLAYER.md`.
- **Shared session:** only the host's phone talks to Spotify. Every other phone just gets the round state from the room.

## Recommended path

1. **Keep it out of gameplay until it's done properly.** Since v0.6, Name That Intro is not in the challenge rotation. It appears only as a disabled "🎵 Planned feature · Future Spotify integration" card on the Go page and in the between-challenges picker. A "bring your own music" version, where someone plays a song from any app and Spaceman only handles answers and scoring, could return later as an interim option.
2. **Ask Spotify for written approval** for a party-game use case, with the Premium-only and host-only playback limits above. Assume the answer is no until it isn't.
3. **Look into licensed alternatives** for a built-in music round:
   - Apple MusicKit (check Apple's terms for games and quizzes before relying on it)
   - licensed preview libraries from music services built for businesses
   - royalty-free or commissioned "sound-alike" intros, which work as a stopgap
4. **Use Spotify where it is allowed.** "Now playing" logging for Memories and the Year in Spaceman top song isn't a game, and still needs to follow the Developer Terms.

**v1.3 note:** when nothing is playing, the "Add your music to the mission" bar only appears during breathers, so games, events and results cards keep the whole screen. A song that is actually playing still shows at all times.

## Sources

- [Authorization Code with PKCE](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow)
- [Redirect URIs](https://developer.spotify.com/documentation/web-api/concepts/redirect_uri)
- [Spotify Design & Branding Guidelines](https://developer.spotify.com/documentation/design)

- [Spotify Developer Policy](https://developer.spotify.com/policy/)
- [Updating the Criteria for Web API Extended Access (Apr 2025)](https://developer.spotify.com/blog/2025-04-15-updating-the-criteria-for-web-api-extended-access)
- [Update on Developer Access and Platform Security (Feb 2026)](https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security)
- [Web Playback SDK](https://developer.spotify.com/documentation/web-playback-sdk)
- [Start/Resume Playback](https://developer.spotify.com/web-api/console/put-play/)
- [Spotify API changes overview (third-party summary)](https://tunelab-developers.pages.dev/blog/spotify-api-changes-2026)
