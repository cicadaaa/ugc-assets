"""Draw, for every beat of the treg hook, a top-view blocking frame and a projected
9:16 camera-view frame. Pure matplotlib, no API. World: metres; x along the curb
(sofa near x=1.2, desk near x=4.2); y>0 sidewalk/building, y<0 road; z up."""
import math, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, Wedge, FancyArrowPatch, FancyBboxPatch

OUT = "/home/claude/treg-ugc-assets/blocking/shots"
os.makedirs(OUT, exist_ok=True)

COL = dict(L="#1f1f1f", H="#e8d27a", FE="#a58fd6", SM="#9aa3ad", SL="#c7b9a6", CAM="#d2452c")
TXT = dict(L="white", H="black", FE="white", SM="white", SL="black")
NAME = dict(L="LEADER", H="HERO", FE="FEATHER", SM="SILVERMAN", SL="SLICKED")

# ---------- fixed set ----------
def rot(cx, cy, w, h, ang):
    a = math.radians(ang)
    return [(cx + dx*math.cos(a) - dy*math.sin(a), cy + dx*math.sin(a) + dy*math.cos(a))
            for dx, dy in [(-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2)]]

SOFA = dict(poly=[(0.72, -2.4), (1.68, -2.4), (1.68, -0.1), (0.72, -0.1)], h=0.45, fc="#efe8da", ec="#8a7f6a", label="sofa")
SOFA_BACK = dict(poly=[(0.72, -2.4), (0.95, -2.4), (0.95, -0.1), (0.72, -0.1)], h=0.85, fc="#d8cfbd", ec="#8a7f6a", label="")
TABLE = dict(circle=(1.2, -3.0, 0.36), h=0.42, fc="#e4d9c3", ec="#8a7f6a", label="table")
DESK = dict(poly=rot(4.2, -0.8, 1.9, 0.75, -30), h=0.75, fc="#d6b98c", ec="#7a6240", label="desk")
LAPTOP = dict(poly=rot(3.72, -0.6, 0.32, 0.44, 0), h=0.77, fc="#c9cdd2", ec="#333", label="")
SCREEN = dict(poly=[(3.56, -0.82), (3.59, -0.82), (3.59, -0.38), (3.56, -0.38)], h=0.98, z0=0.76, fc="#9ecbff", ec="#1f5fbf", label="screen")
LAMP = dict(circle=(4.85, -1.2, 0.14), h=1.25, fc="#111", ec="#111", label="lamp")
CHAIR = dict(circle=(5.4, -0.75, 0.28), h=0.9, fc="#a8743f", ec="#5a3b1e", label="chair")
FURN = [SOFA, SOFA_BACK, TABLE, DESK, LAPTOP, SCREEN, LAMP, CHAIR]

# ---------- people ----------
def P(k, x, y, pose="stand", face=0.0, note=""):
    """pose: stand / sit / kneel. face: heading in degrees (0 = +x toward the desk, 90 = toward the building/camera side)."""
    return dict(k=k, x=x, y=y, pose=pose, face=face, note=note)

HEIGHT = dict(stand=dict(L=1.66, H=1.76, FE=1.72, SM=1.84, SL=1.70), sit=1.25, kneel=1.15)

def person_height(p):
    return HEIGHT["stand"][p["k"]] if p["pose"] == "stand" else HEIGHT[p["pose"]]

# ---------- camera ----------
def CAM(x, y, look, z=1.3, pitch=-8, roll=0.0, note=""):
    return dict(x=x, y=y, z=z, look=look, pitch=pitch, roll=roll, note=note)

F_MM, SENSOR_W, SENSOR_H = 23.0, 23.5, 13.2   # 16:9 landscape crop of APS-C (X100VI held horizontally)

