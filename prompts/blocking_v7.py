import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Wedge, FancyArrowPatch, Polygon

# Map frame (metres, y up): road y<0, curb y=0, sidewalk 0..5, building y>5.
fig, ax = plt.subplots(figsize=(13, 11), dpi=150)
ax.set_xlim(-2.0, 7.5)
ax.set_ylim(-4.6, 4.2)
ax.set_aspect("equal")
ax.axis("off")

ax.add_patch(Rectangle((-2, -4.6), 10, 4.6, color="#5f6368"))        # road
ax.add_patch(Rectangle((-2, 0), 10, 3, color="#d9d4cc"))             # sidewalk
ax.add_patch(Rectangle((-2, 3), 10, 1.2, color="#a89f91"))           # building
for i in range(5):
    ax.add_patch(Rectangle((-1.7 + i * 2.0, 3.0), 1.3, 0.3, color="#3b3a36"))
ax.plot([-2, 8], [0, 0], color="#888", lw=3)
# zebra crossing: a 6 m wide band running straight out from the curb across the road
# (perpendicular to the sidewalk); stripes lie parallel to the curb
ax.add_patch(Rectangle((-0.3, -4.6), 6.3, 4.6, fill=False, ec="#cfcfcf", ls=":", lw=1, zorder=1))
for i in range(8):
    ax.add_patch(Rectangle((-0.3, -0.55 - i * 0.6), 6.3, 0.32, color="#efefef", alpha=.8, zorder=1))
ax.text(7.3, 3.7, "BUILDING (shop windows)", ha="right", va="center", fontsize=9)
ax.text(7.3, 2.5, "SIDEWALK", ha="right", fontsize=9, color="#555")
ax.text(7.3, -0.35, "CURB", ha="right", fontsize=8, color="#ddd")
ax.text(7.3, -4.3, "ROAD", ha="right", fontsize=9, color="#ddd")
ax.text(-1.9, -2.3, "zebra crossing\n(runs straight\nacross the road,\nperpendicular to\nthe sidewalk)", fontsize=7.5, color="#eee")

def rot_rect(cx, cy, w, h, ang, **kw):
    a = math.radians(ang)
    pts = [(cx + dx*math.cos(a) - dy*math.sin(a), cy + dx*math.sin(a) + dy*math.cos(a))
           for dx, dy in [(-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2)]]
    ax.add_patch(Polygon(pts, closed=True, zorder=2, **kw))

# furniture (both on the zebra crossing, touching the curb)
rot_rect(1.2, -1.25, 0.95, 2.3, 0, fc="#efe8da", ec="#9a8f7a", lw=1.5)      # sofa, perpendicular to curb, end touching it
ax.add_patch(Rectangle((0.72, -2.4), 0.2, 2.3, fc="#d8cfbd", ec="#9a8f7a", zorder=2))
ax.text(1.25, -1.25, "SOFA", ha="center", va="center", fontsize=8, rotation=90, zorder=3)
ax.add_patch(Circle((1.2, -3.0), 0.36, fc="#e7dcc6", ec="#9a8f7a", lw=1.2, zorder=2))
ax.text(1.2, -3.0, "table", ha="center", va="center", fontsize=6.5, zorder=3)
rot_rect(4.2, -0.8, 1.9, 0.75, -30, fc="#d6b98c", ec="#7a6240", lw=1.5)    # desk on the crossing, near end at the curb
ax.text(4.25, -0.85, "DESK", ha="center", va="center", fontsize=7.5, rotation=-30, zorder=3)
rot_rect(3.72, -0.6, 0.32, 0.44, 0, fc="#c9cdd2", ec="#333", lw=1)        # laptop on the near end
ax.plot([3.56, 3.56], [-0.82, -0.38], color="#2b6cb0", lw=3, zorder=4)     # screen edge, facing the sofa
ax.annotate("", xy=(3.15, -0.6), xytext=(3.55, -0.6), arrowprops=dict(arrowstyle="-|>", color="#2b6cb0", lw=1.5), zorder=4)
ax.text(3.45, -1.25, "screen faces\nthe sofa", fontsize=6.5, color="#2b6cb0", zorder=4)
ax.text(3.85, -0.3, "laptop", fontsize=6.5)
ax.add_patch(Circle((4.85, -1.2), 0.12, fc="#111", zorder=3))
ax.add_patch(Circle((5.45, -0.55), 0.28, fc="#b07a46", ec="#5a3b1e", zorder=2))
ax.text(5.15, -0.15, "chair", fontsize=6.5, va="center", color="#333")
ax.annotate("", xy=(1.72, -0.4), xytext=(3.38, -0.4), arrowprops=dict(arrowstyle="<->", color="#333", lw=1))
ax.text(2.3, -0.32, "≈2 m", fontsize=8, color="#333")

