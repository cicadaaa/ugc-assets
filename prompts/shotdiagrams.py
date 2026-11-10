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
TABLE = dict(circle=(2.25, -1.3, 0.36), h=0.42, fc="#e4d9c3", ec="#8a7f6a", label="table")
DESK = dict(poly=rot(1.6, -4.6, 1.9, 0.75, 70), h=0.75, fc="#d6b98c", ec="#7a6240", label="desk")
LAPTOP = dict(poly=rot(1.35, -3.95, 0.44, 0.32, 0), h=0.77, fc="#c9cdd2", ec="#333", label="")
SCREEN = dict(poly=[(1.13, -3.82), (1.57, -3.82), (1.57, -3.79), (1.13, -3.79)], h=0.98, z0=0.76, fc="#9ecbff", ec="#1f5fbf", label="screen")
LAMP = dict(circle=(1.85, -5.3, 0.14), h=1.25, fc="#111", ec="#111", label="lamp")
CHAIR = dict(circle=(2.45, -4.7, 0.28), h=0.9, fc="#a8743f", ec="#5a3b1e", label="chair")
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
    ax.set_xlim(-2.0, 5.5); ax.set_ylim(-7.0, 3.2); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Rectangle((-2, -7), 7.5, 7, color="#5f6368"))
    ax.add_patch(Rectangle((-2, 0), 7.5, 2.4, color="#d9d4cc"))
    ax.add_patch(Rectangle((-2, 2.4), 7.5, 0.8, color="#a89f91"))
    for i in range(4):
        ax.add_patch(Rectangle((-0.6 + i*1.8, 2.4), 1.2, 0.25, color="#3b3a36"))
    ax.plot([-2, 5.5], [0, 0], color="#999", lw=3)
    for i in range(11):
        ax.add_patch(Rectangle((-0.3, -0.5 - i*0.6), 6.3, 0.32, color="#efefef", alpha=.85))
    ax.add_patch(Rectangle((-2, -7), 7.5, 0.4, color="#d9d4cc"))  # near sidewalk edge (camera side)
    for fobj in FURN:
        if "poly" in fobj:
            ax.add_patch(Polygon(fobj["poly"], closed=True, fc=fobj["fc"], ec=fobj["ec"], lw=1.2, zorder=3))
        else:
            cx, cy, r = fobj["circle"]; ax.add_patch(Circle((cx, cy), r, fc=fobj["fc"], ec=fobj["ec"], lw=1.2, zorder=3))
    ax.text(1.2, -1.25, "SOFA", rotation=90, ha="center", va="center", fontsize=7, zorder=4)
    ax.text(1.6, -4.6, "DESK", rotation=70, ha="center", va="center", fontsize=7, zorder=4)
    ax.annotate("", xy=(1.35, -3.3), xytext=(1.35, -3.78), arrowprops=dict(arrowstyle="-|>", color="#1f5fbf", lw=1.3), zorder=5)
    ax.add_patch(Rectangle((0.6, -3.7), 1.3, 1.2, fill=False, ec="#d2452c", ls="--", lw=1.2, zorder=4))
    ax.text(2.0, -3.1, "L+H LANE: on the stripes,\nbetween sofa end and desk", ha="left", va="top", fontsize=5.8, color="#8a2414", zorder=5)
    ax.add_patch(Rectangle((0.6, -2.5), 2.1, 2.5, fill=False, ec="#7a6aa8", ls=":", lw=1.1, zorder=4))
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
    ax.text(-1.9, 3.0, title, fontsize=9, weight="bold", va="top")
    ax.text(-1.9, -6.9, "top view · arrows = facing · red wedge = lens", fontsize=6.5, color="#333")

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
    lane = poly_world([(0.6, -3.7), (1.9, -3.7), (1.9, -2.5), (0.6, -2.5)])
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
FE_home = P("FE", 1.35, -1.9, "kneel", 270, "on the seat")
SM_home = P("SM", 1.4, -2.45, "sit", 270, "on the armrest")
SL_home = P("SL", 2.25, -1.3, "sit", 270, "on the table")

