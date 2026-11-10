# treg AIGC promo: hook shot plan v6, 0:00–0:11.5 (Nov 10, 2026)

**v6: the hook is cut to the lines.** Every second has someone talking, except two silent moments of 0.5 s at most: the open (S1) and the push into the screen (S5). Gaps between lines are 0.2 s at most. The walk from the sofa to the desk is gone: S1 cuts straight to the pair already at the desk (S2). The hook is now 11.5 s instead of 13 s.

**Rules for timing**
- No stretch without a line runs longer than **0.5 s**.
- Between two lines: **0.2 s** at most (one breath).
- A beat lasts as long as its line plus at most 0.2 s. Lines are never sped up past ±8% to fit; if a line runs long, the beat grows, not the silence.
- Clips are generated at the model's minimum length and trimmed in the edit to the slot below.

## 0. Timeline

| Beat | Time | Length | Who speaks | Line | Audio file |
|---|---|---|---|---|---|
| S1 | 0:00.0–0:00.5 | 0.5 s | nobody | (silent open: sofa, they rise) | — |
| S2 | 0:00.5–0:02.7 | 2.2 s | LEADER | "Still paying Higgsfield for this?" | `audio/vo_leader_still-paying.mp3` (2.1 s) |
| S3a | 0:02.7–0:05.0 | 2.3 s | HERO | "We made Higgsfield three x cheaper." | `audio/vo_hero_3x-cheaper.mp3` (2.2 s) |
| S3b | 0:05.0–0:09.5 | 4.5 s | HERO | "I cost [$HF] on Higgsfield… and now [$TREG] on treg." | `audio/vo_hero_price.mp3` (to record) |
| S4 | 0:09.5–0:11.0 | 1.5 s | LEADER | **TBD** | `audio/vo_leader_s4.mp3` (to record) |
| S5 | 0:11.0–0:11.5 | 0.5 s | nobody | (silent push into the screen; hand-off to the screen recording) | — |

The camera man's "How??" (`vo_camera_how.mp3`, 0.8 s) is not in the hook. If it comes back, it goes straight after S3a's line with no gap, and everything after it moves 0.8 s later.

## 1. References — exactly these 9 images, in this order, in every keyframe call

Base: `https://raw.githubusercontent.com/cicadaaa/ugc-assets/main/`

| # | File | What it fixes |
|---|---|---|
| 1 | `cast/leader.jpg` | LEADER's face (left) and outfit front + back (right, head removed) |
| 2 | `cast/hero.jpg` | HERO |
| 3 | `cast/feather.jpg` | FEATHER |
| 4 | `cast/slicked.jpg` | SLICKED |
| 5 | `cast/silverman.jpg` | SILVERMAN |
| 6 | `blocking/previz/<beat>.jpg` | THE FRAME: the real empty street with stand-ins pasted where every person and every piece of furniture goes (grey box with a name = person, red dot = nose/facing; coloured boxes = furniture) |
| 7 | `props/sofa_table.jpg` | what the sofa and travertine table look like |
| 8 | `props/desk_set.jpg` | what the desk, laptop, lamp and chair look like |
| 9 | `plates/scene_empty.jpg` | the location itself: building, sidewalk, curb, zebra crossing, light. Every frame's street must look exactly like this. |

**Rules**
- Never pass anything else: no keyframe, no older plate, no generated street.
- S5 has no previz (the camera is behind LEADER): it uses images 1, 2, `plates/scene_empty.jpg` and `props/desk_set.jpg`, with the stone building behind as the background.
- The prompt states the **left-to-right order in the frame** in words (for example "HERO on the LEFT, LEADER on the RIGHT"). Without it the model swapped the pair in 4 of 7 frames.
- **Video calls** (Seedance) take only the approved keyframe as `first_frame` plus the line's audio. The video prompt describes people by their anchors (bob + kimono, platinum + tank).
- **Order of work:** keyframe → Gate 1 → audio → 480p draft → Gate 2 → 720p final. A still that fails is re-rolled, never fixed in video.

## 2. The set and the blocking (fixed for the whole hook)

