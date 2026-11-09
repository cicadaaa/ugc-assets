# S1 keyframe prompt (walk across the crossing, 0:00 frame)

Use with Gemini 3 Pro Image on reAPI, 9:16, 2K, `image_urls` in this order:

1. `cast/leader.jpg`  — LEADER
2. `cast/hero.jpg` — HERO
3. `cast/feather.jpg` — FEATHER
4. `cast/slicked.jpg` — SLICKED
5. `cast/silverman.jpg` — SILVERMAN
6. `plates/p1_master.png` — the street

Base URL: `https://raw.githubusercontent.com/cicadaaa/ugc-assets/main/`

## Prompt

```
Five reference images of five different people are attached, then one photo of the street. Each reference shows ONE person: face on the left, full body on the right. Reproduce each person's exact face, hair, body and outfit. Do not blend them. Do not invent anyone.

IDENTITY RULES (strict):
LEADER (image 1) = the only woman with a black blunt bob and straight fringe, and the ONLY person wearing a kimono: off-white pinstripe yukata, wide charcoal obi, white tabi, wooden zori.
HERO (image 2) = the only platinum blonde, freckles, and the ONLY person holding the magazine: black scoop tank, white pleated trousers, black Mary Janes.
FEATHER (image 3) = the only woman in the lavender ostrich-feather dress, long wavy black hair.
SLICKED (image 4) = the only woman with hair slicked back into a low bun: white drop-waist midi dress, oatmeal knit tied over the shoulders, black flats.
SILVERMAN (image 5) = the only man, shoulder-length silver hair: white crew tee, beige chinos, black belt, black slides.
No one else wears a kimono. No one else is blonde. No one else holds a magazine. Exactly five people in the frame, no extras, no one with glasses.

Shot on a Fujifilm X100VI, 23mm f/2, Eterna film simulation, held vertically 9:16 by a man at chest height. Low saturation, soft contrast, lifted shadows, shallow depth of field, fine grain.

Location is image 6, same building, same sofa and travertine table on the zebra crossing, same angled oak desk on the sidewalk. Soft overcast late-afternoon light around 6500K, no direct sun, no hard shadows; people lit only by the grey sky, neutral skin, soft dim catchlights. Warm shop-window glow stays in the background.

Composition: LEADER and HERO walk side by side toward the camera on the white stripes of the crossing, mid-step, full body, LEADER slightly left of centre and in focus, chin up, amused half-smile, mouth just opening to speak. HERO on her right holds an open large-format magazine up in front of her face with both hands; only her eyes and brows show over the top edge; the left page reads "3X CHEAPER" in huge thin black serif capitals on two lines, the right page is a black-and-white photo of legs on a crossing. Behind them, soft and out of focus: SILVERMAN mid-jump onto the cream sofa, laughing; FEATHER sitting on the sofa arm leaning away from him, laughing; SLICKED standing behind the sofa twisting FEATHER's hair, closed-lip smile. Nobody in the background looks at the camera. A light breeze lifts hair and loose fabric.

Natural skin with visible pores, slight asymmetry, no airbrushing. No text anywhere except the magazine. No logos, no signs, no borders.
```

## Fallback (if identities still drift)
Remove the jump: SILVERMAN already seated on the sofa, laughing. If it drifts again, generate LEADER and HERO only, with the three background people as a soft, blurred group far behind.

## Gate 1 check before any video
- LEADER face = cast/leader.jpg, bob + fringe, kimono on her and only her
- HERO face = cast/hero.jpg, platinum, magazine in her hands
- Background three: right outfit on the right body, no extra people
- "3X CHEAPER" spelled correctly
- Light: even, neutral, no sun