SHOTS = [
 ("S1a", "Sofa, camera arrives",
  "S1a 0:00  All five at the sofa at the far (building) curb. LEADER sits on the sofa at the ROAD end (nearest the camera), HERO right beside her on her right, magazine closed on her lap. FEATHER kneels on the seat behind them; SILVERMAN sits on the far armrest; SLICKED sits on the travertine table beside the sofa. Nobody stands behind the sofa. The desk stands on the crossing nearer the camera, lower right. Camera C1 on the near sidewalk corner.",
  [P("L", 1.35, -2.0, "sit", 270, "sits, road end"), P("H", 1.0, -2.0, "sit", 270, "sits beside L"), P("FE", 1.35, -1.2, "kneel", 270, "on the seat"), P("SM", 1.4, -0.3, "sit", 270, "on the armrest"), SL_home],
  CAM(-2.98, -8.87, (1.2, -2.0), z=1.8, pitch=-7.7, note="C1 · wide on the sofa")),
 ("S1b", "They stand and walk toward the camera; camera backs up",
  "S1b 0:00.8  LEADER and HERO are up and walking along the stripes from the sofa toward the desk and the lens, HERO glued to LEADER's right, magazine open over her face. They stay inside the lane between the sofa's road end and the desk; the sofa is one step behind them, the desk one step ahead. Camera walks BACKWARD on the near sidewalk.",
  [P("L", 1.35, -2.9, "stand", 270, "walking, eyes on lens"), P("H", 0.8, -2.85, "stand", 270, "magazine over face"), FE_home, SM_home, SL_home],
  CAM(-3.2, -9.2, (1.2, -3.0), z=1.8, pitch=-7, roll=2, note="C1→C2 · walking backward")),
 ("S2a", "At the desk; LEADER starts her line",
  "S2a 0:02  They stop at the desk's sofa-side end: HERO's right hip almost touches the desk corner, LEADER one step to her left (camera-right). Both face the lens; both on the stripes. LEADER: 'Still paying Higgsfield for this?' Crew soft on the sofa behind them.",
  [P("L", 1.45, -3.45, "stand", 270, "faces lens, speaking"), P("H", 0.95, -3.4, "stand", 270, "at the desk corner, looks at L"), FE_home, SM_home, SL_home],
  CAM(-2.98, -8.87, (1.2, -3.4), z=1.8, pitch=-7.7, note="C2 · medium two-shot")),
 ("S2b", "Push-in on LEADER",
  "S2b 0:03  While LEADER speaks the camera walks in to 0.8 m: her face and upper body fill the frame, focus on her eyes. HERO a soft shape at the frame edge, looking at LEADER.",
  [P("L", 1.45, -3.45, "stand", 270, "close-up"), P("H", 0.95, -3.4, "stand", 270, "soft, edge"), FE_home, SM_home, SL_home],
  CAM(1.2, -4.9, (1.45, -3.45), z=1.5, pitch=2, note="C2+ · close on LEADER")),
 ("S3a", "HERO speaks; camera turns to her",
  "S3a 0:04.5  HERO's lines. Camera whips from LEADER to HERO and holds. HERO looks lens → LEADER → lens; LEADER watches HERO, hand on her shoulder. Same marks as S2a.",
  [P("L", 1.45, -3.45, "stand", 230, "watches H"), P("H", 0.95, -3.4, "stand", 270, "speaking to lens"), FE_home, SM_home, SL_home],
  CAM(-2.98, -8.87, (0.95, -3.4), z=1.8, pitch=-7.7, note="C2 · on HERO")),
 ("S3b", "Camera walks round to LEADER's left",
  "S3b 0:07  Still HERO's line; nobody moves. The camera man walks round to LEADER's LEFT (camera-right side), 1 m from her. Foreground: LEADER's left shoulder, sleeve and the back of her bob, soft. HERO talking beyond her; the sofa and crew behind.",
  [P("L", 1.45, -3.45, "stand", 250, "fg shoulder"), P("H", 0.95, -3.4, "stand", 280, "talking"), FE_home, SM_home, SL_home],
  CAM(2.5, -4.1, (0.95, -3.4), z=1.5, pitch=0, roll=3, note="C3 · arriving, over L's shoulder")),
 ("S4", "LEADER turns her head and speaks side-on",
  "S4 0:10  LEADER keeps her body toward the lens's old position and turns her head over her LEFT shoulder to the camera beside her: three-quarter profile, chest-up, sly proud half-smile. HERO behind her, soft, smiling at her.",
  [P("L", 1.45, -3.45, "stand", 330, "head turned to lens"), P("H", 0.95, -3.4, "stand", 300, "soft, smiling at L"), FE_home, SM_home, SL_home],
  CAM(2.55, -3.9, (1.45, -3.45), z=1.5, pitch=1, note="C3 · side-on close-up")),
 ("S5a", "Behind LEADER: over her left shoulder onto the laptop",
  "S5a 0:11.5  LEADER steps to the desk's sofa-side end, lifts the laptop and holds it at chest height, screen toward her (toward the sofa side), lid toward the road. Her BACK is to the sofa. The camera man steps in BEHIND her, between her and the sofa, slightly to her left: back of her bob, left ear edge, left shoulder and sleeve large and soft on the right of frame; the glowing screen past her shoulder. HERO on her right, leaning in. No face.",
  [P("L", 1.35, -3.55, "stand", 270, "back to camera, laptop in hands"), P("H", 0.85, -3.6, "stand", 290, "leans in"), FE_home, SM_home, SL_home],
  CAM(1.75, -2.5, (1.3, -3.9), z=1.55, pitch=-18, note="C4 · behind her, over the left shoulder")),
 ("S5b", "Push past her shoulder to the screen",
  "S5b 0:12.5  From behind her the camera pushes forward past her left shoulder until the plain glowing screen fills most of the frame; her bob and shoulder slide out of frame on the right. Still no face. Beyond the screen: her hands, the desk top, the stripes and the road.",
  [P("L", 1.35, -3.55, "stand", 270, "back of head, soft"), P("H", 0.85, -3.6, "stand", 290, "")],
  CAM(1.6, -3.0, (1.3, -3.9), z=1.35, pitch=-14, note="C4+ · screen fills frame")),
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
