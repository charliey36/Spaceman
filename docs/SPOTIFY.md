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

## Sources

- [Spotify Developer Policy](https://developer.spotify.com/policy/)
- [Updating the Criteria for Web API Extended Access (Apr 2025)](https://developer.spotify.com/blog/2025-04-15-updating-the-criteria-for-web-api-extended-access)
- [Update on Developer Access and Platform Security (Feb 2026)](https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security)
- [Web Playback SDK](https://developer.spotify.com/documentation/web-playback-sdk)
- [Start/Resume Playback](https://developer.spotify.com/web-api/console/put-play/)
- [Spotify API changes overview (third-party summary)](https://tunelab-developers.pages.dev/blog/spotify-api-changes-2026)