def project(cam, X, Y, Z):
    """World -> image plane (u right, v up) in sensor mm, plus depth."""
    lx, ly = cam["look"]
    yaw = math.atan2(ly - cam["y"], lx - cam["x"])
    pitch = math.radians(cam["pitch"])
    dx, dy, dz = X - cam["x"], Y - cam["y"], Z - cam["z"]
    # rotate into camera frame: forward f, right r, up u
    f = dx*math.cos(yaw) + dy*math.sin(yaw)
    r = dx*math.sin(yaw) - dy*math.cos(yaw)
    u = dz
    f2 = f*math.cos(pitch) + u*math.sin(pitch)
    u2 = -f*math.sin(pitch) + u*math.cos(pitch)
    if f2 <= 0.05:
        return None
    uu = F_MM * r / f2
    vv = F_MM * u2 / f2
    ro = math.radians(cam["roll"])
    uu, vv = uu*math.cos(ro) - vv*math.sin(ro), uu*math.sin(ro) + vv*math.cos(ro)
    return uu, vv, f2

def to_axes(uv):
    """sensor mm -> axes coords in a 16:9 frame of width 16, height 9."""
    uu, vv = uv
    return 8 + uu / (SENSOR_W/2) * 8, 4.5 + vv / (SENSOR_H/2) * 4.5

# ---------- drawing: top view ----------
def draw_top(ax, people, cam, title):
    ax.set_xlim(-1.0, 6.5); ax.set_ylim(-4.0, 3.2); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Rectangle((-1, -4), 7.5, 4, color="#5f6368"))
    ax.add_patch(Rectangle((-1, 0), 7.5, 2.4, color="#d9d4cc"))
    ax.add_patch(Rectangle((-1, 2.4), 7.5, 0.8, color="#a89f91"))
    for i in range(4):
        ax.add_patch(Rectangle((-0.6 + i*1.8, 2.4), 1.2, 0.25, color="#3b3a36"))
    ax.plot([-1, 6.5], [0, 0], color="#999", lw=3)
    for i in range(7):
        ax.add_patch(Rectangle((-0.3, -0.5 - i*0.6), 6.3, 0.32, color="#efefef", alpha=.85))
    for fobj in FURN:
        if "poly" in fobj:
            ax.add_patch(Polygon(fobj["poly"], closed=True, fc=fobj["fc"], ec=fobj["ec"], lw=1.2, zorder=3))
        else:
            cx, cy, r = fobj["circle"]; ax.add_patch(Circle((cx, cy), r, fc=fobj["fc"], ec=fobj["ec"], lw=1.2, zorder=3))
    ax.text(1.2, -1.25, "SOFA", rotation=90, ha="center", va="center", fontsize=7, zorder=4)
    ax.text(4.3, -0.9, "DESK", rotation=-30, ha="center", va="center", fontsize=7, zorder=4)
    ax.annotate("", xy=(3.2, -0.6), xytext=(3.55, -0.6), arrowprops=dict(arrowstyle="-|>", color="#1f5fbf", lw=1.3), zorder=5)
    ax.add_patch(Rectangle((1.75, -1.2), 1.6, 1.1, fill=False, ec="#d2452c", ls="--", lw=1.2, zorder=4))
    ax.text(2.55, -1.35, "L+H LANE: only here, on the stripes,\nbetween sofa and desk (1.7 m)", ha="center", va="top", fontsize=5.8, color="#8a2414", zorder=5)
    ax.add_patch(Rectangle((0.6, -3.5), 1.25, 3.5, fill=False, ec="#7a6aa8", ls=":", lw=1.1, zorder=4))
    ax.text(1.2, 0.08, "crew: ON the sofa / armrest / table only", ha="center", va="bottom", fontsize=5.5, color="#5b4a8a", zorder=5)
    # camera frustum
    lx, ly = cam["look"]; yaw = math.degrees(math.atan2(ly - cam["y"], lx - cam["x"]))
    hfov = math.degrees(2*math.atan((SENSOR_W/2)/F_MM))
    ax.add_patch(Wedge((cam["x"], cam["y"]), 3.2, yaw - hfov/2, yaw + hfov/2, fc=COL["CAM"], alpha=.13, zorder=2))
    ax.add_patch(Rectangle((cam["x"]-0.15, cam["y"]-0.15), 0.3, 0.3, fc=COL["CAM"], ec="black", lw=.8, zorder=8))
    ax.text(cam["x"], cam["y"]+0.3, "CAM", ha="center", fontsize=7, color=COL["CAM"], weight="bold", zorder=9)
    # people
    for p in people:
        r = 0.22 if p["pose"] == "stand" else 0.2
        ax.add_patch(Circle((p["x"], p["y"]), r, fc=COL[p["k"]], ec="black", lw=.8, zorder=6))
        ax.text(p["x"], p["y"], p["k"], ha="center", va="center", fontsize=6.5, color=TXT[p["k"]], weight="bold", zorder=7)
        a = math.radians(p["face"])
        ax.add_patch(FancyArrowPatch((p["x"] + r*math.cos(a), p["y"] + r*math.sin(a)),
                                     (p["x"] + (r+0.3)*math.cos(a), p["y"] + (r+0.3)*math.sin(a)),
                                     arrowstyle="-|>", mutation_scale=9, color=COL[p["k"]] if p["k"] != "L" else "#444", lw=1.2, zorder=6))
    ax.text(-0.9, 3.0, title, fontsize=9, weight="bold", va="top")
    ax.text(-0.9, -3.9, "top view · arrows = facing · red wedge = lens", fontsize=6.5, color="#333")