- **Location** (`plates/scene_empty.jpg`): a granite sidewalk along an old carved-stone building with fluted columns and warm-lit shop windows; a wide zebra crossing runs out from the curb, stripes parallel to the curb.
- **Sofa:** on the crossing at the far curb, by the building (left-centre of the frame from the main camera). Travertine table at its road end.
- **Desk:** on the crossing nearer the camera, centre-right of the frame, just right of the sofa. Laptop on the end nearest the sofa; dome lamp on the far end; tan chair, empty, at the near side.
- **The laptop's screen ALWAYS faces the sofa.** On the desk the camera sees only the blank silver lid. In S5 LEADER, her back to the sofa, lifts it and holds it at chest height: the screen faces her (still the sofa direction), the lid faces away.
- **HERO is always on LEADER's right.** Facing the main camera that puts HERO on the LEFT of the frame, LEADER on the RIGHT, LEADER nearer the desk. In S5, seen from behind, HERO is on the LEFT of the frame.
- **Crew:** FEATHER on the sofa seat, SILVERMAN on the armrest, SLICKED on or by the travertine table. They stay on the furniture; nobody stands behind the sofa or at the desk.
- **Camera man:** the only person on the sidewalk side; never seen.
- Top view and marks: `prompts/shotdiagrams.py` and `prompts/previz.py` (calibrated camera on `scene_empty.jpg`) render `blocking/previz/<beat>.jpg`.

**Consistency contract**

