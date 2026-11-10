import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Wedge, FancyArrowPatch, Polygon

# Map frame (metres, y up): road y<0, curb y=0, sidewalk 0..5, building y>5.
fig, ax = plt.subplots(figsize=(13, 11), dpi=150)
ax.set_xlim(-2.0, 8.0)
ax.set_ylim(-4.6, 6.2)
ax.set_aspect("equal")
ax.axis("off")

ax.add_patch(Rectangle((-2, -4.6), 10, 4.6, color="#5f6368"))        # road
ax.add_patch(Rectangle((-2, 0), 10, 5, color="#d9d4cc"))             # sidewalk
ax.add_patch(Rectangle((-2, 5), 10, 1.2, color="#a89f91"))           # building
for i in range(5):
    ax.add_patch(Rectangle((-1.7 + i * 2.0, 5.0), 1.3, 0.3, color="#3b3a36"))
ax.plot([-2, 8], [0, 0], color="#888", lw=3)
for i in range(8):                                                   # zebra stripes, run across the road
    ax.add_patch(Rectangle((-1.2 + i * 0.6, -4.5), 0.32, 4.35, color="#efefef", alpha=.85, zorder=1))
ax.text(7.8, 5.6, "BUILDING (shop windows)", ha="right", va="center", fontsize=9)
ax.text(7.8, 4.4, "SIDEWALK", ha="right", fontsize=9, color="#555")
ax.text(7.8, -0.35, "CURB", ha="right", fontsize=8, color="#ddd")
ax.text(7.8, -4.3, "ROAD", ha="right", fontsize=9, color="#ddd")
ax.text(-1.2, -4.75, "zebra crossing", fontsize=8, color="#333")

def rot_rect(cx, cy, w, h, ang, **kw):
    a = math.radians(ang)
    pts = [(cx + dx*math.cos(a) - dy*math.sin(a), cy + dx*math.sin(a) + dy*math.cos(a))
           for dx, dy in [(-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2)]]
    ax.add_patch(Polygon(pts, closed=True, zorder=2, **kw))

# furniture
rot_rect(1.2, -1.25, 0.95, 2.3, 0, fc="#efe8da", ec="#9a8f7a", lw=1.5)      # sofa, perpendicular to curb, end touching it
ax.add_patch(Rectangle((0.72, -2.4), 0.2, 2.3, fc="#d8cfbd", ec="#9a8f7a", zorder=2))  # sofa back (road-crossing side)
ax.text(1.25, -1.25, "SOFA", ha="center", va="center", fontsize=8, rotation=90, zorder=3)
ax.add_patch(Circle((2.3, -1.3), 0.38, fc="#e7dcc6", ec="#9a8f7a", lw=1.2, zorder=2))
ax.text(2.3, -1.3, "table", ha="center", va="center", fontsize=6.5, zorder=3)
rot_rect(4.3, 1.5, 1.9, 0.75, 30, fc="#d6b98c", ec="#7a6240", lw=1.5)      # desk on the sidewalk, 30 deg
ax.text(4.35, 1.5, "DESK", ha="center", va="center", fontsize=7.5, rotation=30, zorder=3)
rot_rect(3.8, 1.25, 0.42, 0.3, 30, fc="#c9cdd2", ec="#333", lw=1)          # laptop
ax.text(3.35, 0.55, "laptop", fontsize=6.5)
ax.add_patch(Circle((4.95, 1.85), 0.12, fc="#111", zorder=3))               # lamp
ax.add_patch(Circle((5.5, 0.75), 0.28, fc="#b07a46", ec="#5a3b1e", zorder=2))
ax.text(5.85, 0.75, "chair", fontsize=6.5, va="center")
ax.annotate("", xy=(1.68, 0.08), xytext=(3.42, 1.0), arrowprops=dict(arrowstyle="<->", color="#444", lw=1))
ax.text(2.25, 0.65, "≈2 m", fontsize=8, color="#333")

def person(x, y, label, col, r=0.24, txt="white"):
    ax.add_patch(Circle((x, y), r, fc=col, ec="black", lw=0.8, zorder=6))
    ax.text(x, y, label, ha="center", va="center", fontsize=7, color=txt, zorder=7, weight="bold")

