# UGC — locked asset library

These are the locked Stage 2 assets for the treg AIGC promo, a UGC-style ad claiming "3x cheaper than Higgsfield". They were locked on Nov 9, 2026.

To browse them, open `index.html`. For a machine-readable list, see `manifest.json`.

## Cast sheets (`sheets/`, 2752×1536)
| File | Role | Look |
|---|---|---|
| `leader_bob_kimono.jpg` | Leader | Black blunt bob with fringe. Off-white pinstripe yukata, charcoal obi, white tabi, wooden zori |
| `hero.jpg` | Hero | Platinum blonde, freckles. Black scoop tank, white pleated barrel trousers, black Mary Janes |
| `bg_feather_model.jpg` | Background | Very slim Japanese runway model, long wavy black hair. Lilac ostrich-feather column dress |
| `bg_slicked.jpg` | Background | Slicked-back brown hair. White square-neck drop-waist midi, oatmeal knit over the shoulders, black flats |
| `bg_silver_man.jpg` | Background | Japanese male model, shoulder-length silver hair. White tee only, beige chinos, black belt, black slides |

The sheets carry identity, hair, body and outfit only. Lighting for every shot comes from the locked blocks in the shot plan.

## Set plates (`plates/`, 1536×2752, 9:16)
| File | Status |
|---|---|
| `p1_master.png` | **Master geography.** The angled oak desk is on the sidewalk; the bare bouclé sofa and travertine table are on the zebra crossing |
| `p3_to_reroll.png` | Desk medium shot. To be re-rolled from p1 so it matches |
| `p2_unused.png` | Not used |

## Not here yet
- Plate pA: the desk-side curb, looking across the crossing
- The p3 re-roll
- The magazine prop ("3X CHEAPER"), which is blocked until real prices are in
- The voice takes, which were made in a separate session

## Notes
- All faces are AI-generated.
- Images were made with Gemini 3 Pro Image through treg.
- The plans and prompts are in the claude.ai Project "aigc" (`treg-ugc-*.md`).

## Prompt references (v4.0, Nov 10) — use these, never the sheets, never an old keyframe
Fixed order for every still call (12 images; reAPI allows 14). Each person = a FACE board (faces only, same person 3–4 times, age labelled) + an OUTFIT photo with the head cropped off, so the model can only take the face from the face board.

| # | File | Role | What it is |
|---|---|---|---|
| 1 | `cast/leader_face.jpg` | LEADER face | 3 sheet face views + the approved in-scene face, labelled "same young woman, about 25" |
| 2 | `cast/leader_body.jpg` | LEADER outfit | front + back, head cropped |
| 3 | `cast/hero_face.jpg` | HERO face | 3 sheet face views + the approved in-scene face |
| 4 | `cast/hero_body.jpg` | HERO outfit | front + back, head cropped |
| 5–6 | `cast/feather_face.jpg`, `cast/feather_body.jpg` | FEATHER | face board / headless outfit |
| 7–8 | `cast/slicked_face.jpg`, `cast/slicked_body.jpg` | SLICKED | face board / headless outfit |
| 9–10 | `cast/silverman_face.jpg`, `cast/silverman_body.jpg` | SILVERMAN | face board / headless outfit |
| 11 | `plates/P-C2.jpg` (or the beat's camera mark) | empty set | building, crossing, sofa, desk, laptop from that camera — fixes the furniture |
| 12 | `blocking/shots/<beat>.png` | blocking diagram | top view + projected camera view with every person and prop as a labelled shape |

The old single crops (`cast/leader.jpg` … `cast/silverman.jpg`, face + body in one file) are deleted; they let the model pick a face from the body panel.

## Blocking (`blocking/`)
- `set_layout.png` — top-view floor plan of the fixed set (sofa on the crossing perpendicular to the curb, desk 2 m along at 30°, laptop screen facing the sofa).
- `blocking_v7.png` — walking paths and camera marks C1–C4.
- `blocking/shots/S1a.png … S5b.png` — one diagram per beat; `blocking/shots/_all_shots.jpg` shows all nine.
- Source: `prompts/shotdiagrams.py`, `prompts/set_layout.py`, `prompts/blocking_v7.py`.

## Plates (`plates/`)
- `P-C2.jpg` — LOCKED empty set from camera mark C2 (Nov 10). P-C1, P-C3, P-C4 still to make from it.
- `p1_master.png` — old layout, reference for building/light only.

The 8-panel sheets in `sheets/` are the source of truth for review, but a video model reads a grid as eight people, so they must not go into a prompt.

Keyframe prompts live in `prompts/`.