# ---------- drawing: camera view ----------
def draw_cam(ax, people, cam, title):
    clip = Rectangle((0, 0), 16, 9, transform=ax.transData)
    ax.set_xlim(0, 16); ax.set_ylim(0, 9); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 16, 9, fc="#cfd3d6", ec="black", lw=1.5))
    # ground: stripes and curb line as projected polylines
    def poly_world(pts, z=0.0):
        out = []
        for (X, Y) in pts:
            pr = project(cam, X, Y, z)
            if pr is None:
                return None
            out.append(to_axes(pr[:2]))
        return out
    # road, sidewalk, building bands
    for (pts, col) in [([(-6, -9), (12, -9), (12, 0), (-6, 0)], "#5f6368"),
                       ([(-6, 0), (12, 0), (12, 2.4), (-6, 2.4)], "#d9d4cc"),
                       ([(-6, 2.4), (12, 2.4), (12, 2.4)], None)]:
        if col is None:
            continue
        pw = poly_world(pts)
        if pw:
            ax.add_patch(Polygon(pw, closed=True, fc=col, ec="none", zorder=1))
    # building as a wall from y=2.4 up to z=6
    wall = []
    for (X, Y, Z) in [(-6, 2.4, 0), (12, 2.4, 0), (12, 2.4, 7), (-6, 2.4, 7)]:
        pr = project(cam, X, Y, Z)
        if pr is None:
            wall = None; break
        wall.append(to_axes(pr[:2]))
    if wall:
        ax.add_patch(Polygon(wall, closed=True, fc="#a89f91", ec="none", zorder=1))
        for i in range(-3, 7):
            w = poly_world([(i*1.8, 2.41), (i*1.8+1.2, 2.41)], 0.3)
            w2 = poly_world([(i*1.8, 2.41), (i*1.8+1.2, 2.41)], 2.6)
            if w and w2:
                ax.add_patch(Polygon([w[0], w[1], w2[1], w2[0]], closed=True, fc="#3b3a36", ec="none", zorder=1))
    for i in range(7):
        s = poly_world([(-0.3, -0.5 - i*0.6), (6.0, -0.5 - i*0.6), (6.0, -0.18 - i*0.6), (-0.3, -0.18 - i*0.6)])
        if s:
            ax.add_patch(Polygon(s, closed=True, fc="#efefef", ec="none", alpha=.85, zorder=1))
    lane = poly_world([(1.75, -1.2), (3.35, -1.2), (3.35, -0.1), (1.75, -0.1)])
    if lane:
        ax.add_patch(Polygon(lane, closed=True, fc="none", ec="#d2452c", ls="--", lw=1.0, zorder=2))
    # depth-sorted objects
    items = []
    for fobj in FURN:
        if "poly" in fobj:
            cx = np.mean([p[0] for p in fobj["poly"]]); cy = np.mean([p[1] for p in fobj["poly"]])
        else:
            cx, cy, _ = fobj["circle"]
        d = math.hypot(cx - cam["x"], cy - cam["y"]); items.append((d, "f", fobj))
    for p in people:
        d = math.hypot(p["x"] - cam["x"], p["y"] - cam["y"]); items.append((d, "p", p))
    items.sort(key=lambda t: -t[0])
    for d, kind, o in items:
        if kind == "f":
            z0 = o.get("z0", 0.0)
            if "poly" in o:
                pts = o["poly"]
            else:
                cx, cy, r = o["circle"]; pts = [(cx + r*math.cos(t), cy + r*math.sin(t)) for t in np.linspace(0, 2*math.pi, 16)]
            base = poly_world(pts, z0); top = poly_world(pts, o["h"])
            if not base or not top:
                continue
            # draw sides as hull of base+top (simple: fill union polygon of top and base via convex hull)
            allpts = np.array(base + top)
            try:
                from scipy.spatial import ConvexHull
                hull = allpts[ConvexHull(allpts).vertices]
            except Exception:
                hull = allpts
            ax.add_patch(Polygon(hull, closed=True, fc=o["fc"], ec=o["ec"], lw=1, zorder=3, alpha=0.95))
            if o["label"]:
                cx = np.mean([p[0] for p in top]); cy = np.mean([p[1] for p in top])
                ax.text(cx, cy, o["label"], ha="center", va="center", fontsize=6.5, color="#222", zorder=4)
        else:
            p = o; hgt = person_height(p)
            foot = project(cam, p["x"], p["y"], 0.0); head = project(cam, p["x"], p["y"], hgt)
            shoulder = project(cam, p["x"], p["y"], hgt - 0.25)
            if foot is None or head is None:
                # person partly behind/beside the camera: draw a big soft foreground shape at the edge
                continue
            fx, fy = to_axes(foot[:2]); hx, hy = to_axes(head[:2]); sx, sy = to_axes(shoulder[:2])
            depth = head[2]
            k = F_MM / depth * (16 / SENSOR_W)                # metres -> axes units at this depth
            headr = 0.11 * k
            bodyw = (0.46 if p["pose"] == "stand" else 0.55) * k
            ax.add_patch(FancyBboxPatch((sx - bodyw/2, fy), bodyw, max(sy - fy, 0.05), boxstyle="round,pad=0.02",
                                        fc=COL[p["k"]], ec="black", lw=.8, zorder=5, alpha=.95))
            ax.add_patch(Circle((hx, hy - headr*0.2), headr, fc=COL[p["k"]], ec="black", lw=.8, zorder=6))
            ax.text(hx, hy - headr*0.2, p["k"], ha="center", va="center", fontsize=max(5, min(11, headr*22)), color=TXT[p["k"]], weight="bold", zorder=7)
            if p["note"]:
                ax.text(hx, hy + headr + 0.15, p["note"], ha="center", va="bottom", fontsize=5.5, color="#111", zorder=7,
                        bbox=dict(fc="white", ec="none", alpha=.7, pad=1))
    for art in ax.patches[1:] + ax.texts:
        art.set_clip_path(clip)
    ax.text(8, 8.75, title, ha="center", va="top", fontsize=8.5, weight="bold", color="white",
            bbox=dict(fc="black", alpha=.6, pad=3))
    ax.text(0.15, 0.15, "camera view · 23mm · 16:9 landscape · shapes = where each person/prop lands in frame", fontsize=5.5, color="white",
            bbox=dict(fc="black", alpha=.5, pad=1.5))

