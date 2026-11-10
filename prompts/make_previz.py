import sys; sys.path.insert(0,'/home/claude')
import previz as pv, shotdiagrams as sd
from PIL import Image, ImageDraw
beats={b[0]:b for b in sd.SHOTS}; W,H=2752,1536; P=sd.P; FE=sd.FE_home; SM=sd.SM_home; SL=sd.SL_home
out='/home/claude/treg-ugc-assets/blocking/previz/'
def pxy(X,Y,Z): return pv.px(pv.PLATE_CAM,X,Y,Z,W,H)
for k in ['S1a','S1b','S2a','S3a']:
    pv.render(beats[k][3], out=out+f'{k}.jpg', label=f'{k}  stand-ins: grey = people (name on body), coloured = furniture')
def crop_render(people, centre, wf, name, label):
    im=pv.render(people); cx,cy=centre; w=int(W*wf); h=int(w*9/16)
    x0=int(min(max(cx-w/2,0),W-w)); y0=int(min(max(cy-h/2,0),H-h))
    c=im.crop((x0,y0,x0+w,y0+h)).resize((W,H),Image.LANCZOS)
    ImageDraw.Draw(c).text((20,20),label,fill='white',font=pv.FONT,stroke_width=3,stroke_fill='black'); c.save(out+name,quality=92)
Lh=pxy(1.45,-3.45,1.55); Hh=pxy(0.95,-3.4,1.6)
crop_render([P("L",1.45,-3.45,"stand",270),P("H",0.95,-3.4,"stand",270),FE,SM,SL],(Lh[0],Lh[1]+210),0.30,'S2b.jpg','S2b  push-in on LEADER')
crop_render([P("L",1.45,-3.45,"stand",230),P("H",0.95,-3.4,"stand",270),FE,SM,SL],((Lh[0]+Hh[0])/2,Hh[1]+260),0.42,'S3b.jpg','S3b  tighter: HERO talking, LEADER watching')
crop_render([P("L",1.45,-3.45,"stand",270),P("H",0.95,-3.4,"stand",300),FE,SM,SL],(Lh[0],Lh[1]+230),0.34,'S4.jpg','S4  close on LEADER, head turned')