| What | Comes from | Never from |
|---|---|---|
| Faces | `cast/<name>.jpg`, the one face on the left | a keyframe, the prompt's imagination |
| Outfits | `cast/<name>.jpg`, the headless outfit on the right (LEADER's obi bow: her back photo) | — |
| The street | `plates/scene_empty.jpg` | any other plate |
| Furniture look | `props/sofa_table.jpg`, `props/desk_set.jpg` | — |
| Furniture and people position | the beat's `blocking/previz/<beat>.jpg` + the left-to-right line | the model's own layout |

## 3. Locked blocks (paste word for word)

**Camera:**
```
Shot on a Fujifilm X100VI with its fixed 23mm f/2 lens (35mm equivalent), Eterna film simulation, held horizontally, 16:9 landscape frame, handheld by a young man at his chest height. Eterna look: low saturation, soft gentle contrast, lifted shadows, smooth highlight roll-off, muted cyan-green in the shade. Shallow depth of field at f/2 with a softly blurred street behind the subject, slight glow on highlights when close up, fine film-like grain. Auto exposure breathes slightly as the framing changes, then settles. No flash.
```
**Operator motion (video only):**
```
Filmed by one young man holding the camera in one hand: small tremors, step bob when he walks, small framing corrections, breath-level sway when standing still, no stabilizer, no gimbal, no smooth gliding. When he turns the camera from one person to the other it is a quick hand pan that overshoots a touch and settles back, with focus hunting for a moment before it locks on the new face. When he walks around someone, each footstep shows as a small dip and the horizon rolls a degree or two, then levels.
```
**Environment light:**
```
Soft overcast late-afternoon daylight around 6500K from a uniformly bright white-grey sky; no direct sun anywhere, no hard-edged shadows, only faint soft shadows under the furniture and curbs; the desk lamp and shop interiors add a small warm 2700K glow in the background only.
```
**Light on people:**
```
The people are lit only by the neutral overcast sky: soft, even, slightly cool light that wraps around their faces from above, the same from every direction, no sun patches, no hard shadows, no warm color cast on skin. Only faint soft shading under the chin, the brows and the hair line. Matte skin with subtle specular highlights, visible pores, no shine except a light natural T-zone sheen. Eyes carry a soft grey sky reflection as a broad dim catchlight, not a bright point. The warm shop-window and desk-lamp glow stays behind them and never colors their faces.
```
**Breeze:**
```
A light steady breeze blows along the street; hair, loose fabric, feathers and the magazine page edges drift with it, gently, never whipping.
```
**Performance (video only):**
```
Every person in frame is alive: irregular natural blinking, not evenly timed; eyes make tiny tracking movements and refocus; visible breathing; weight shifts; nobody holds a frozen pose. The gaze breaks from the lens briefly, then returns. Natural weight and momentum: the body settles after each stop or turn, heels take the weight on the curb step. She takes natural pauses as she speaks. All real motion, no robotic gestures, and people react to each other a beat late, like real people.
```
**Magazine (locked):**
```
An open large-format fashion magazine, matte off-white uncoated paper, about A3 when open, slightly curled and creased at the fold. BOTH PAGES ARE COMPLETELY BLANK: plain off-white paper, no text, no letters, no photo. The matte paper reflects the sky softly, with no glare hotspot.
```
**Laptop (locked):**
```
A silver MacBook, the thin aluminium wedge kind, open at about 110 degrees. Brushed silver anodised aluminium body, black island-style keyboard keys, a large glass trackpad, a thin dark screen bezel. The outside of the lid is completely blank with no logo, no badge and no lettering of any kind. The screen shows only a plain soft bright glow with no interface, no icons, no windows and no text, and picks up a soft diagonal band of pale sky glare.
```
**Avoid (every prompt ends with it):**
```
Avoid: airbrushed skin, studio light, direct sun, extra people, passers-by, a second kimono, a second blonde, any text on the magazine, any logo on the laptop, readable signs, borders, an older-looking LEADER, a laptop turned toward the camera, furniture placed anywhere other than where the diagram puts it, furniture that looks different from the furniture references, a different street from the location reference, a vertical frame.
```

## 4. Who the camera follows, and where everyone looks

**Camera follows the speaker.**
- **Default: the camera is on LEADER.** Whenever nobody is speaking, LEADER is the subject and the focus point.
- **Only while HERO is speaking** does the camera turn to HERO and hold on her. When her line ends, it drifts back to LEADER.
- **When LEADER speaks,** the camera guy walks in close to her until her face and upper body take up most of the frame (chest-up to tight close-up). Focus on her eyes. Let the camera catch her small, cute, proud facial movements: the corner of her mouth lifting, a little chin lift, a squint of pride, a quick eyebrow raise, a tiny head tilt. Show real skin up close: visible pores and the **fine creases at the outer corners of her eyes when she smiles.**

**Eyelines.**
- **While LEADER speaks:** HERO looks at LEADER, not at the camera.
- **While HERO speaks:** HERO looks back and forth between the camera and LEADER. LEADER looks at HERO.
- **Background crew:** mostly busy with each other, but now and then one of them glances over at whoever is speaking, holds for a beat, and goes back to the chat. Never all at once, and never straight into the lens.

**Paste into every video prompt (adapt the names to the shot):**
```
The camera follows whoever is speaking. While the woman with the black bob speaks, the camera walks in close until her face and upper body fill most of the frame, focused on her eyes, catching her small proud, cute facial movements and the fine creases at the outer corners of her eyes when she smiles. While the platinum blonde speaks, the camera turns to her; she looks back and forth between the camera and the bob-haired woman, who watches her. The listener always looks at the speaker. Now and then one of the people in the background glances over at whoever is speaking, then goes back to their chat; they never look into the lens.
```


## 4b. Camera moves — one per beat, all handheld

| Move | What it looks like | Used in |
|---|---|---|
| **Settle + tilt-up** | the frame settles on the group and tilts up a beat late as LEADER and HERO rise | S1 |
| **Rack + push-in** | focus racks from HERO's magazine to LEADER's eyes as she opens her mouth, then 2–3 small forward steps, a dip on each, waist-up to close-up | S2 |
| **Whip pan** | fast hand pan from LEADER to HERO, overshoots a touch and snaps back, a frame of motion blur, focus hunts then locks | S3a |
| **Arc** | a quarter circle along the curb to LEADER's left while HERO keeps talking; each step a dip, background sweeps, horizon rolls 2–3° and levels | S3b |
| **Hold with breath** | standing close, breathing and micro-corrections; a small reframe as LEADER turns her head | S4 |
| **Fast push past** | from behind LEADER, a quick push past her left shoulder until the screen fills the frame; a little wobble, 1° tilt | S5 |

## 5. Cast: constant motion signatures
These hold in every shot; the per-shot tables in section 6 add what each person does in that moment.

| Who | Look (from crop) | Fabric and hair motion (always on) |
|---|---|---|
| **LEADER**: black blunt bob with fringe | Off-white pinstripe yukata, wide sleeves, charcoal obi, white tabi, wooden zori | The bob swings as one block; the fringe lifts in the breeze. Wide sleeves sway with every arm move. The hem flicks at the ankles. The obi stays rigid. Short quick steps; a light wooden zori click. |
| **HERO**: platinum blonde, freckles | Fitted black scoop tank, white pleated barrel trousers, black Mary Janes. **Prop: the magazine** | Loose platinum strands drift and catch at her cheek. Page corners lift and flutter. Wide trouser legs ripple with each step. |
| **FEATHER** (bg): long wavy black hair, very slim | Lavender column dress in lilac ostrich feathers, lilac flats | Feathers quiver and ripple the whole time, kept soft. Long hair lifts in the breeze. |
| **SLICKED** (bg): brown hair, green eyes | White square-neck drop-waist midi, oatmeal knit tied over the shoulders, black flats | Her hair stays put, a contrast with the others. The knit's tied sleeves swing. The midi hem sways. |
| **SILVERMAN** (bg): shoulder-length silver hair | White crew tee, beige pleated chinos, black belt, black slides | Silver hair moves in the breeze. The tee ripples a little. |
| **Camera guy** (never seen) | none | Opens on the group at the sofa; after the cut, stands in front of the pair at the desk; stays on LEADER except while HERO speaks; pushes in on LEADER's line; arcs to her left during HERO's price line; ends BEHIND her, pushing past her left shoulder into the laptop. |

**Rules for every prompt:** each character's outfit belongs only to them; the magazine belongs only to HERO. Background people stay behind the pair and fall soft at f/2. Nobody in the background looks at the camera; they may glance at whoever is speaking (section 4).

## 6. Beats (16:9)

### S1 · Sofa, they rise · 0:00.0–0:00.5 · silent
- **Length:** 0.5 s = 12 frames at 24 fps. The only job: show the street, the crew and LEADER, and start the rise that the cut to S2 finishes.
- **First frame:** `keyframes/v10/S1a.jpg` · previz `blocking/previz/S1a.jpg`
- **Camera:** plate camera (the angle of `scene_empty.jpg`): on the sidewalk side, lens at about 1.8 m, 23 mm, tilted down about 8°, wide: building, sofa, table and desk all in frame. 16:9.
- **Frame, left to right:** SILVERMAN on the left armrest · HERO on the seat, closed magazine on her lap · FEATHER on the seat · SLICKED on the travertine table · LEADER at the sofa's right end, nearest the desk · desk with the blank laptop lid, lit lamp, empty chair at the right.
- **Action, frame by frame:**
  - 0.00–0.15 s: LEADER looks up at the lens, half-smile. HERO is mid-laugh. FEATHER's feathers ripple; SILVERMAN shifts on the armrest; SLICKED's knit sleeves swing in the breeze.
  - 0.15–0.50 s: LEADER puts her hands on her knees and starts to stand, eyes still on the lens; HERO closes the magazine and pushes up with her. The crew stays on the furniture and turns its heads toward the two of them.
- **Move:** settle + tilt-up. The frame lands on the group with a small bob and a 1° drift it corrects; as LEADER rises, the camera tilts up a beat late.
- **Focus:** on LEADER; the crew slightly soft.
- **Sound:** no line. Street room tone, light breeze; HERO's laugh may bleed under the cut (not a line).
- **Cut:** on the action, as LEADER's knees straighten → hard cut to S2 (they're already at the desk; her line starts on S2's first frame).
- **Video:** first frame S1a, no audio input, minimum length; keep only the first 12 frames.
- **Gate:** LEADER's face matches `cast/leader.jpg`; nobody stands behind the sofa or at the desk; the laptop lid stays blank and toward the camera; the street is `scene_empty.jpg`.

### S2 · LEADER's line, push-in · 0:00.5–0:02.7 · LEADER speaks
- **Keyframes:** first frame `keyframes/v10/S2a.jpg`; the push ends on `S2b.jpg`.
- **Frame order:** sofa with the crew, HERO, LEADER, desk. HERO's hip near LEADER, LEADER by the desk corner.
- **Line:** LEADER, eyes on the lens: "Still paying Higgsfield for this?" She starts on the first frame, no lead-in. HERO, magazine at her chest, looks at LEADER.
- **Move:** rack + push-in, ending chest-up on LEADER, HERO soft at the left edge, the sofa and crew soft behind.

### S3a · HERO: "3x cheaper" · 0:02.7–0:05.0 · HERO speaks
- **Keyframe:** `keyframes/v10/S3a.jpg`
- **Frame order:** HERO (left), LEADER (right, hand on HERO's shoulder), sofa and crew behind, desk centre-right.
- **Line:** HERO: "We made Higgsfield three x cheaper." She looks lens → LEADER → lens; LEADER watches her.
- **Move:** whip pan from LEADER to HERO on her first word.

### S3b · HERO: the prices · 0:05.0–0:09.5 · HERO speaks
- **Keyframe:** `keyframes/v10/S3b.jpg`
- **Frame order:** HERO (left-centre), LEADER (right-centre), desk with the blank lid at the right edge, sofa and crew soft at the left.
- **Line:** HERO: "I cost [$HF] on Higgsfield… and now [$TREG] on treg." Magazine open in her hands; eyes slide to LEADER on "treg". LEADER watches her, proud.
- **Move:** arc to LEADER's left, ending with LEADER's shoulder in the left foreground.

### S4 · LEADER turns her head and speaks · 0:09.5–0:11.0 · LEADER speaks
- **Keyframe:** `keyframes/v10/S4.jpg`
- **Frame order:** HERO (left-centre, soft), LEADER (right-centre, sharp); sofa crew soft at the far left; desk and chair empty, blank lid toward the camera.
- **Line:** LEADER turns her head over her LEFT shoulder to the lens, three-quarter face, sly proud half-smile: **line TBD (1.5 s)**.
- **Move:** hold with breath; small reframe as she turns.

### S5 · Push into the screen · 0:11.0–0:11.5 · silent
- **Keyframes:** first frame `keyframes/v10/S5a.jpg`; ends on `S5b.jpg`.
- **Frame:** from behind LEADER: back of her bob, the yukata, the obi bow centred as in her back photo, NO face. She holds the open laptop at chest height, screen toward her and the camera, glowing with a plain unreadable interface. HERO on the LEFT of the frame, from behind. The stone building of `scene_empty.jpg` behind, soft.
- **Move:** fast push past her left shoulder until the screen fills the frame. Generated as a normal-speed push and sped up in the edit to 0.5 s.
- **Hand-off:** last frame is the match cut to the screen recording.

## 6b. Video routing

| Clip | Beat | First frame | Generate | Use in edit | Audio |
|---|---|---|---|---|---|
| 1 | S1 | S1a | minimum length | first 0.5 s | none |
| 2 | S2 | S2a | 4 s | 2.2 s | `vo_leader_still-paying.mp3` |
| 3 | S3a | S3a | 4 s | 2.3 s | `vo_hero_3x-cheaper.mp3` |
| 4 | S3b | S3b | 5 s | 4.5 s | `vo_hero_price.mp3` |
| 5 | S4 | S4 | 4 s | 1.5 s | `vo_leader_s4.mp3` |
| 6 | S5 | S5a | minimum length | whole push, sped up to 0.5 s | none |

Each spoken clip gets its line as audio input so the lips sync; the line starts on the clip's first frame. The final mix uses the clean voice files, not the clip's own audio.

## 7. Props and artwork

**Artwork, drawn not generated:**

| File | What |
|---|---|
| `art/magazine_spread.png` | The magazine artwork: "3X" at 3× the size of "CHEAPER", "pay per call" bottom-left, the treg lock-up alone on the right page |
| `art/treg_logo.png` | The treg lock-up, transparent PNG |

Both are rendered in code with the real fonts, so the type is exact and cannot be misspelled. They are **composited in the edit**, corner-pin tracked onto the blank generated pages. Nothing readable is ever generated.

**treg brand spec** (read from treg.to's own page source, Nov 10):
- **Glyph:** `<svg viewBox="0 0 290 290"><rect width="140.5" height="140.5" rx="20"/><rect x="149.5" y="149.5" width="140.5" height="140.5" rx="20"/></svg>` — two rounded squares set diagonally, reversed out of a rounded badge.
- **Wordmark:** lowercase `treg` in **DM Mono**, weight 600. Lock-up: gap 9/28 of the badge, type 15/28 of the badge.
- **Other faces:** Geist Pixel (display), Suisse Intl / Inter (sans).
- **Slogan:** "pay per call" (short). Full tagline: "OpenRouter for agent tools and data, pay per call" — too long to read at phone size.


## 8. Gate 1 — keyframe check (every still, before any video)
- **Faces:** each face matches its cast file; LEADER looks about 25; no extra person.
- **Outfits:** exactly one kimono (LEADER, obi bow as in her back photo), one blonde (HERO), one magazine (HERO).
- **Location:** the same building, sidewalk, curb and crossing as `plates/scene_empty.jpg`; 16:9 landscape.
- **Positions:** the left-to-right order matches the beat; HERO on LEADER's right (frame-left facing camera, frame-left from behind); crew on the sofa/armrest/table; nobody at the desk.
- **Laptop:** screen toward the sofa; the camera sees only the blank lid, except over LEADER's shoulder in S5.
- **S5:** no face.

## 9. Gate 2 — 480p drafts
- Identity holds through the clip; no face or outfit swaps.
- Lips sync with the line; the line starts on the first frame.
- No silent stretch over 0.5 s survives the trim.
- Handheld reads as one man with a camera; each clip shows its one move.
- Furniture never moves; the laptop screen faces the sofa.

## 10. Cost
- Keyframes: 9 × $0.03 per full pass.
- Video at 480p, 3 tries per clip: about $8. Finals at 720p: about $6.
- Voice lines: under $0.01 each.

## 11. Still open
- LEADER's S4 line (1.5 s).
- [$HF] / [$TREG] for HERO's price line in S3b.
- Record `vo_hero_price.mp3` and `vo_leader_s4.mp3`; re-export the three existing takes into `audio/` in the repo.
