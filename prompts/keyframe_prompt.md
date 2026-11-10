# Keyframe prompt (v4.1) — one template, every beat

Model: `reapi.image-gen.gemini-3-pro-image`, 9:16, 2K. `image_urls`, always this order:

1. `cast/leader.jpg`  2. `cast/hero.jpg`  3. `cast/feather.jpg`  4. `cast/slicked.jpg`  5. `cast/silverman.jpg`
6. `plates/P-C2.jpg`  7. `blocking/shots/<BEAT>.png`

Base: `https://raw.githubusercontent.com/cicadaaa/ugc-assets/main/`

## Fixed part (identical for every beat)

```
REFERENCES. Images 1-5 are five different people, ONE file per person. In each file the photo on the LEFT is that person's only face; the photos on the RIGHT are that person's outfit from the front and the back with the head and hair deliberately removed. Copy each face exactly from the left photo and each outfit exactly from the right photos. Never blend two people, never swap a face or a garment between people, never invent anyone.
Image 1 = LEADER: a young woman about 25, black blunt bob with a straight fringe, the ONLY person in a kimono (off-white pinstripe yukata, wide charcoal obi, white tabi, wooden zori).
Image 2 = HERO: a young woman about 24, the ONLY platinum blonde, freckles, black scoop tank, white pleated trousers, black Mary Janes, the ONLY one holding a magazine (blank off-white pages).
Image 3 = FEATHER: long wavy black hair, lavender ostrich-feather dress.
Image 4 = SLICKED: hair slicked into a low bun, white drop-waist midi dress, oatmeal knit tied over the shoulders.
Image 5 = SILVERMAN: the only man, shoulder-length silver hair, white tee, beige chinos.
Image 6 = the EMPTY SET photographed from this camera position: the building, sidewalk, curb, zebra crossing, cream sofa, travertine table, oak desk, laptop, dome lamp and tan chair are all already in their final places. Keep every one of them exactly where it is. Add only the people.
Image 7 = the BLOCKING DIAGRAM for this frame. Left half: top view, red square = this camera, arrows = which way each person faces. Right half: the camera view, where each labelled shape (L, H, FE, SM, SL) must land in the frame. Place each person exactly where their shape is, facing the way the top view shows.
Exactly five people in the scene, never more. HERO is always right beside LEADER, on LEADER's right. The laptop stays on the desk with its screen facing the sofa and its lid blank.
LOOK. Fujifilm X100VI 23mm f/2, Eterna film simulation, vertical 9:16, handheld by one young man standing on the sidewalk at chest height, looking slightly down onto the crossing. Soft overcast late-afternoon light around 6500K, no sun, no hard shadows; faces lit evenly by the grey sky, neutral skin with visible pores, fine grain, slight handheld imperfection. A light breeze in hair and fabric.
```

## Beat part (replace per beat)

```
THIS FRAME: <beat text from the shot plan, section 4>
```

## Ending (identical for every beat)

```
Avoid: airbrushed skin, studio light, direct sun, extra people, passers-by, a second kimono, a second blonde, any text on the magazine, any logo or sticker on the laptop, readable signs, borders, an older-looking LEADER, a laptop that is turned toward the camera, furniture moved from where image 6 has it.
```
