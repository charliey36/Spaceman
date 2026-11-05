# Spaceman
Will you be the Spaceman?

Spaceman is a social driving companion. Every journey with friends becomes a shared space mission, and friendships are measured in miles travelled together.

This repo holds the interactive web prototype: one self-contained `index.html`, built mobile-first.

## Run it

Open `index.html` in a browser. There's no build step and nothing to install. For the phone experience, use your browser's device mode at about 390px wide.

Sign in with any email. There's no password, and accounts are stored in your browser's localStorage. Use **You → Prototype tools → Load sample data** to fill an account with friends, journeys and memories.

## What's in the prototype

| Area | Contents |
|---|---|
| Navigation | Home · Crew · **Go** · Memories · You |
| Crew | Friendship levels and milestones based on miles together, guests and invite/claim codes, removing friends |
| Go | One-tap mission launch, Captain picker, journey vibe, challenge line-up |
| Live mission | Passenger mode and Captain (Driver Safe) view, challenges including Cosmic Answers, power-ups, cosmic events, transmissions, Captain decisions |
| Recap | Journey Spaceman, final scores, miles together, Captain rating, awards, mission log, share card preview |
| Memories | Scrapbook of every journey |
| You | Profile, Spaceman avatar editor, Captain rating, driving stats, Year in Spaceman preview |

The live mission runs on a simulated clock where 10 real seconds equals one mission minute. Use the **Prototype: warp 5 minutes** link on the live screen to skip ahead.

Places where real functionality will plug in later (GPS, Spotify, voice, sharing) are marked `FUTURE:` in the code.
