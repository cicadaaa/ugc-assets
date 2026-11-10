# UGC — reference assets (v5.0, Nov 10, 2026) — 16:9 landscape

Only the files below exist. Every image call uses them through these public links:
`https://raw.githubusercontent.com/cicadaaa/ugc-assets/main/<path>`

## Pass to every keyframe call, in this order (9 images)

| # | File | Role | Unique anchor |
|---|---|---|---|
| 1 | `cast/leader.jpg` | LEADER | the only black blunt bob + fringe, the only kimono |
| 2 | `cast/hero.jpg` | HERO | the only platinum blonde, the only one with the magazine |
| 3 | `cast/feather.jpg` | FEATHER | the only lavender feather dress |
| 4 | `cast/slicked.jpg` | SLICKED | the only slicked-back bun, white midi + knit |
| 5 | `cast/silverman.jpg` | SILVERMAN | the only man, silver hair |
| 6 | `plates/scene_empty.jpg` | LOCATION | the empty street, no furniture — never changes |
| 7 | `props/sofa_table.jpg` | furniture look | sofa + travertine table (appearance only) |
| 8 | `props/desk_set.jpg` | furniture look | desk + laptop + lamp + chair (appearance only) |
| 9 | `blocking/shots/<beat>.png` | blocking diagram | where each person AND each piece of furniture goes |

**Cast files:** one JPG per person. Left: the person's ONE front-view face. Right: their outfit front and back, with the head and all hair removed, so the only face in the file is the one on the left.

**Video calls** (Seedance) take only the approved keyframe as `first_frame`.

## Blocking (`blocking/`)
- `set_layout.png` — top view of the fixed set: sofa on the zebra crossing perpendicular to the curb, seat facing the desk; desk 2 m along at 30°; laptop on the near end, screen facing the sofa.
- `paths_v7.png` — walking paths and camera marks C1–C4.
- `shots/S1a.png … S5b.png` — one diagram per beat (top view + projected camera view); `shots/_all_shots.jpg` shows all nine.

## Plates (`plates/`)
- `scene_empty.jpg` — the LOCATION reference, 16:9: the empty street with no furniture. Used in every call.

## Props (`props/`) — appearance only
- `sofa_table.jpg`, `desk_set.jpg`

## Edit-only artwork (`art/`) — composited in the edit, never in a generation call
- `magazine_spread.png`, `treg_logo.png`

## Scripts (`prompts/`)
- `shotdiagrams.py`, `set_layout.py`, `blocking_v7.py` — redraw the blocking images.

Everything older (character sheets, face boards, prop sheets, all earlier keyframes, the furnished and portrait plates, drafts, storyboards) was removed on Nov 10 so nothing can reference it by mistake. It is still in the git history if ever needed.
