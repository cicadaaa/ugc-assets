# treg AIGC promo: hook shot plan v5.2, 0:00–0:13 (Nov 10, 2026)

**v5.0 is a clean rewrite.** Everything that was superseded (portrait 9:16 frame, furnished plates, per-camera plates, older prop crops, character sheets, earlier keyframes) is gone from this plan and from the repo. What is here is current.

**v5.2 (Nov 10, after keyframes v7): why people drifted off the marks, and the fix.**
Root causes found in v7 (S1b, S2a, S3b, S5a, S5b):
1. **The diagram's camera was too close.** C1/C2 sat 1.5 m from the curb, so in the diagram's camera view the two women filled the frame and the desk and sofa were cropped out. The model had no furniture in the diagram to anchor to, matched the people's *size* instead, and the only place that size fits in the wide empty plate is up on the sidewalk, close to the lens. Fix: C1/C2 moved to 2.6 m back; every diagram's camera view now shows the desk corner, the gap and the sofa edge together with the people.
2. **"Beside the desk" and "between sofa and desk" had no measure.** The model stretched the gap to 4–5 m and put people in the middle of it. Fix: the gap is written as **1.7 m, one sofa length**, and the marks are stated as contact: *HERO's right hip almost touches the desk's near corner; LEADER one step to her left.*
3. **Nothing said who may stand on the sidewalk.** Fix: *the camera man is the only person on the sidewalk; everyone else stands or sits on the zebra crossing below the curb.* The diagrams now draw an **L+H lane** (dashed red box, 1.7 m × 1.1 m, on the stripes between sofa and desk) and the people are only ever inside it.
4. **"Crew around the sofa" let them stand behind it.** Fix: *FEATHER on the seat, SILVERMAN on the road-end armrest, SLICKED on the travertine table; nobody stands behind the sofa.* The crew zone in the diagrams is now the sofa's own footprint.
5. **S5b had no street in frame**, so the model invented a room. Fix: the beat now keeps the stripes and road visible beyond the screen and says so.