ax.add_patch(Circle((1.3, -1.6), 1.65, fill=False, ls="--", ec="#7a6aa8", lw=1.2, zorder=3))
ax.text(3.1, -3.4, "crew zone: hop around\nthe sofa, stay in the ring", fontsize=7.5, color="#e9e3ff")
person(1.35, -2.0, "FE", "#a58fd6")
person(1.3, -2.9, "SM", "#9aa3ad")
person(0.25, -1.4, "SL", "#c7b9a6", txt="black")

LEADER, HERO, CAM = "#222222", "#e8d27a", "#d2452c"
person(1.35, -0.55, "L1", LEADER)          # seated on the sofa, curb end
person(1.35, -1.25, "H1", HERO, txt="black")
person(3.0, 2.4, "L2", LEADER)
person(3.6, 1.7, "H2", HERO, txt="black")
person(3.1, 2.0, "L3", LEADER, r=0.17)
person(2.7, 1.35, "H3", HERO, r=0.2, txt="black")

def arrow(p, q, col, ls="-", lw=2, rad=0.0, z=5):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=14, color=col, lw=lw, ls=ls,
                                 connectionstyle=f"arc3,rad={rad}", zorder=z))

arrow((1.6, -0.45), (2.8, 2.15), LEADER, rad=-0.15)
arrow((1.6, -1.15), (3.4, 1.45), "#b89a20", rad=-0.1)

def cam(x, y, face_deg, label, note, nx, ny):
    ax.add_patch(Wedge((x, y), 1.0, face_deg - 22, face_deg + 22, fc=CAM, alpha=.15, zorder=4))
    ax.add_patch(Rectangle((x - 0.14, y - 0.14), 0.28, 0.28, fc=CAM, ec="black", lw=.8, zorder=8))
    ax.text(nx, ny, f"{label}  {note}", fontsize=7.3, color="#8a2414", weight="bold", zorder=9)

cam(3.0, 0.35, -150, "C1", "arrives, faces the sofa", 3.2, 0.1)
cam(4.6, 3.6, -143, "C2", "backed up; L or H as each speaks", 4.75, 3.65)
cam(3.65, 2.9, -143, "C2+", "push-in, leader", 3.95, 3.05)
cam(2.4, 3.2, -53, "C3", "leader's LEFT", 0.8, 3.55)
cam(3.25, 2.65, -62, "C4", "over left shoulder", 1.35, 2.55)
arrow((3.05, 0.55), (4.45, 3.4), CAM, ls="--", lw=1.6, rad=-0.35)
ax.text(4.85, 2.55, "camera walks BACKWARD,\nslips past the desk end", fontsize=6.8, color=CAM)
arrow((4.45, 3.75), (2.6, 3.4), CAM, ls="--", lw=1.4, rad=0.3)
arrow((2.55, 3.0), (3.1, 2.75), CAM, ls="--", lw=1.2, rad=-0.3)
arrow((3.3, 2.45), (3.72, 1.45), CAM, ls=":", lw=1.4)

fig.text(0.02, 0.975, "treg hook — blocking map v5 (top view, metres)", fontsize=13, weight="bold", va="top")
fig.text(0.98, 0.975, "L leader · H hero · FE feather · SM silverman · SL slicked · red = camera", fontsize=8.5, ha="right", va="top")
beats = [
    "B1  L and H are sitting on the sofa with the crew. C1 arrives; they stand up, step onto the curb and walk to the desk; camera walks backward to C2.",
    "B2  At the desk (L2/H2). LEADER speaks to the lens; camera pushes in to C2+.",
    "B3  HERO speaks: camera pans to her, then walks round to C3, the leader's LEFT.",
    "B4  LEADER turns her head left and speaks to C3 side-on.",
    "B5  LEADER steps to the laptop (L3), HERO to H3; camera to C4, over her left shoulder, pushes into the screen.",
    "Sofa sits on the zebra crossing, perpendicular to the curb, one end touching it. Desk on the sidewalk, ≈2 m away. Crew stay around the sofa.",
]
fig.text(0.02, 0.015, "\n".join(beats), fontsize=8.6, va="bottom",
         bbox=dict(fc="white", ec="#999", boxstyle="round,pad=0.5"))
plt.subplots_adjust(left=0.01, right=0.99, top=0.95, bottom=0.14)
plt.savefig("/home/claude/treg-ugc-assets/blocking_v5.png")
print("ok")
