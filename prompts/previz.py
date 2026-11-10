"""Stand-in previz: draw furniture boxes and person mannequins at exact projected
positions ON the real empty plate, from the calibrated plate camera."""
import sys, math, json
sys.path.insert(0, '/home/claude')
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import shotdiagrams as sd

PLATE = '/home/claude/treg-ugc-assets/plates/scene_empty.jpg'
FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 34)

def mk(cx, cy, cz, yawdeg, pitch):
    y = math.radians(yawdeg)
    return dict(x=cx, y=cy, z=cz, look=(cx + math.cos(y), cy + math.sin(y)), pitch=pitch, roll=0)

PLATE_CAM = mk(-2.981, -8.875, 1.796, 47.2, -7.75)   # fitted to scene_empty.jpg + Chia's couch/desk boxes

COL = {'L': (30, 30, 30), 'H': (232, 210, 122), 'FE': (165, 143, 214), 'SM': (154, 163, 173), 'SL': (199, 185, 166)}
FCOL = {'sofa': (239, 232, 218), 'table': (228, 217, 195), 'desk': (214, 185, 140), 'laptop': (201, 205, 210),
        'screen': (120, 170, 255), 'lamp': (20, 20, 20), 'chair': (168, 116, 63)}

def px(cam, X, Y, Z, W, H):
    p = sd.project(cam, X, Y, Z)
    if p is None:
        return None
    u, v = sd.to_axes(p[:2])
    return (u / 16 * W, (1 - v / 9) * H)

def box(draw, cam, pts, z0, z1, fill, W, H, outline=(0, 0, 0)):
    base = [px(cam, x, y, z0, W, H) for x, y in pts]
    top = [px(cam, x, y, z1, W, H) for x, y in pts]
    if not all(base) or not all(top):
        return
    from scipy.spatial import ConvexHull
    allp = np.array(base + top)
    hull = allp[ConvexHull(allp).vertices]
    draw.polygon([tuple(p) for p in hull], fill=fill, outline=outline, width=3)
    draw.polygon(top, outline=outline, width=2)

def circle_pts(cx, cy, r, n=16):
    return [(cx + r * math.cos(t), cy + r * math.sin(t)) for t in np.linspace(0, 2 * math.pi, n, endpoint=False)]

def draw_furniture(draw, cam, W, H):
    box(draw, cam, sd.SOFA['poly'], 0, 0.45, FCOL['sofa'], W, H)
    box(draw, cam, sd.SOFA_BACK['poly'], 0, 0.85, (216, 207, 189), W, H)
    cx, cy, r = sd.TABLE['circle']; box(draw, cam, circle_pts(cx, cy, r), 0, 0.42, FCOL['table'], W, H)
    box(draw, cam, sd.DESK['poly'], 0.68, 0.76, FCOL['desk'], W, H)          # desk top slab
    for lx, ly in [(1.1, -3.95), (2.1, -5.25), (1.75, -3.7), (1.45, -5.5)]:  # legs
        box(draw, cam, [(lx - 0.03, ly - 0.03), (lx + 0.03, ly - 0.03), (lx + 0.03, ly + 0.03), (lx - 0.03, ly + 0.03)], 0, 0.72, (90, 70, 40), W, H)
    box(draw, cam, sd.LAPTOP['poly'], 0.76, 0.78, FCOL['laptop'], W, H)       # base
    box(draw, cam, sd.SCREEN['poly'], 0.76, 0.98, FCOL['screen'], W, H)       # screen, facing the sofa
    cx, cy, r = sd.LAMP['circle']; box(draw, cam, circle_pts(cx, cy, 0.03), 0.76, 1.15, FCOL['lamp'], W, H); box(draw, cam, circle_pts(cx, cy, r), 1.12, 1.25, FCOL['lamp'], W, H)
    cx, cy, r = sd.CHAIR['circle']; box(draw, cam, circle_pts(cx, cy, r), 0.42, 0.47, FCOL['chair'], W, H); box(draw, cam, circle_pts(cx + 0.22, cy, 0.05), 0.45, 0.9, FCOL['chair'], W, H)

def draw_person(draw, cam, p, W, H):
    hgt = sd.person_height(p)
    k, x, y = p['k'], p['x'], p['y']
    col = COL[k]
    shoulder_w = 0.42; body_d = 0.22
    a = math.radians(p['face'])
    # body box oriented by facing: width across facing direction
    ux, uy = -math.sin(a), math.cos(a)   # across
    fx, fy = math.cos(a), math.sin(a)    # facing
    def rect(cx, cy, w, d):
        return [(cx + ux*w/2 + fx*d/2, cy + uy*w/2 + fy*d/2), (cx - ux*w/2 + fx*d/2, cy - uy*w/2 + fy*d/2),
                (cx - ux*w/2 - fx*d/2, cy - uy*w/2 - fy*d/2), (cx + ux*w/2 - fx*d/2, cy + uy*w/2 - fy*d/2)]
    if p['pose'] == 'stand':
        box(draw, cam, rect(x, y, 0.34, 0.24), 0, hgt - 0.78, col, W, H)            # legs
        box(draw, cam, rect(x, y, shoulder_w, body_d), hgt - 0.78, hgt - 0.22, col, W, H)  # torso
        head_z0 = hgt - 0.22
    else:
        box(draw, cam, rect(x, y, shoulder_w, 0.45), 0.42, hgt - 0.22, col, W, H)
        head_z0 = hgt - 0.22
    box(draw, cam, circle_pts(x + fx*0.02, y + fy*0.02, 0.11, 10), head_z0, head_z0 + 0.22, col, W, H)
    # nose marker to show facing
    npt = px(cam, x + fx*0.14, y + fy*0.14, head_z0 + 0.1, W, H)
    if npt: draw.ellipse([npt[0]-6, npt[1]-6, npt[0]+6, npt[1]+6], fill=(255, 60, 60))
    top = px(cam, x, y, head_z0 + 0.3, W, H)
    if top:
        draw.text((top[0], top[1] - 40), k, fill='white', font=FONT, anchor='ms', stroke_width=3, stroke_fill='black')

def render(people, cam=None, out=None, label=''):
    cam = cam or PLATE_CAM
    im = Image.open(PLATE).convert('RGB'); W, H = im.size
    draw = ImageDraw.Draw(im, 'RGBA')
    # depth sort: furniture then people by distance (far first)
    draw_furniture(draw, cam, W, H)
    for p in sorted(people, key=lambda q: -math.hypot(q['x'] - cam['x'], q['y'] - cam['y'])):
        draw_person(draw, cam, p, W, H)
    if label:
        draw.text((20, 20), label, fill='white', font=FONT, stroke_width=3, stroke_fill='black')
    if out:
        im.save(out, quality=92)
    return im

if __name__ == '__main__':
    beats = {b[0]: b for b in sd.SHOTS}
    for sid in ['S1a', 'S1b', 'S2a', 'S3a']:
        render(beats[sid][3], out=f'/home/claude/treg-ugc-assets/blocking/previz/{sid}.jpg', label=f'{sid}  stand-ins: replace each coloured box with the real person or furniture in exactly this spot')
