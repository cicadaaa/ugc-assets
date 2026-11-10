# Keyframe prompt (v4.2) — one template, every beat

Model: `reapi.image-gen.gemini-3-pro-image`, 9:16, 2K. `image_urls`, always this order:

1. `cast/leader.jpg`  2. `cast/hero.jpg`  3. `cast/feather.jpg`  4. `cast/slicked.jpg`  5. `cast/silverman.jpg`
6. `plates/scene_empty.jpg`  7. `props/sofa_table.jpg`  8. `props/desk_set.jpg`  9. `blocking/shots/<BEAT>.png`

Base: `https://raw.githubusercontent.com/cicadaaa/ugc-assets/main/`

## Fixed part (identical for every beat)

```
REFERENCES. Images 1-5 are five different people, ONE file per person. In each file the photo on the LEFT is that person's only face; the photos on the RIGHT are that person's outfit from the front and the back with the head and hair deliberately removed. Copy each face exactly from the left photo and each outfit exactly from the right photos. Never blend two people, never swap a face or a garment between people, never invent anyone.
Image 1 = LEADER: a young woman about 25, black blunt bob with a straight fringe, the ONLY person in a kimono (off-white pinstripe yukata, wide charcoal obi, white tabi, wooden zori).
Image 2 = HERO: a young woman about 24, the ONLY platinum blonde, freckles, black scoop tank, white pleated trousers, black Mary Janes, the ONLY one holding a magazine (blank off-white pages).
Image 3 = FEATHER: long wavy black hair, lavender ostrich-feather dress.
Image 4 = SLICKED: hair slicked into a low bun, white drop-waist midi dress, oatmeal knit tied over the shoulders.
Image 5 = SILVERMAN: the only man, shoulder-length silver hair, white tee, beige chinos.
Image 6 = the LOCATION: the empty street with no furniture. Its building, sidewalk, curb and zebra crossing never change; build the frame inside this exact location.
Image 7 = what the cream sofa and the round travertine table look like. Image 8 = what the oak desk, silver laptop, black dome lamp and tan chair look like. Copy their appearance exactly; they are references for LOOK only, not for position.
Image 9 = the BLOCKING DIAGRAM for this frame. It sets the position of every piece of furniture and every person. Left half: top view, red square = this camera, arrows = which way each person faces. Right half: the camera view, where each labelled shape (L, H, FE, SM, SL) must land in the frame. Place each person and each piece of furniture exactly where its shape is, facing the way the top view shows. The sofa stands on the zebra crossing perpendicular to the curb, seat facing the desk; the desk stands on the crossing two metres along the curb at 30 degrees; the laptop sits on the desk end nearest the sofa with its screen facing the sofa.
Exactly five people in the scene, never more. HERO is always right beside LEADER, on LEADER's right. The laptop stays on the desk with its screen facing the sofa and its lid blank.
LOOK. Fujifilm X100VI 23mm f/2, Eterna film simulation, vertical 9:16, handheld by one young man standing on the sidewalk at chest height, looking slightly down onto the crossing. Soft overcast late-afternoon light around 6500K, no sun, no hard shadows; faces lit evenly by the grey sky, neutral skin with visible pores, fine grain, slight handheld imperfection. A light breeze in hair and fabric.
```

## Beat part (replace per beat)

```
THIS FRAME: <beat text from the shot plan, section 4>
```

## Ending (identical for every beat)

```
Avoid: airbrushed skin, studio light, direct sun, extra people, passers-by, a second kimono, a second blonde, any text on the magazine, any logo or sticker on the laptop, readable signs, borders, an older-looking LEADER, a laptop that is turned toward the camera, furniture placed anywhere other than where image 9 puts it, furniture that looks different from images 7-8.
```
