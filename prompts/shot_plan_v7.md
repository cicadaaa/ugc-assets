# treg AIGC promo: hook shot plan v7 — one take, layered (Nov 10, 2026)

**v7 replaces the cut version (v6).** What changed, and why:
- **One take.** There is one camera man and he never cuts. The hook is three clips of about 5 s; each is a single continuous handheld take, and each clip starts on the exact last frame of the one before, so they join into one unbroken shot. Chia stitches them.
- **The camera man walks backward** in front of LEADER and HERO, **never more than 1 m from them** (0.6–1.0 m). Framing changes only because he steps closer, steps back or turns the camera to the other person. No post zoom, no post shake: all movement is generated in camera.
- **Two layers.** The background crew is generated on its own (locked camera, exactly three people), LEADER and HERO are generated on their own (green screen), and the two are composited. The crew can no longer change, multiply or vanish.
- **Small mouths.** Lips barely part when speaking; relaxed jaw; no wide vowels.
- **More keyframes:** 11 (K01–K11), about one per second.

## 0. The take

| Clip | Time | Keyframes | Who speaks | Line | Camera man (always ≤ 1 m) |
|---|---|---|---|---|---|
| **A** | 0–5 s | K01 → K05 | LEADER, then HERO | 0.5 s silent, then "Still paying Higgsfield for this?" · "We made Higgsfield three x cheaper." | walks backward; lets LEADER close in to 0.6 m on her line; turns the camera to HERO on hers; steps back to 0.9 m as they slow down |
| **B** | 5–10 s | K05 → K08 | HERO | "I cost nine forty-five on Higgsfield… and now a dollar eighty on treg." | they stand at the desk; camera on HERO at 0.8 m, then he sidesteps round to LEADER's left, staying 0.8 m away |
| **C** | 10–13 s (+ hold) | K08 → K09 → K10 → K11 | LEADER | "Told you. It's pay per call." | 0.7 m on LEADER as she turns her head; she lifts the laptop while still speaking; he steps behind her left shoulder and pushes to the screen, landing at most 0.5 s after her last word |

Rules: no silent stretch over 0.5 s; gaps between lines 0.2 s at most; lines are never sped up past ±8%. Clip C is generated at 4–5 s; what follows the screen landing is a hold to trim or cover with the screen recording.

## 1. Layers

| Layer | What | How it is made | File |
|---|---|---|---|
| **BG** | the street, the sofa, the table and exactly three crew (SILVERMAN on the armrest, FEATHER on the seat, SLICKED on the table), chatting, never looking at the lens | one still from `blocking/previz/BG_crew.jpg` + cast + `props/sofa_table.jpg` + `plates/scene_empty.jpg`; animated ONCE as a 10 s locked-camera clip | `layers/bg_crew.jpg` |
| **DESK** | oak desk, laptop (blank lid toward camera), lit lamp | a still on green, cut out; slides in at the lower right as they reach the desk | `layers/desk_green.jpg` |
| **FG** | LEADER and HERO, chest-up, on chroma green | stills from `cast/leader.jpg` + `cast/hero.jpg` only; animated with Seedance (first + last frame, the lines as audio), handheld in camera | `layers/fg/K01…K09.jpg` |
| **Composite** | FG over DESK over BG; BG defocused (f/2 look), fine grain over everything | `prompts/comp.py` | `keyframes/v11/K01…K11.jpg` |

