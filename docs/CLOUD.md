# Cloud accounts and cross-device sync

Spaceman is a static page on GitHub Pages, so it has no server of its own. Phase 14 adds optional cloud accounts so the same email gives the same account on every phone and laptop.

## Architecture (and why)

| Option | Verdict |
|---|---|
| Browser storage only (before) | Per device. A new phone starts empty. |
| Firebase / Supabase (hosted auth + database) | **Chosen: Supabase.** Free tier, email one-time-code login, Postgres, Row Level Security, plain `fetch` from a static page. No server to run. |
| Own backend | More control, far more to maintain. Not needed for this size. |

Flow: email → 6-digit code → session → the app pulls the account row for that user, merges it with anything on the device, and pushes changes back a few seconds after you make them (and when you leave the tab).

- One row per account in `public.accounts` (`data` is the whole profile: friends, journeys, statistics, crew progress, settings, avatar, Spotify settings).
- **Merge rules:** newest account snapshot wins for settings/avatar/totals; journeys, friends, guests and achievements are unioned so nothing made on another device is lost. Deleting a journey leaves a tombstone so it does not come back from an older device.
- Logging out pushes first, then removes the local copy, so shared phones don't keep your data. Offline: changes stay on the device and sync on the next successful push.
- Spotify tokens are **not** synced. They stay on each device, so connect Spotify once per device (one tap).
- Security: the anon key in `config.json` is public by design. Every row is protected by Row Level Security (`auth.uid() = user_id`).

## Turn it on (about 10 minutes)

1. Create a free project at supabase.com.
2. SQL editor → run:

```sql
create table public.accounts (
  user_id uuid primary key references auth.users on delete cascade,
  email text not null,
  data jsonb not null,
  updated_at timestamptz not null default now()
);
alter table public.accounts enable row level security;
create policy "own row read"   on public.accounts for select using (auth.uid() = user_id);
create policy "own row insert" on public.accounts for insert with check (auth.uid() = user_id);
create policy "own row update" on public.accounts for update using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "own row delete" on public.accounts for delete using (auth.uid() = user_id);
```

3. Authentication → Providers → Email: enable, and turn on **email OTP** (put `{{ .Token }}` in the Magic Link / Confirm template so the email contains the 6-digit code). Add `https://charliey36.github.io/Spaceman/` under URL configuration.
4. Settings → API: copy the project URL and the `anon` public key into `config.json`:

```json
"supabase": { "url": "https://xxxx.supabase.co", "anonKey": "eyJ…" }
```

5. Push. Everyone now logs in with an emailed code and gets the same account everywhere. (Supabase's built-in email sender is rate-limited; add your own SMTP for real use.)

## Shared game configuration (same for every user)

`config.json` and `version.json` are served next to `index.html` on GitHub Pages, so every device that loads the page gets the same ElevenLabs proxy URL, voice IDs and Supabase settings, with no per-device setup. The transmission catalogues, Bluff prompts, events and game rules live in the page itself and ship as one versioned file, so every device on the same deployed version sees the same game. `version.json` lets a stale cached copy notice a newer release (`GlobalConfig.newer`). Real avatar images aren't used: avatars are generated from account settings, so they sync with the account.

Not done: a separate remote config database. The page bundle is the single source of truth, which is simpler and cannot drift between devices.
