import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Wedge, FancyArrowPatch, Polygon

# Map frame (metres, y up): road y<0, curb y=0, sidewalk 0..6, building y>6.
# The pair walks +x (sofa -> desk). Facing +x: LEFT = building side (+y), RIGHT = road side (-y).

fig, ax = plt.subplots(figsize=(16, 9.5), dpi=150)
ax.set_xlim(-1.5, 15)
ax.set_ylim(-3.2, 7.8)
ax.set_aspect("equal")
ax.axis("off")

# ground
ax.add_patch(Rectangle((-1.5, -3.2), 16.5, 3.2, color="#5f6368"))            # road
ax.add_patch(Rectangle((-1.5, 0), 16.5, 6, color="#d9d4cc"))                 # sidewalk
ax.add_patch(Rectangle((-1.5, 6), 16.5, 1.8, color="#a89f91"))               # building
for i in range(0, 16, 2):
    ax.add_patch(Rectangle((i - 1.3, 6.0), 1.4, 0.35, color="#3b3a36"))      # shop windows
ax.plot([-1.5, 15], [0, 0], color="#888", lw=3)                              # curb
for i in range(7):                                                           # zebra crossing (decor, not used)
    ax.add_patch(Rectangle((-1.2 + i * 0.55, -3.0), 0.3, 2.8, color="#f2f2f2", alpha=.9))
ax.text(14.8, 6.9, "BUILDING  (carved stone, shop windows)", ha="right", va="center", fontsize=9, color="#222")
ax.text(14.8, 5.3, "SIDEWALK  (6 m wide)", ha="right", fontsize=9, color="#555")
ax.text(14.8, -0.35, "CURB", ha="right", fontsize=8, color="#ddd")
ax.text(14.8, -2.8, "ROAD", ha="right", fontsize=9, color="#ddd")
ax.text(2.8, -2.9, "zebra crossing (background only)", fontsize=8, color="#eee")

def rot_rect(cx, cy, w, h, ang, **kw):
    a = math.radians(ang)
    pts = []
    for dx, dy in [(-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2)]:
        pts.append((cx + dx*math.cos(a) - dy*math.sin(a), cy + dx*math.sin(a) + dy*math.cos(a)))
    ax.add_patch(Polygon(pts, closed=True, **kw))

# furniture (fixed)
rot_rect(2.0, 3.6, 2.3, 0.95, 0, fc="#efe8da", ec="#9a8f7a", lw=1.5)          # sofa, back to building, facing road
ax.text(2.0, 3.6, "SOFA\n(fixed, mid-sidewalk)", ha="center", va="center", fontsize=8)
ax.add_patch(Circle((2.0, 2.45), 0.38, fc="#e7dcc6", ec="#9a8f7a", lw=1.2))   # travertine table
ax.text(2.0, 2.45, "table", ha="center", va="center", fontsize=6.5)
rot_rect(11.2, 0.0, 1.9, 0.75, 30, fc="#d6b98c", ec="#7a6240", lw=1.5)        # desk straddling the curb, 30 deg
ax.text(12.6, -0.75, "OAK DESK 30°\nhalf on sidewalk,\nhalf on road", fontsize=7.5, color="white")
ax.add_patch(Rectangle((10.55, 0.05), 0.42, 0.3, angle=30, fc="#c9cdd2", ec="#333", lw=1))  # laptop (sidewalk half)
ax.text(10.15, -0.5, "laptop", fontsize=6.5, color="white")
ax.add_patch(Circle((11.85, 0.15), 0.12, fc="#111"))                            # dome lamp
ax.add_patch(Circle((12.4, 1.15), 0.28, fc="#b07a46", ec="#5a3b1e"))            # tan chair
ax.text(12.75, 1.15, "chair", fontsize=6.5, va="center")

def person(x, y, label, col, r=0.24, fs=7, txt="white"):
    ax.add_patch(Circle((x, y), r, fc=col, ec="black", lw=0.8, zorder=5))
    ax.text(x, y, label, ha="center", va="center", fontsize=fs, color=txt, zorder=6, weight="bold")

# background crew: home marks relative to the sofa, they hop around within the dashed ring
ax.add_patch(Circle((2.0, 3.4), 2.0, fill=False, ls="--", ec="#7a6aa8", lw=1.2))
ax.text(-0.9, 5.65, "crew zone: they hop around the sofa,\nnever leave this ring", fontsize=7.5, color="#5b4a8a")
person(1.3, 3.75, "FE", "#a58fd6")     # feather: kneeling/bouncing on left seat
person(3.45, 3.95, "SM", "#9aa3ad")    # silverman: on the right arm, hops off/on
person(2.0, 4.65, "SL", "#c7b9a6", txt="black")  # slicked: behind the sofa back