**Keeping the layers locked together while the camera moves.** The handheld movement lives in the FG clip. Small tracking marks are added to the green before animation; their motion is tracked frame by frame and the same shift and scale are applied to BG and DESK, so the background moves with the camera. BG also shrinks slowly through clip A (the camera is walking away from the sofa) and slides sideways in clip B (he steps to LEADER's left).
- **This is the part that is not proven yet.** If the marks don't track cleanly, the fallback is single-layer generation from the composite keyframes (first + last frame per clip), with the crew described as "exactly three seated friends".
- Clip C is single-layer from the start: first frame = composite K08, last frame = K11. The crew is only visible in its first second.

## 2. The set (fixed)

- **Location:** `plates/scene_empty.jpg`, the only street reference.
- **Sofa** at the far curb by the building, travertine table beside it; **desk** on the crossing nearer the camera.
- **Path:** LEADER and HERO start standing just in front of the sofa and stroll to the desk (about 2 m) during clip A, then stand at the desk. HERO is always on LEADER's right: frame-left when they face the camera.
- **Crew** stays on the sofa, armrest and table for the whole take.
- **Laptop screen always faces the sofa:** blank lid toward the camera until LEADER lifts it in clip C, screen toward her.
- **Camera man:** in front of the pair, walking backward toward the desk, 0.6–1.0 m from them, lens at their eye height. He ends behind LEADER's left shoulder.

## 3. Locked blocks (paste word for word)

**Camera:**
```
Shot on a Fujifilm X100VI with its fixed 23mm f/2 lens (35mm equivalent), Eterna film simulation, held horizontally, 16:9 landscape frame, handheld by a young man at his chest height. Eterna look: low saturation, soft gentle contrast, lifted shadows, smooth highlight roll-off, muted cyan-green in the shade. Shallow depth of field at f/2 with a softly blurred street behind the subject, slight glow on highlights when close up, fine film-like grain. Auto exposure breathes slightly as the framing changes, then settles. No flash.
```
**Operator motion (video only):**
```
Filmed by one young man holding the camera in one hand: small tremors, step bob when he walks, small framing corrections, breath-level sway when standing still, no stabilizer, no gimbal, no smooth gliding. He walks backward for most of the take: short, slightly uneven steps, a soft up-and-down bob on each, a slight side-to-side sway and a tiny horizon tilt that he keeps correcting. He is never more than one metre from the two women. When he turns the camera from one person to the other it is a quick hand pan that overshoots a touch and settles back, with focus hunting for a moment before it locks on the new face. When he walks around someone, each footstep shows as a small dip and the horizon rolls a degree or two, then levels.
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
- **When LEADER speaks,** the camera guy lets her come closer (0.6 m) until her face and upper body take up most of the frame. Focus on her eyes. Let the camera catch her small, cute, proud facial movements: the corner of her mouth lifting, a little chin lift, a squint of pride, a quick eyebrow raise, a tiny head tilt. Show real skin up close: visible pores and the **fine creases at the outer corners of her eyes when she smiles.**

**Eyelines.**
- **While LEADER speaks:** HERO looks at LEADER, not at the camera.
- **While HERO speaks:** HERO looks back and forth between the camera and LEADER. LEADER looks at HERO.
- **Background crew:** mostly busy with each other, but now and then one of them glances over at whoever is speaking, holds for a beat, and goes back to the chat. Never all at once, and never straight into the lens.

**Paste into every video prompt (adapt the names to the shot):**
```
The camera follows whoever is speaking. While the woman with the black bob speaks, the camera walks in close until her face and upper body fill most of the frame, focused on her eyes, catching her small proud, cute facial movements and the fine creases at the outer corners of her eyes when she smiles. While the platinum blonde speaks, the camera turns to her; she looks back and forth between the camera and the bob-haired woman, who watches her. The listener always looks at the speaker. Now and then one of the people in the background glances over at whoever is speaking, then goes back to their chat; they never look into the lens.
```

**Mouths (paste into every video prompt with speech):**
```
When she speaks her mouth moves only a little: lips part a few millimetres, relaxed jaw, soft small articulation like someone talking quietly to a friend, no wide-open vowels, no exaggerated lip shapes, no teeth-baring. Expression comes from the eyes, brows and the corners of the mouth. When she is not speaking her lips rest closed.
```

## 5. Cast: constant motion signatures
These hold in every shot; the per-shot tables in section 6 add what each person does in that moment.

| Who | Look (from crop) | Fabric and hair motion (always on) |
|---|---|---|
| **LEADER**: black blunt bob with fringe | Off-white pinstripe yukata, wide sleeves, charcoal obi, white tabi, wooden zori | The bob swings as one block; the fringe lifts in the breeze. Wide sleeves sway with every arm move. The hem flicks at the ankles. The obi stays rigid. Short quick steps; a light wooden zori click. |
| **HERO**: platinum blonde, freckles | Fitted black scoop tank, white pleated barrel trousers, black Mary Janes. **Prop: the magazine** | Loose platinum strands drift and catch at her cheek. Page corners lift and flutter. Wide trouser legs ripple with each step. |
| **FEATHER** (bg): long wavy black hair, very slim | Lavender column dress in lilac ostrich feathers, lilac flats | Feathers quiver and ripple the whole time, kept soft. Long hair lifts in the breeze. |
| **SLICKED** (bg): brown hair, green eyes | White square-neck drop-waist midi, oatmeal knit tied over the shoulders, black flats | Her hair stays put, a contrast with the others. The knit's tied sleeves swing. The midi hem sways. |
| **SILVERMAN** (bg): shoulder-length silver hair | White crew tee, beige pleated chinos, black belt, black slides | Silver hair moves in the breeze. The tee ripples a little. |
| **Camera guy** (never seen) | none | One take, no cuts. Walks backward ahead of the pair from the sofa to the desk, 0.6–1.0 m from them; turns the camera to whoever speaks; sidesteps to LEADER's left during HERO's price line; ends behind LEADER's left shoulder, pushing to the laptop screen. |

**Rules for every prompt:** each character's outfit belongs only to them; the magazine belongs only to HERO. Background people stay behind the pair and fall soft at f/2. Nobody in the background looks at the camera; they may glance at whoever is speaking (section 4).

## 6. Keyframes (16:9; `keyframes/v11/`)

| # | Time | Distance | Frame |
|---|---|---|---|
| K01 | 0.0 s | 1.0 m | Both chest-up, first step toward the camera. LEADER eyes on the lens, closed-lip half-smile; HERO laughing softly, closed magazine at her chest. Crew on the sofa behind. |
| K02 | 1.2 s | 0.6 m | Camera on LEADER, collarbone up, mid-line, lips barely parted, brow up. HERO at the left edge, soft, looking at her. |
| K03 | 2.2 s | 0.6 m | LEADER after her line: sly closed-lip smirk, proud squint. HERO grins at her. |
| K04 | 3.0 s | 0.7 m | Camera turned to HERO, chest-up, speaking, magazine open. LEADER at the right edge watching. |
| K05 | 4.8 s | 0.9 m | Stepped back: both in frame, slowing to a stop. HERO grinning, LEADER's hand on her shoulder. **Last frame of A = first frame of B.** |
| K06 | 6.0 s | 0.8 m | At the desk. Camera on HERO: "nine forty-five", small counting gesture. LEADER's shoulder at the right. |
| K07 | 8.0 s | 0.8 m | Camera has moved to LEADER's left: LEADER nearer, three-quarter, watching HERO; HERO beyond, "a dollar eighty". |
| K08 | 9.8 s | 0.8 m | HERO done, eyes slide to LEADER; LEADER about to turn. **Last frame of B = first frame of C.** |
| K09 | 10.4 s | 0.7 m | LEADER's head turned over her left shoulder to the lens: "Told you." HERO soft, smiling. |
| K10 | 12.0 s | 0.7 m | From behind her left shoulder: back of her bob, obi bow, she lifts the laptop, screen toward her. No face. |
| K11 | 13.0 s | 0.4 m | The screen fills the frame. Hand-off to the screen recording. |

K01–K09 are composites (FG + DESK + BG). K10 and K11 are single-layer stills on `scene_empty.jpg`.

## 6b. Video routing (Seedance 2.5 via reAPI, 480p drafts first)

| Job | Layer | First frame | Last frame | Length | Audio |
|---|---|---|---|---|---|
| BG | crew plate, locked camera | `layers/bg_crew.jpg` | — | 10 s | none |
| A | FG on green + marks | `layers/fg/K01` | `layers/fg/K05` | 5 s | LEADER line + HERO "3x" line in one file |
| B | FG on green + marks | last frame of A | `layers/fg/K08` | 5 s | `vo_hero_price.mp3` |
| C | single layer | composite K08 | K11 | 4–5 s | `vo_leader_told-you.mp3` |

Order: **test first** — BG plate + clip A only (about $1.80 at 480p), composite, check that the layers hold together. Then B and C.

**Video prompt rules for A and B:** one continuous handheld take, no cuts; the camera man walks backward ahead of them, never further than one metre; he reframes only by stepping closer or back and by turning the camera from one woman to the other; background stays flat chroma green with the marks; mouths small (block above).

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


## 8. Gate 1 — keyframes
- Faces and outfits match `cast/`; HERO frame-left, LEADER frame-right (facing camera).
- Chest-up or closer in every frame: the camera is never more than 1 m away.
- BG has exactly three crew, all seated; the street is `scene_empty.jpg`.
- Mouths: closed or barely parted.
- K10/K11: no face.

## 9. Gate 2 — 480p drafts
- Each clip is one take: no cut, no jump in framing.
- The first frame of B equals the last frame of A; the first frame of C equals the last frame of B.
- Handheld movement is in camera: step bob while he walks backward, reframing by stepping and turning.
- Crew: three people, same seats, from start to end.
- Lip movement small; lines start where the timeline says.
- Composite: no green fringe on hair, BG moves with the camera.

## 10. Cost
- Keyframes pass: 12 stills × $0.03 = $0.36.
- 480p: BG 10 s + A 5 s + B 5 s + C 5 s = 25 s × $0.12 ≈ $3 per pass. 720p finals ≈ $6.70.

## 11. Still open
- Run the layer test (BG plate + clip A).
- The desk is barely in frame at this distance (only the laptop lid and lamp at the lower right); decide whether that is enough.
