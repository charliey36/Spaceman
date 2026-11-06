# Sound effects (v0.8)

**Direction:** modern sci-fi UI. Spacecraft control systems, subtle and futuristic. Premium, not cartoonish, never loud.

All sounds are synthesised live with the Web Audio API (`SFX` in `index.html`):
- There are no audio files to download or license.
- Every sound uses the same palette: clean sine and triangle tones, filtered noise and a little high shimmer.
- Everything runs through one gain stage (×0.5) and a gentle compressor, so no cue is louder than the rest.

| Moment | Sound | Who hears it |
|---|---|---|
| 🚀 Start mission tapped | Filtered noise rising from a low rumble to a bright whoosh, a sub-bass lift, an ignition tone and a soft two-note shimmer (about 2 s) | This phone |
| Mission live | Two-note rising chime with a soft sub | This phone |
| Game starts / Spot Challenge | Short rising pair / two quick radar pips | Every phone |
| Trivia reveal | Bright two-note confirm, or a soft falling pair if nobody got it | Every phone |
| Game complete | Quiet confirm | Every phone |
| Power-up collected | Quick upward triangle arpeggio | Only phones that received one |
| Asteroid detected | Low filtered rumble with two muted warning beeps | Every phone |
| Supply drop / solar flare | Crate click and a two-note pickup | Every phone |
| Black hole | Falling sweep | Every phone |
| Co-Pilot assigned or changes | Sonar ping with two echoes | Every phone |
| Mission Promotion | Selection blip, dice rattle, then a fanfare on a 6, a pickup on a 5, or a soft miss | Every phone |
| Mission end | Gentle three-note descent | This phone |
| 👑 Journey Spaceman crowned | Low swell, a warm major chord and a rising sparkle | This phone, on the recap |
| Milestone unlocked | Two-partial bell | This phone, on the recap |

**Controls:**
- *Sound effects* on or off is in the mission menu, saved per account.
- Transmissions keep their own *Read aloud* switch.

**Mobile notes:**
- iOS only allows audio after a tap, so the first sound plays from the Start mission tap, which also unlocks audio for the rest of the mission.
- Phones on silent mode may mute Web Audio.

**Later:**
- Swap the most important cues (launch, crowned) for professionally produced sounds in the same style.
- Duck the car's music under cues.
- Add a user volume slider.