# pair start marks
LEADER, HERO = "#222222", "#e8d27a"
person(3.6, 2.85, "L1", LEADER)
person(3.6, 1.95, "H1", HERO, txt="black")
# pair end marks at the desk
person(8.6, 2.6, "L2", LEADER)
person(8.6, 1.6, "H2", HERO, txt="black")
person(9.8, 1.25, "L3", LEADER)      # leader steps to the laptop
person(8.95, 0.75, "H3", HERO, txt="black")

def arrow(p, q, col, ls="-", lw=2, rad=0.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=14, color=col, lw=lw, ls=ls,
                                 connectionstyle=f"arc3,rad={rad}", zorder=4))

arrow((3.9, 2.85), (8.3, 2.62), LEADER)
arrow((3.9, 1.95), (8.3, 1.62), "#b89a20")
arrow((8.8, 2.4), (9.6, 1.45), LEADER, lw=1.5)
arrow((8.7, 1.38), (8.85, 1.0), "#b89a20", lw=1.2)

# camera path (walks BACKWARD, facing the pair)
CAM = "#d2452c"
def cam(x, y, face_deg, label, note=None, dx=0.0, dy=0.42):
    ax.add_patch(Wedge((x, y), 1.35, face_deg - 22, face_deg + 22, fc=CAM, alpha=.16, zorder=3))
    ax.add_patch(Rectangle((x - 0.17, y - 0.17), 0.34, 0.34, fc=CAM, ec="black", lw=.8, zorder=6))
    ax.text(x + dx, y + dy, label, ha="center", fontsize=8, color=CAM, weight="bold", zorder=7)
    if note:
        ax.text(x + dx, y + dy + 0.32, note, ha="center", fontsize=6.8, color="#7a2214", zorder=7)

cam(5.6, 2.45, 180, "C1", "arrives, faces the crew")
cam(11.2, 2.3, 180, "C2", "backed up; on L / H as each speaks", dx=1.2, dy=0.45)
cam(9.6, 2.65, 182, "C2+", "push-in, leader's face", dx=0.2, dy=0.4)
cam(8.6, 3.95, -90, "C3", "leader's LEFT, she turns her head", dx=0.0, dy=0.35)
cam(10.05, 2.1, -60, "C4", "rear-left, over her shoulder", dx=1.75, dy=-0.55)
arrow((5.9, 2.45), (10.9, 2.3), CAM, ls="--", lw=1.6)
ax.text(6.3, 2.15, "camera walks BACKWARD", ha="center", fontsize=7.5, color=CAM)
arrow((11.0, 2.6), (8.9, 3.95), CAM, ls="--", lw=1.4, rad=0.3)
arrow((8.9, 3.75), (9.85, 2.3), CAM, ls="--", lw=1.4, rad=-0.25)
arrow((10.15, 1.9), (10.55, 0.55), CAM, ls=":", lw=1.4)
ax.text(10.7, 1.0, "push to\nscreen", fontsize=6.5, color=CAM)

# legend / beats
beats = [
    "BEATS (camera always on LEADER unless HERO is speaking)",
    "B1  Crew + L1/H1 around the sofa. C1 arrives. L & H walk toward the lens; camera backs up to C2.",
    "B2  At the desk (L2/H2). LEADER speaks to the lens: camera pushes in to C2+ (face + upper body).",
    "B3  HERO speaks: camera turns to her (eyes lens <-> leader), then walks round to C3, leader's LEFT.",
    "B4  LEADER turns her head left and speaks to C3 in profile / three-quarter.",
    "B5  LEADER steps to the laptop (L3), HERO to H3. Camera to C4, over her left shoulder, pushes into the screen.",
]
for i, t in enumerate(beats):
    ax.text(-1.3, 7.55 - 0.0 - i * 0.0, "", fontsize=1)
fig.text(0.02, 0.025, "\n".join(beats), fontsize=9, va="bottom", family="DejaVu Sans",
         bbox=dict(fc="white", ec="#999", boxstyle="round,pad=0.5"))
fig.text(0.02, 0.97, "treg hook — blocking map v4 (top view, metres, fixed marks)", fontsize=13, weight="bold", va="top")
fig.text(0.98, 0.97, "L = leader (bob, yukata)   H = hero (platinum)   FE feather · SM silverman · SL slicked   red = camera",
         fontsize=8.5, ha="right", va="top")
plt.subplots_adjust(left=0.01, right=0.99, top=0.93, bottom=0.17)
plt.savefig("/home/claude/treg-ugc-assets/blocking_v4.png")
print("ok")
