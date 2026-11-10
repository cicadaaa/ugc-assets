import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont
W,H=1920,1080
def key(path, lo=18, hi=60):
    im=np.asarray(Image.open(path).convert('RGB')).astype(np.float32)
    r,g,b=im[...,0],im[...,1],im[...,2]
    d=g-np.maximum(r,b)
    a=1-np.clip((d-lo)/(hi-lo),0,1)
    g2=np.minimum(g,(r+b)/2+3)           # despill
    out=np.dstack([r,g2,b,a*255]).astype(np.uint8)
    im=Image.fromarray(out,'RGBA')
    al=im.getchannel('A').filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2)); im.putalpha(al)
    return im
BG=Image.open('raw_BG.jpg').convert('RGB'); BW,BH=BG.size
def bg(cx,cy,wf,blur):
    w=int(BW*wf); h=int(w*9/16); x0=int(min(max(cx*BW-w/2,0),BW-w)); y0=int(min(max(cy*BH-h/2,0),BH-h))
    return BG.crop((x0,y0,x0+w,y0+h)).resize((W,H),Image.LANCZOS).filter(ImageFilter.GaussianBlur(blur))
DESK=key('raw_DESK.jpg'); bb=DESK.getchannel('A').point(lambda v:255 if v>128 else 0).getbbox(); DESK=DESK.crop(bb); print('desk',DESK.size)
def comp(name, fg, bgp, desk=None, grain=True):
    c=bg(*bgp).convert('RGBA')
    if desk:
        s,x,y,bl=desk; d=DESK.resize((int(DESK.width*s),int(DESK.height*s)),Image.LANCZOS).filter(ImageFilter.GaussianBlur(bl)); c.alpha_composite(d,(x,y))
    f=key(fg).resize((W,H),Image.LANCZOS); c.alpha_composite(f)
    c=c.convert('RGB')
    if grain:
        a=np.asarray(c).astype(np.float32); a+=np.random.normal(0,3.0,a.shape[:2]+(1,)); c=Image.fromarray(np.clip(a,0,255).astype(np.uint8))
    c.save(name,quality=92); return c
# bg params: centre x,y (fraction of plate), width fraction, blur px
B={ 'K01':(0.40,0.40,0.46,4),'K02':(0.42,0.38,0.40,8),'K03':(0.42,0.38,0.40,8),'K04':(0.38,0.38,0.46,7),'K05':(0.40,0.40,0.54,5),
    'K06':(0.42,0.40,0.60,5),'K07':(0.36,0.40,0.60,5),'K08':(0.36,0.40,0.60,5),'K09':(0.32,0.40,0.56,6)}
D={ 'K06':(1.25,1330,470,1.5),'K07':(1.25,1420,470,1.5),'K08':(1.25,1420,470,1.5),'K09':(1.3,1380,450,1.5)}
import sys
for k in B: comp(f'{k}.jpg', f'raw_{k}.jpg', B[k], D.get(k))