def render(shot_id, title, beat_text, people, cam):
    fig = plt.figure(figsize=(15, 6.2), dpi=150)
    ax1 = fig.add_axes([0.01, 0.17, 0.40, 0.80])
    ax2 = fig.add_axes([0.42, 0.20, 0.57, 0.74])
    draw_top(ax1, people, cam, f"{shot_id}  {title}")
    draw_cam(ax2, people, cam, f"{shot_id} · {cam['note']}")
    fig.text(0.02, 0.02, beat_text, fontsize=8.6, va="bottom", wrap=True,
             bbox=dict(fc="white", ec="#999", boxstyle="round,pad=0.5"))
    path = f"{OUT}/{shot_id}.png"
    fig.savefig(path); plt.close(fig)
    return path

# ---------- the beats ----------
# crew home marks
FE_home = P("FE", 1.35, -1.9, "kneel", 90, "on the seat")
SM_home = P("SM", 1.4, -2.5, "sit", 90, "on the armrest")
SL_home = P("SL", 1.2, -3.0, "sit", 90, "on the table")

SHOTS = [
 ("S1a", "Sofa, camera arrives",
  "S1a 0:00  All five at the sofa. LEADER sits at the curb end of the sofa, HERO right beside her on her right (the road side), magazine closed on her lap. "
  "FEATHER bounces on the far seat; SILVERMAN sits on the road-end armrest and hops up and down on it; SLICKED sits on the travertine table facing the sofa. Nobody stands behind the sofa. "
  "Camera C1 on the sidewalk, 2.6 m back from the curb, looking down at the sofa. LEADER glances up at the lens. Desk at the right frame edge.",
  [P("L", 1.35, -0.55, "sit", 0, "sits, curb end"), P("H", 1.35, -1.25, "sit", 0, "sits beside L"), FE_home, SM_home, SL_home],
  CAM(2.9, 2.6, (1.4, -1.4), z=1.5, pitch=-7, note="C1 · wide on the sofa")),
 ("S1b", "They stand and walk; camera backs up",
  "S1b 0:00.8  LEADER and HERO are up and walking along the curb toward the desk, HERO glued to LEADER's right (road side), magazine now open over her face. They walk ON the white stripes, inside the 1.7 m lane between sofa and desk, never up onto the sidewalk. "
  "Camera walks BACKWARD 2 m ahead of them along the sidewalk, step bob, slight tilt. Crew stays at the sofa, 1–2 m behind the pair, soft. LEADER looks into the lens.",
  [P("L", 2.3, -0.4, "stand", 0, "walking, eyes on lens"), P("H", 2.3, -1.0, "stand", 0, "magazine over face"), FE_home, SM_home, SL_home],
  CAM(3.7, 2.7, (2.3, -0.7), z=1.5, pitch=-5, roll=2, note="C1→C2 · walking backward")),
 ("S2a", "At the desk; LEADER starts her line",
  "S2a 0:02  They stop at the desk's near end: HERO's right hip almost touches the desk corner, LEADER one step to her left. Both stand on the stripes below the curb; the camera man is the only one on the sidewalk. "
  "magazine lowered to her chest, looking at LEADER. Camera C2 on the sidewalk, 2.6 m back from the curb. LEADER: 'Still paying Higgsfield for this?' Crew soft 2 m behind.",
  [P("L", 2.85, -0.45, "stand", 90, "faces lens, speaking"), P("H", 3.2, -0.3, "stand", 120, "at the desk corner, looks at L"),
   FE_home, SM_home, SL_home],
  CAM(4.1, 2.6, (2.95, -0.45), z=1.5, pitch=-4, note="C2 · medium two-shot")),
 ("S2b", "Push-in on LEADER",
  "S2b 0:03  While LEADER speaks the camera walks in to 0.8 m: her face and upper body fill the frame, focus on her eyes, proud cute micro-expressions. "
  "HERO is a soft shape at the right edge, still looking at LEADER. Nothing else sharp.",
  [P("L", 2.85, -0.45, "stand", 90, "close-up"), P("H", 3.2, -0.3, "stand", 120, "soft, edge"), FE_home, SM_home, SL_home],
  CAM(3.15, 0.75, (2.85, -0.45), z=1.5, pitch=0, note="C2+ · close on LEADER")),
 ("S3a", "HERO speaks; camera turns to her",
  "S3a 0:04.5  HERO: 'We made Higgsfield 3x cheaper… I cost [$HF] on Higgsfield, and now [$TREG] on treg.' Camera pans from LEADER to HERO (small overshoot, refocus) and holds on her. "
  "HERO looks lens → LEADER → lens; LEADER watches HERO, hand on her shoulder. Same marks as S2a.",
  [P("L", 2.85, -0.45, "stand", 30, "watches H"), P("H", 3.2, -0.3, "stand", 100, "speaking to lens"), FE_home, SM_home, SL_home],
  CAM(4.1, 2.6, (3.2, -0.3), z=1.5, pitch=-4, note="C2 · on HERO")),
 ("S3b", "Camera walks round to LEADER's left",
  "S3b 0:07  Still on HERO's price line, the camera man walks along the curb to C3, on LEADER's LEFT (the sofa side), 1 m from her. Each step a dip, horizon rolls a degree or two. "
  "In the near foreground: LEADER's left shoulder, kimono sleeve and the back of her bob, soft. HERO still talking beyond her. Desk and laptop behind them.",
  [P("L", 2.85, -0.45, "stand", 40, "fg shoulder"), P("H", 3.2, -0.3, "stand", 150, "talking"), FE_home, SM_home, SL_home],
  CAM(1.9, 0.6, (3.2, -0.35), z=1.5, pitch=-1, roll=3, note="C3 · arriving, over L's shoulder")),
 ("S4", "LEADER turns her head and speaks side-on",
  "S4 0:10  LEADER keeps her body toward the desk but turns her head over her LEFT shoulder to the camera beside her: three-quarter profile, chest-up, sly proud half-smile, line TBD. "
  "HERO behind her on the right, soft, smiling at her. Camera C3 standing still: only breath sway.",
  [P("L", 2.85, -0.45, "stand", 150, "head turned to lens"), P("H", 3.2, -0.3, "stand", 170, "soft, smiling at L"), FE_home, SM_home, SL_home],
  CAM(1.85, 0.5, (2.85, -0.45), z=1.5, pitch=0, note="C3 · side-on close-up")),
 ("S5a", "Behind LEADER: over her left shoulder onto the laptop",
  "S5a 0:11.5  LEADER steps to the laptop on the desk's near end and stands facing its screen (the screen faces the sofa, so she stands on the sofa side of the desk with her BACK to the sofa and to the camera). "
  "The camera man steps in BEHIND her, slightly to her left, on the crossing, lens at her shoulder height looking past her left shoulder down onto the screen. We see the BACK of her black bob, the edge of her left ear, her left shoulder and kimono sleeve, soft and large at the RIGHT edge of the frame, and the glowing screen beyond in the middle. Her FACE IS NOT VISIBLE. HERO on LEADER's right, seen from behind-three-quarter, leaning in.",
  [P("L", 3.0, -0.55, "stand", 0, "back to camera, at the desk edge"), P("H", 2.95, -1.1, "stand", 25, "leans in"), FE_home, SM_home, SL_home],
  CAM(2.5, 0.08, (3.58, -0.62), z=1.55, pitch=-20, note="C4 · behind her, over the left shoulder")),
 ("S5b", "Push-in past her shoulder to the screen",
  "S5b 0:12.5  From behind her the camera pushes forward past her left shoulder until the plain glowing screen fills most of the frame: the back of her bob and the edge of her shoulder slide out of frame on the right, soft. Still no face. No UI, no logo. Hand-off frame for the match cut to the screen recording.",
  [P("L", 3.0, -0.55, "stand", 0, "back of head, soft"), P("H", 2.95, -1.1, "stand", 25, "")],
  CAM(2.95, -0.15, (3.58, -0.62), z=1.25, pitch=-16, note="C4+ · screen fills frame")),
]

if __name__ == "__main__":
    paths = [render(*s) for s in SHOTS]
    # contact sheet
    from PIL import Image
    ims = [Image.open(p) for p in paths]
    w, h = ims[0].size
    cols = 3; rows = math.ceil(len(ims)/cols)
    sheet = Image.new("RGB", (w*cols, h*rows), "white")
    for i, im in enumerate(ims):
        sheet.paste(im, ((i % cols)*w, (i//cols)*h))
    sheet.thumbnail((4200, 4200))
    sheet.save(f"{OUT}/_all_shots.jpg", quality=85)
    print("\n".join(paths))