def person(x, y, label, col, r=0.24, txt="white"):
    ax.add_patch(Circle((x, y), r, fc=col, ec="black", lw=0.8, zorder=6))
    ax.text(x, y, label, ha="center", va="center", fontsize=7, color=txt, zorder=7, weight="bold")

ax.add_patch(Circle((1.1, -1.7), 1.75, fill=False, ls="--", ec="#b9aef0", lw=1.2, zorder=3))
ax.text(2.9, -3.3, "crew zone: hop around\nthe sofa, stay in the ring", fontsize=7.5, color="#e9e3ff")
person(1.35, -2.0, "FE", "#a58fd6")
person(1.95, -2.75, "SM", "#9aa3ad")
person(0.25, -1.4, "SL", "#c7b9a6", txt="black")

LEADER, HERO, CAM = "#222222", "#e8d27a", "#d2452c"
person(1.35, -0.55, "L1", LEADER)
person(1.35, -1.25, "H1", HERO, txt="black")
person(2.45, -0.45, "L2", LEADER)
person(3.0, -0.2, "H2", HERO, txt="black")
person(3.2, -0.75, "L3", LEADER, r=0.17)
person(3.15, -1.25, "H3", HERO, r=0.17, txt="black")

def arrow(p, q, col, ls="-", lw=2, rad=0.0, z=5):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=14, color=col, lw=lw, ls=ls,
                                 connectionstyle=f"arc3,rad={rad}", zorder=z))

arrow((1.6, -0.5), (2.2, -0.45), LEADER, lw=1.8)
arrow((1.6, -1.2), (2.85, -0.4), "#b89a20", lw=1.8, rad=0.2)

def cam(x, y, face_deg, label, note, nx, ny):
    ax.add_patch(Wedge((x, y), 1.0, face_deg - 22, face_deg + 22, fc=CAM, alpha=.15, zorder=4))
    ax.add_patch(Rectangle((x - 0.14, y - 0.14), 0.28, 0.28, fc=CAM, ec="black", lw=.8, zorder=8))
    ax.text(nx, ny, f"{label}  {note}", fontsize=7.3, color="#8a2414", weight="bold", zorder=9)

cam(2.3, 1.3, -113, "C1", "arrives, faces the sofa", 0.25, 1.25)
cam(3.9, 1.65, -118, "C2", "backed up; L or H as each speaks", 4.1, 1.75)
cam(3.13, 0.25, -118, "C2+", "push-in, leader", 3.45, 0.5)
cam(1.95, 0.15, -41, "C3", "leader's LEFT, at the curb", -0.25, 0.1)
cam(2.45, 0.25, -35, "C4", "over left shoulder", 0.35, 0.6)
arrow((2.45, 1.38), (3.72, 1.6), CAM, ls="--", lw=1.6)
ax.text(2.55, 1.6, "walks BACKWARD", fontsize=6.8, color=CAM, rotation=8)
arrow((3.7, 1.75), (2.05, 0.35), CAM, ls="--", lw=1.4, rad=0.35)
arrow((2.1, 0.3), (2.35, 0.3), CAM, ls="--", lw=1.2)
arrow((2.6, 0.15), (3.45, -0.5), CAM, ls=":", lw=1.4)

fig.text(0.02, 0.975, "treg hook — blocking map v7 (top view, metres)", fontsize=13, weight="bold", va="top")
fig.text(0.98, 0.975, "L leader · H hero · FE feather · SM silverman · SL slicked · red = camera", fontsize=8.5, ha="right", va="top")
beats = [
    "B1  L and H are sitting on the sofa with the crew. C1 arrives on the sidewalk; they stand up and walk the ~2 m along the curb to the desk; camera walks backward to C2.",
    "B2  At the desk (L2/H2). LEADER speaks to the lens; camera pushes in to C2+.",
    "B3  HERO speaks: camera pans to her, then walks round to C3, the leader's LEFT.",
    "B4  LEADER turns her head left and speaks to C3 side-on.",
    "B5  LEADER steps round to face the laptop screen (L3), HERO stays at her right (H3); camera to C4, over her left shoulder, pushes into the screen.",
    "Sofa AND desk on the zebra crossing at the curb, ≈2 m apart. Laptop screen faces the sofa. HERO is ALWAYS right beside LEADER, on her right. Crew stay around the sofa.",
]
fig.text(0.02, 0.015, "\n".join(beats), fontsize=8.6, va="bottom",
         bbox=dict(fc="white", ec="#999", boxstyle="round,pad=0.5"))
plt.subplots_adjust(left=0.01, right=0.99, top=0.95, bottom=0.14)
plt.savefig("/home/claude/treg-ugc-assets/blocking_v7.png")
print("ok")
