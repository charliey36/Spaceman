# Spaceman
Will you be the Spaceman?

Spaceman is a social driving companion. Every journey with friends becomes a shared space mission, and friendships are measured in miles travelled together.

This repo holds the interactive web prototype: one self-contained `index.html`, built mobile-first.

## Run it

Open `index.html` in a browser. There's no build step and nothing to install. To try real Spotify sign-in, serve it instead (`python3 -m http.server 8000 --bind 127.0.0.1`, then open `http://127.0.0.1:8000/`); see `docs/SPOTIFY.md`. For the phone experience, use your browser's device mode at about 390px wide.

Sign in with any email. There's no password, and accounts are stored in your browser's localStorage. Use **You → Prototype tools → Load sample data** to fill an account with friends, journeys and memories.

## What's in the prototype

| Area | Contents |
|---|---|
| Navigation | Home · Crew · **Go** · Memories · You |
| Crew | Friendship levels and milestones based on miles together, guests and invite/claim codes, removing friends |
| Go | One-tap mission launch, Captain picker, pacing (Relaxed / **Balanced** / Chaotic). The mission picks the games |
| Live mission | Crew total vs Spaceman decides the mission; hostages move credits to Spaceman until the crew pays a rescue fund; Spaceman Fury; 22 milestone outcomes; tap your own avatar for emotes, anyone else's for their player card; a pixel-art breather. Commander Atlas, a human-sounding Mission Control who remembers the journey and reacts to it. Party moments: Chance Time, duels, Spaceman's secret bribes, alliances, hot streaks, Final Approach and end-of-mission Bonus Awards. Crew vs Spaceman: a persistent AI opponent with a personality and a radio voice. It takes hostages (rescue missions, ransoms, swaps), comments on every game, and triggers milestones every 10 miles. Co-Pilot Qualification Roll and king-of-the-hill Seat Challenges. 28 Captain decisions with gambles and callbacks. Passenger mode and Captain (Driver Safe) view, eight games (see `docs/GAMES.md`), power-ups, cosmic events, transmissions, Spaceman roasts, Captain decisions |
| Recap | Crew took control or Spaceman Retains Control, Journey Spaceman, final scores, miles together, Captain rating, awards, mission log, share card preview |
| Memories | Scrapbook of every journey |
| You | Profile, Spaceman avatar editor (8 helmets, 11 visor colours, 8 expressions, 6 suit styles, 10 accents, 7 accessories), Captain rating, driving stats, Year in Spaceman preview |

The live mission runs on a simulated clock where 10 real seconds equals one mission minute. Use the **Prototype: warp 5 minutes** link on the live screen to skip ahead.

Places where real functionality will plug in later (GPS, Spotify, voice, sharing) are marked `FUTURE:` in the code.

## Design docs

| Doc | What it covers |
|---|---|
| `docs/ATLAS.md` | Commander Atlas: the human Mission Control voice, his mood, memory, dialogue system and ElevenLabs setup |
| `docs/ELEVENLABS.md` | ElevenLabs setup, Test Voice, error messages, audit findings and defaults |
| `docs/PARTY.md` | Party-board research (Mario Party, Wii Party, Fortune Street, Party Project) and the real-time mechanics it led to |
| `docs/PRODUCT-REVIEW.md` | Phase 10 research, gameplay, commercial, engagement and TikTok audits, and recommendations |
| `docs/SPACEMAN.md` | Crew vs Spaceman: Spaceman's character, hijacks and rescues, milestones, surprise events, how Spaceman earns, pacing |
| `docs/GAMES.md` | The game catalogue and scoring |
| `docs/BALANCE.md` | Fairness simulations for the Captain, Co-Pilot and crew |
| `docs/COPILOT.md` | The Co-Pilot seat |
| `docs/MULTIPLAYER.md` | Host-authoritative engine and device sync |
| `docs/AUDIO.md`, `docs/VOICE.md` | Sound and voice plans |
| `docs/SPOTIFY.md` | Phase 12 Spotify integration: PKCE sign-in, Share Spotify Data, music commentary, Aux King, and the Developer Policy switches |
| `docs/GAME-DESIGN-ROADMAP.md` | Long-term direction for the games |


## Phase 14

- `docs/CLOUD.md`: cross-device accounts (Supabase) and shared config.
- `docs/ELEVENLABS.md`: proxy mode (`worker/`), voice roles, and the "response blocked" cause.
- `docs/SPOTIFY.md`: real-only Spotify and listening-together limits.
