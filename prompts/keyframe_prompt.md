# Keyframe prompt (v5.1) — one template, every beat, 16:9

Model: `reapi.image-gen.gemini-3-pro-image`, size **16:9**, 2K. `image_urls`, always this order:

1. `cast/leader.jpg` 2. `cast/hero.jpg` 3. `cast/feather.jpg` 4. `cast/slicked.jpg` 5. `cast/silverman.jpg`
6. `plates/scene_empty.jpg` 7. `props/sofa_table.jpg` 8. `props/desk_set.jpg` 9. `blocking/shots/<BEAT>.png`

Base: `https://raw.githubusercontent.com/cicadaaa/ugc-assets/main/`

## Fixed part
```
REFERENCES. Images 1-5 are five different people, ONE file per person. In each file the photo on the LEFT is that person's only face; the photos on the RIGHT are that person's outfit from the front and the back with the head and hair deliberately removed. Copy each face exactly from the left photo and each outfit exactly from the right photos. Never blend two people, never swap a face or a garment between people, never invent anyone.
Image 1 = LEADER: a young woman about 25, black blunt bob with a straight fringe, the ONLY person in a kimono (off-white pinstripe yukata, wide charcoal obi, white tabi, wooden zori).
Image 2 = HERO: a young woman about 24, the ONLY platinum blonde, freckles, black scoop tank, white pleated trousers, black Mary Janes, the ONLY one holding a magazine (blank off-white pages).
Image 3 = FEATHER: long wavy black hair, lavender ostrich-feather dress.
Image 4 = SLICKED: hair slicked into a low bun, white drop-waist midi dress, oatmeal knit tied over the shoulders.
Image 5 = SILVERMAN: the only man, shoulder-length silver hair, white tee, beige chinos.
Image 6 = the LOCATION: this exact empty street, 16:9, with no furniture. Its carved-stone building, warm shop windows, granite sidewalk, curb and zebra crossing never change; build the frame inside this street.
Image 7 = what the cream sofa and round travertine table look like. Image 8 = what the light oak desk, silver laptop, black dome lamp and tan chair look like. Copy their appearance exactly; they are LOOK references, not position references.
Image 9 = the BLOCKING DIAGRAM for this frame. Left half: top view, red square = this camera, red wedge = where it points, arrows = which way each person faces. Right half: the 16:9 camera view, where each labelled shape (L = LEADER, H = HERO, FE, SM, SL, and the furniture) must land in the frame. Place every person and every piece of furniture exactly where its shape is.
SET RULES. The sofa stands on the zebra crossing perpendicular to the curb, one end touching the curb, seat facing the desk; the travertine table at its road end. The desk stands on the crossing two metres along the curb at 30 degrees, near end touching the curb; the laptop sits on the desk end nearest the sofa with its SCREEN FACING THE SOFA and its lid blank; the dome lamp on the far end; the tan chair behind. Exactly five people, never more. HERO is always right beside LEADER, on LEADER's right. FEATHER, SILVERMAN and SLICKED stay around the sofa.
LOOK. Fujifilm X100VI 23mm f/2, Eterna film simulation, held horizontally, 16:9 landscape frame, handheld by one young man at chest height, so the frame is never perfectly level or perfectly still. Soft overcast late-afternoon light around 6500K, no sun, no hard shadows; faces lit evenly by the grey sky, neutral skin with visible pores, fine grain. A light breeze in hair and fabric.
```
## Beat part (per beat, built from the shot plan section 6: Camera + Move + Beat)
```
THIS FRAME (<beat id>, <title>). Camera: <Camera line>. The frozen moment of this move: <Move line>
Action: <Beat text>
ASSET LOCK: the location is image 6 and it never changes. The sofa and table look exactly like image 7, the desk, laptop, lamp and chair look exactly like image 8, and every one of them stands exactly where image 9 puts it. Do not move, add, restyle or reinvent any furniture, building, curb or stripe. Every person's face and outfit come only from images 1-5.
```
## Ending
```
Avoid: airbrushed skin, studio light, direct sun, extra people, passers-by, a second kimono, a second blonde, any text on the magazine, any logo or sticker on the laptop, readable signs, borders, an older-looking LEADER, a laptop turned toward the camera, furniture placed anywhere other than where image 9 puts it, furniture that looks different from images 7-8, a different street from image 6, a vertical frame, a perfectly level tripod-steady frame.
```