**v5.1: checked against the top-view blocking, camera moves enriched.** Every mark in section 6 was read back against `blocking/paths_v8.png` and `blocking/set_layout.png` (positions, facings, HERO on LEADER's right, laptop screen toward the sofa, camera path C1→C2→C2+→C3→C4). New section 4b: a camera-move vocabulary and one distinct move per beat, all handheld.

**What changed in v5.0**
- **Frame is 16:9 landscape** (X's wide video format). The X100VI is held horizontally.
- **One location reference:** `plates/scene_empty.jpg`, the empty street with no furniture. The furniture is added from two look references and placed by the blocking diagram.
- **Asset lock in every beat:** each beat repeats the rule that the location, furniture look and positions come only from the references.
- **S5 rewritten:** the camera is BEHIND LEADER. We see the back of her bob and her shoulder, never her face, then push into the screen.

## 1. References — exactly these 9 images, in this order, in every keyframe call

Base: `https://raw.githubusercontent.com/cicadaaa/ugc-assets/main/`

| # | File | What it fixes |
|---|---|---|
| 1 | `cast/leader.jpg` | LEADER's face (left) and outfit (right, head and hair removed) |
| 2 | `cast/hero.jpg` | HERO |
| 3 | `cast/feather.jpg` | FEATHER |
| 4 | `cast/slicked.jpg` | SLICKED |
| 5 | `cast/silverman.jpg` | SILVERMAN |
| 6 | `plates/scene_empty.jpg` | the LOCATION: building, sidewalk, curb, zebra crossing. No furniture. Never changes. |
| 7 | `props/sofa_table.jpg` | what the sofa and travertine table look like (look only, not position) |
| 8 | `props/desk_set.jpg` | what the desk, laptop, lamp and chair look like (look only) |
| 9 | `blocking/shots/<beat>.png` | where every person AND every piece of furniture stands in this frame |

**Rules**
- Never pass anything else: no keyframe, no sheet, no older plate.
- The full prompt template is `prompts/keyframe_prompt.md`; per beat, only the THIS FRAME text and the diagram change.
- **Video calls** (Seedance 2.5) take only the approved keyframe as `first_frame`: `image_with_roles` can't mix first_frame with reference images. The video prompt describes people by their anchors (bob + kimono, platinum + tank).
- **Order of work:** keyframe → check against references and diagram (Gate 1) → animate → check (Gate 2) → finals. A still that fails is re-rolled, never fixed in video.

## 2. The set and the blocking (fixed for the whole hook)

- **Location** (`plates/scene_empty.jpg`): a granite sidewalk along an old carved-stone building with warm-lit shop windows; from the curb a wide zebra crossing runs straight out across the road, perpendicular to the sidewalk, stripes parallel to the curb.
- **Sofa:** on the zebra crossing, perpendicular to the curb, one end touching it, seat facing the desk. Travertine table at its road end.
- **Desk:** on the crossing about 2 m along the curb, at 30°, near end touching the curb. Laptop on the near end, **screen facing the sofa**, lid blank. Dome lamp on the far end; tan chair behind.
- **The L+H lane.** LEADER and HERO only ever stand or walk inside the 1.7 m gap between the sofa's curb end and the desk's near corner, on the white stripes, one step below the curb. They never step up onto the sidewalk and never pass the desk. At the desk their marks are contact marks: HERO's right hip almost touches the desk's near corner; LEADER is one step to HERO's left.
- **HERO is always on LEADER's right.**
- **Crew:** FEATHER kneels/bounces on the sofa seat, SILVERMAN sits on the road-end armrest and hops on and off it, SLICKED sits on the travertine table facing the sofa. They stay ON the furniture; nobody stands behind the sofa or wanders onto the crossing.
- **Camera man:** the ONLY person on the sidewalk. C1 and C2 are 2.6 m back from the curb (so the frame holds sofa, gap and desk together), C2+ and C3 at the curb edge, C4 on the crossing behind LEADER.

| File | What |
|---|---|
| `blocking/set_layout.png` | top view of the fixed set |
| `blocking/paths_v8.png` | walking paths and camera marks C1–C4 |
| `blocking/shots/S1a.png … S5b.png` | one diagram per beat: top view + the projected 16:9 camera view with every person and prop as a labelled shape |
| `blocking/shots/_all_shots.jpg` | all nine together |

**Consistency contract (what keeps every frame the same):**

| What | Comes from | Never from |
|---|---|---|
| Faces | `cast/<name>.jpg`, the one face on the left | a keyframe, a sheet, the prompt's imagination |
| Outfits | `cast/<name>.jpg`, the headless outfit on the right | — |
| The street | `plates/scene_empty.jpg` | any other plate |
| Furniture look | `props/sofa_table.jpg`, `props/desk_set.jpg` | — |
| Furniture position | the beat's `blocking/shots/<beat>.png` | the model's own layout |
| People position and facing | the beat's diagram, drawn from `paths_v8.png` | — |
| Camera position, height, direction | the beat's diagram (red square + wedge) | — |

If any of these is wrong in a still, the still is re-rolled; nothing is "fixed in video".

**Locked location text (paste into video prompts):**
```
EXT. CITY STREET CROSSWALK – LATE AFTERNOON. A wide granite-slab sidewalk along an old carved-stone building with fluted columns and tall dark shop windows with warm lamps glowing inside, no signs, no lettering. From the curb a wide zebra crossing runs straight out across the road, perpendicular to the sidewalk, its white stripes parallel to the curb, on worn, slightly cracked asphalt. On the crossing, right against the curb: a cream bouclé sofa turned perpendicular to the curb, seat facing the desk, an empty round travertine table at its far end; two metres along, a light oak desk at a 30-degree angle with a silver laptop on its near end, screen facing the sofa, and a black dome lamp on its far end, a tan leather chair behind it. Nothing else.
```

## 3. Locked blocks (paste word for word)

**Camera:**
```
Shot on a Fujifilm X100VI with its fixed 23mm f/2 lens (35mm equivalent), Eterna film simulation, held horizontally, 16:9 landscape frame, handheld by a young man at his chest height. Eterna look: low saturation, soft gentle contrast, lifted shadows, smooth highlight roll-off, muted cyan-green in the shade. Shallow depth of field at f/2 with a softly blurred street behind the subject, slight glow on highlights when close up, fine film-like grain. Auto exposure breathes slightly as the framing changes, then settles. No flash.
```
**Operator motion (video only):**
```
Filmed by one young man holding the camera in one hand: small tremors, step bob when he walks, small framing corrections, breath-level sway when standing still, no stabilizer, no gimbal, no smooth gliding. When he walks backward his steps are shorter and a little uneven: a soft up-and-down bob on each step, a slight side-to-side sway and a tiny horizon tilt that he keeps correcting. When he turns the camera from one person to the other it is a quick hand pan that overshoots a touch and settles back, with focus hunting for a moment before it locks on the new face. When he walks around someone, each footstep shows as a small dip and the horizon rolls a degree or two, then levels.
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

## 4b. Camera moves — handheld vocabulary, one distinct move per beat

Every move is by the same young man holding the X100VI in one or two hands: no gimbal, no slider, no drone. Each beat uses a different move so the 13 seconds never feel static, and each move is motivated by what the people do.

| Move | What it looks like | Used in |
|---|---|---|
| **Arrive-and-settle** | the last two steps of a walk: bob, bob, a small overshoot of the frame, then it settles with breath sway | S1a |
| **Walking backward** | short uneven steps, soft vertical bob on each, slight side sway, horizon tilts 1–3° and is corrected; one glance-back jolt | S1b |
| **Tilt-up on the rise** | as LEADER stands, the camera tilts up with her, a beat late, so her head briefly clips the top of frame and he corrects | S1b (start) |
| **Rack focus** | focus hunts from one person to the other and settles; the out-of-focus one goes soft | S2a (HERO → LEADER as she starts talking), S5a (shoulder → screen) |
| **Push-in** | 2–3 small forward steps, a dip on each, framing tightens from waist-up to chest-up/close-up | S2b |
| **Whip pan** | a fast hand pan that overshoots a touch and snaps back; a frame of motion blur | S3a (LEADER → HERO) |
| **Arc** | walking a quarter circle around someone; each step a dip, the background sweeps past, horizon rolls and levels | S3b (C2 → C3) |
| **Hold with breath** | standing close, only breathing and micro-corrections; a small reframe when the subject moves | S4 |
| **Step-in behind** | a step and a half round behind someone: dip, slight roll, the back of their head enters frame large | S5a |
| **Slow push past** | pushing forward past a shoulder until the thing beyond fills the frame; a little wobble, 1° tilt | S5b |
| **Low-angle beat** (optional) | for one moment in S1b the camera dips to waist height on a step and comes back up, so the stripes rush in the lower frame | S1b (one step) |

**Rule:** moves never cross the blocking. The camera stays on the marks in `paths_v8.png`; the moves happen on the way between marks or in place.

## 5. Cast: constant motion signatures
These hold in every shot; the per-shot tables in section 6 add what each person does in that moment.

| Who | Look (from crop) | Fabric and hair motion (always on) |
|---|---|---|
| **LEADER**: black blunt bob with fringe | Off-white pinstripe yukata, wide sleeves, charcoal obi, white tabi, wooden zori | The bob swings as one block; the fringe lifts in the breeze. Wide sleeves sway with every arm move. The hem flicks at the ankles. The obi stays rigid. Short quick steps; a light wooden zori click. |
| **HERO**: platinum blonde, freckles | Fitted black scoop tank, white pleated barrel trousers, black Mary Janes. **Prop: the magazine** | Loose platinum strands drift and catch at her cheek. Page corners lift and flutter. Wide trouser legs ripple with each step. |
| **FEATHER** (bg): long wavy black hair, very slim | Lavender column dress in lilac ostrich feathers, lilac flats | Feathers quiver and ripple the whole time, kept soft. Long hair lifts in the breeze. |
| **SLICKED** (bg): brown hair, green eyes | White square-neck drop-waist midi, oatmeal knit tied over the shoulders, black flats | Her hair stays put, a contrast with the others. The knit's tied sleeves swing. The midi hem sways. |
| **SILVERMAN** (bg): shoulder-length silver hair | White crew tee, beige pleated chinos, black belt, black slides | Silver hair moves in the breeze. The tee ripples a little. |
| **Camera guy** (never seen) | none | Arrives on the sidewalk facing the sofa; walks backward ahead of the pair to the desk; stays on LEADER except while HERO speaks; pushes in on LEADER's line; moves to her left during HERO's lines; ends BEHIND her, over her left shoulder, pushing into the laptop. |

**Rules for every prompt:** each character's outfit belongs only to them; the magazine belongs only to HERO. Background people stay behind the pair and fall soft at f/2. Nobody in the background looks at the camera; they may glance at whoever is speaking (section 4).

## 6. Beats (each beat = one keyframe; 16:9)

### S1a · Sofa, camera arrives · 0:00–0:00.8
- **Diagram (image 9):** `blocking/shots/S1a.png`
- **Camera:** C1 — wide, on the sidewalk 2.6 m back from the curb, sofa and desk both in frame. 16:9 landscape.
- **Beat:** LEADER sits at the curb end of the sofa; HERO right beside her on her right (road side), magazine closed on her lap. FEATHER bounces on the far seat; SILVERMAN sits on the road-end armrest and hops on it; SLICKED sits on the travertine table facing the sofa. Nobody stands behind the sofa. LEADER glances up at the lens. The desk is 1.7 m along the curb at the right of frame, in the same shot as the sofa.
- **Handheld:** Camera man arriving: last two steps, a small bob, settles; frame drifts a degree and corrects.
- **Move:** arrive-and-settle. He walks the last two steps toward the sofa, the frame bobs twice, overshoots slightly past LEADER and settles on the group. Rack: the frame is on the whole group; focus sits on LEADER.
- **Asset lock (paste into this beat's prompt):** ASSET LOCK: the location is image 6 and it never changes. The sofa and table look exactly like image 7, the desk, laptop, lamp and chair look exactly like image 8, and every one of them stands exactly where image 9 puts it. Do not move, add, restyle or reinvent any furniture, building, curb or stripe. Every person's face and outfit come only from images 1-5.

### S1b · They stand and walk; camera backs up · 0:00.8–0:02
- **Diagram (image 9):** `blocking/shots/S1b.png`
- **Camera:** C1→C2 — walking backward along the sidewalk. 16:9 landscape.
- **Beat:** LEADER and HERO are up and walking along the curb toward the desk, HERO glued to LEADER's right, magazine open over her face. They are inside the 1.7 m lane between sofa and desk, on the white stripes, one step below the curb, never on the sidewalk; the sofa is one step behind them and the desk one step ahead, both in frame. LEADER's eyes on the lens.
- **Handheld:** Short uneven backward steps, a soft bob on each, slight sway, horizon tilts ~2° and is corrected; one glance over his shoulder (small jolt) before the desk.
- **Move:** tilt-up on the rise, then walking backward. As LEADER stands the camera tilts up a beat late, her head clips the top edge and he corrects; then he backs up along the sidewalk, short uneven steps, soft bob, 1–3° tilt corrected each step; one step dips to waist height and comes back up; one glance-back jolt before the desk.
- **Asset lock (paste into this beat's prompt):** ASSET LOCK: the location is image 6 and it never changes. The sofa and table look exactly like image 7, the desk, laptop, lamp and chair look exactly like image 8, and every one of them stands exactly where image 9 puts it. Do not move, add, restyle or reinvent any furniture, building, curb or stripe. Every person's face and outfit come only from images 1-5.

### S2a · At the desk; LEADER starts her line · 0:02–0:03
- **Diagram (image 9):** `blocking/shots/S2a.png`
- **Camera:** C2 — medium two-shot, on the sidewalk 2.6 m back from the curb, sofa edge and desk corner both in frame. 16:9 landscape.
- **Beat:** They stop at the desk's near (laptop) end: HERO's right hip almost touches the desk corner, LEADER one step to her left; both on the stripes below the curb, the sofa one sofa-length behind them in frame. LEADER faces the lens and starts: "Still paying Higgsfield for this?" HERO, magazine at her chest, looks at LEADER. Crew soft on the sofa behind.
- **Handheld:** Standing: breath sway, small framing corrections.
- **Move:** stop and rack focus. He stops at C2 with a small settle; focus is briefly on HERO's magazine and racks to LEADER's eyes as she opens her mouth.
- **Asset lock (paste into this beat's prompt):** ASSET LOCK: the location is image 6 and it never changes. The sofa and table look exactly like image 7, the desk, laptop, lamp and chair look exactly like image 8, and every one of them stands exactly where image 9 puts it. Do not move, add, restyle or reinvent any furniture, building, curb or stripe. Every person's face and outfit come only from images 1-5.

### S2b · Push-in on LEADER · 0:03–0:04.5
- **Diagram (image 9):** `blocking/shots/S2b.png`
- **Camera:** C2+ — close-up, 0.8 m. 16:9 landscape.
- **Beat:** Face and upper body fill the frame, focus on her eyes: chin lift, mouth corner curling, a proud squint. HERO a soft shape at the frame edge watching her. Sofa and stripes very soft behind.
- **Handheld:** Two or three small forward steps, a dip on each; on the hold, breathing; focus breathes then settles on her eyes.
- **Move:** push-in. Two or three small forward steps, a dip on each, from waist-up to chest-up to a close-up; on the hold, breath sway; focus breathes and settles on her eyes.
- **Asset lock (paste into this beat's prompt):** ASSET LOCK: the location is image 6 and it never changes. The sofa and table look exactly like image 7, the desk, laptop, lamp and chair look exactly like image 8, and every one of them stands exactly where image 9 puts it. Do not move, add, restyle or reinvent any furniture, building, curb or stripe. Every person's face and outfit come only from images 1-5.

### S3a · HERO speaks; camera turns to her · 0:04.5–0:07
- **Diagram (image 9):** `blocking/shots/S3a.png`
- **Camera:** C2 — medium on HERO. 16:9 landscape.
- **Beat:** HERO: "We made Higgsfield 3x cheaper… I cost [$HF] on Higgsfield, and now [$TREG] on treg." HERO looks lens → LEADER → lens; LEADER at the frame edge watches her, hand on her shoulder. Same marks as S2a: same street, same sofa behind, same desk beside HERO.
- **Handheld:** Quick hand pan from LEADER to HERO, overshoots a touch and settles; focus hunts a beat, then locks on HERO.
- **Move:** whip pan. On HERO's first word the camera whips from LEADER to HERO, overshoots a touch, snaps back; focus hunts a beat, locks on HERO.
- **Asset lock (paste into this beat's prompt):** ASSET LOCK: the location is image 6 and it never changes. The sofa and table look exactly like image 7, the desk, laptop, lamp and chair look exactly like image 8, and every one of them stands exactly where image 9 puts it. Do not move, add, restyle or reinvent any furniture, building, curb or stripe. Every person's face and outfit come only from images 1-5.

### S3b · Camera walks round to LEADER's left · 0:07–0:10
- **Diagram (image 9):** `blocking/shots/S3b.png`
- **Camera:** C2→C3 — arriving on LEADER's left, 1 m. 16:9 landscape.
- **Beat:** Still HERO's price line; nobody has moved: HERO still at the desk corner, LEADER one step to her left, both on the stripes. The camera man walks along the curb edge to LEADER's LEFT (sofa side), 1 m from her. Foreground: LEADER's left shoulder, sleeve and the back of her bob, soft. HERO talking beyond her, the desk and laptop right behind HERO.
- **Handheld:** Each step a visible dip; the horizon rolls 2–3° and levels as he stops.
- **Move:** arc. Still on HERO's line he walks a quarter circle along the curb to LEADER's left; each step a dip, the sofa and building sweep across the background, the horizon rolls 2–3° and levels as he stops; LEADER's shoulder grows into the left foreground.
- **Asset lock (paste into this beat's prompt):** ASSET LOCK: the location is image 6 and it never changes. The sofa and table look exactly like image 7, the desk, laptop, lamp and chair look exactly like image 8, and every one of them stands exactly where image 9 puts it. Do not move, add, restyle or reinvent any furniture, building, curb or stripe. Every person's face and outfit come only from images 1-5.

### S4 · LEADER turns her head and speaks side-on · 0:10–0:11.5
- **Diagram (image 9):** `blocking/shots/S4.png`
- **Camera:** C3 — side-on close-up, 1 m. 16:9 landscape.
- **Beat:** LEADER keeps her body toward the desk and turns her head over her LEFT shoulder to the camera: three-quarter profile, chest-up, sly proud half-smile. Line **TBD**. HERO behind her on the right, soft, smiling at her.
- **Handheld:** Standing still: breath sway; a small reframe as she turns her head.
- **Move:** hold with breath. Standing 1 m away, only breathing and micro-corrections; a small reframe as her head turns to him.
- **Asset lock (paste into this beat's prompt):** ASSET LOCK: the location is image 6 and it never changes. The sofa and table look exactly like image 7, the desk, laptop, lamp and chair look exactly like image 8, and every one of them stands exactly where image 9 puts it. Do not move, add, restyle or reinvent any furniture, building, curb or stripe. Every person's face and outfit come only from images 1-5.

### S5a · BEHIND LEADER: over her left shoulder onto the laptop · 0:11.5–0:12.5
- **Diagram (image 9):** `blocking/shots/S5a.png`
- **Camera:** C4 — behind her, lens at her shoulder height. 16:9 landscape.
- **Beat:** LEADER takes half a step to the laptop and stands at the desk's near edge facing the screen, close enough to touch the keyboard. **The screen faces the sofa, so she stands on the sofa side of the desk with her BACK to the camera.** The sofa is 1.7 m behind her, at the left edge of frame. The camera man steps in BEHIND her, slightly to her left. **Her face is NOT visible.** What the camera sees: the back of her black bob and the edge of her left ear, her left shoulder and the pinstripe kimono sleeve, large and soft at the right edge of the frame; past her shoulder, the open laptop on the desk with its plain glowing screen, sharp in the middle of the frame. HERO on LEADER's right, seen from behind three-quarter, leaning toward the screen. The laptop never moves.
- **Handheld:** A step and a half in behind her: a dip, a slight roll; focus racks from her shoulder to the screen.
- **Move:** step-in behind + rack focus. A step and a half round behind her onto the crossing: a dip, a slight roll; the back of her bob enters frame large on the right; focus racks from her shoulder to the screen.
- **Asset lock (paste into this beat's prompt):** ASSET LOCK: the location is image 6 and it never changes. The sofa and table look exactly like image 7, the desk, laptop, lamp and chair look exactly like image 8, and every one of them stands exactly where image 9 puts it. Do not move, add, restyle or reinvent any furniture, building, curb or stripe. Every person's face and outfit come only from images 1-5.

### S5b · Push past her shoulder into the screen · 0:12.5–0:13
- **Diagram (image 9):** `blocking/shots/S5b.png`
- **Camera:** C4+ — screen fills the frame. 16:9 landscape.
- **Beat:** From behind her, the camera pushes forward past her left shoulder until the plain glowing screen fills most of the frame. The back of her bob and her shoulder slide out of frame on the right, soft. **Still no face.** Beyond and around the screen, out of focus: the oak desk top, the white stripes and the grey road of the same street; this is still outdoors on the crossing. No UI, no logo. Hand-off frame for the match cut to the screen recording.
- **Handheld:** A slow handheld push with a little wobble; a one-degree tilt.
- **Move:** slow push past. He pushes forward past her left shoulder; her bob and shoulder slide out on the right; the screen fills the frame; a little wobble, a 1° tilt; the last frame is the hand-off.
- **Asset lock (paste into this beat's prompt):** ASSET LOCK: the location is image 6 and it never changes. The sofa and table look exactly like image 7, the desk, laptop, lamp and chair look exactly like image 8, and every one of them stands exactly where image 9 puts it. Do not move, add, restyle or reinvent any furniture, building, curb or stripe. Every person's face and outfit come only from images 1-5.

**Video routing:**

| Clip | Beats | First frame | Length |
|---|---|---|---|
| 1 | S1a → S1b | approved S1a | 5 s |
| 2 | S2a → S2b | approved S2a | 4 s |
| 3 | S3a | approved S3a | 4 s |
| 4 | S3b | approved S3b | 4 s |
| 5 | S4 | approved S4 | 3 s |
| 6 | S5a → S5b | approved S5a | 4 s |

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
- **Faces:** each face matches its cast file; LEADER looks about 25; no extra person; no glasses.
- **Outfits:** exactly one kimono (LEADER), one blonde (HERO), one magazine (HERO).
- **Location:** same building, sidewalk, curb and crossing as `plates/scene_empty.jpg`; the frame is 16:9 landscape.
- **Furniture look:** the sofa, table, desk, laptop, lamp and chair look like `props/`.
- **Positions:** every person and every piece of furniture is where the beat's diagram puts it. LEADER and HERO are inside the lane (on the stripes, between sofa and desk, below the curb), never on the sidewalk; at the desk HERO touches the desk corner. Sofa-to-desk gap reads as one sofa length. Crew is ON the sofa/armrest/table. HERO is on LEADER's right. The laptop screen faces the sofa.
- **S5a/S5b:** LEADER seen from behind only (bob, ear edge, shoulder). No face.
- **Light:** soft overcast, neutral faces, no sun.

## 9. Gate 2 — 480p drafts
- Identity holds through the clip; no face or outfit swaps.
- Handheld reads as one man with a camera, never a glide; each clip shows its one move from section 4b (settle, tilt-up + walk-back, rack, push-in, whip pan, arc, hold, step-in, push past).
- Every visible person moves.
- Lip sync stays inside the slot.
- Furniture never moves.

## 10. Cost
- Keyframes: 9 × $0.03 = $0.27 per full pass.
- Video at 480p, 3 tries each: ≈ $8. Finals at 720p: ≈ $6.

## 11. Still open
- LEADER's side-on line in S4.
- [$HF] / [$TREG] for S3a.
- Voice files to `audio/` in the repo for Seedance `audio_urls`.
