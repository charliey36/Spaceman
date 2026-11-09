import json, sys, subprocess, math, glob, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FPS=30; OW,OH=1080,1920
CW,CH=864,1536; CX=(OW-CW)//2; CY=292; RAD=50
ease=lambda x: 0.5-0.5*math.cos(math.pi*max(0,min(1,x)))
SC=json.load(open('t2.json')); CAPS_SPEC=json.load(open('c2.json')); OV=json.load(open('o2.json'))
FILES={s['dir']:sorted(glob.glob(f"c3/{s['dir']}/*.jpg")) for s in SC}
cache={}
def src(d,i):
    fs=FILES[d]; fn=fs[max(0,min(len(fs)-1,i))]
    if fn not in cache:
        if len(cache)>30: cache.clear()
        cache[fn]=Image.open(fn).convert('RGB')
    return cache[fn]
F_XB='/usr/share/fonts/opentype/inter/InterDisplay-ExtraBold.otf'; F_SB='/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf'; F_B='/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf'
NAMEC={'Megan':(255,143,177),'Connor':(124,182,255)}
def wrap(words, f, maxw):
    lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if f.getlength(t)>maxw and cur: lines.append(cur); cur=w
        else: cur=t
    lines.append(cur); return lines
def cap_img(txt):  # narration caption: big, white, soft shadow
    f=ImageFont.truetype(F_XB,58); lines=txt.split('\n'); lh=70
    ws=[f.getlength(l) for l in lines]; w=int(max(ws))+60; h=lh*len(lines)+40
    im=Image.new('RGBA',(w,h),(0,0,0,0)); sh=Image.new('RGBA',(w,h),(0,0,0,0)); sd=ImageDraw.Draw(sh); d=ImageDraw.Draw(im)
    for i,l in enumerate(lines):
        x=(w-ws[i])/2; sd.text((x,20+i*lh+4),l,font=f,fill=(0,0,0,200)); d.text((x,20+i*lh),l,font=f,fill=(255,255,255,255))
    sh=sh.filter(ImageFilter.GaussianBlur(8)); sh.alpha_composite(im); return sh
def pill_img(txt, size=40, font=F_SB):
    f=ImageFont.truetype(font,size); w=int(f.getlength(txt))+64; h=size+40
    im=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((0,0,w-1,h-1),radius=h//2,fill=(10,12,20,215),outline=(255,255,255,38),width=2)
    d.text((32,(h-size)/2-size*0.08),txt,font=f,fill=(255,255,255,255)); return im
def sub_img(name, txt):  # dialogue: speaker name in colour, line in white, dark rounded box
    fn=ImageFont.truetype(F_XB,44); ft=ImageFont.truetype(F_B,44); lh=56
    lines=[l for part in txt.split('\n') for l in wrap(part.split(), ft, 820)]; prefix=name+'  '
    pw=fn.getlength(prefix)
    widths=[ (pw if i==0 else 0)+ft.getlength(l) for i,l in enumerate(lines)]
    w=int(max(widths))+64; h=lh*len(lines)+36
    im=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((0,0,w-1,h-1),radius=28,fill=(10,12,20,225),outline=(255,255,255,34),width=2)
    for i,l in enumerate(lines):
        x=(w-widths[i])/2; y=18+i*lh-4
        if i==0: d.text((x,y),prefix,font=fn,fill=NAMEC.get(name,(255,255,255))+(255,)); x+=pw
        d.text((x,y),l,font=ft,fill=(255,255,255,255))
    return im
CAPS=[]
for c in CAPS_SPEC:
    img = cap_img(c['text']) if c['style']=='cap' else pill_img(c['text']) if c['style']=='label' else sub_img(c['name'], c['text'])
    CAPS.append((c,img))
mask=Image.new('L',(CW,CH),0); ImageDraw.Draw(mask).rounded_rectangle((0,0,CW-1,CH-1),radius=RAD,fill=255)
shadow=Image.new('RGBA',(OW,OH),(0,0,0,0)); ImageDraw.Draw(shadow).rounded_rectangle((CX-4,CY+14,CX+CW+4,CY+CH+26),radius=RAD+8,fill=(0,0,0,190)); shadow=shadow.filter(ImageFilter.GaussianBlur(30))
border=Image.new('RGBA',(OW,OH),(0,0,0,0)); ImageDraw.Draw(border).rounded_rectangle((CX,CY,CX+CW-1,CY+CH-1),radius=RAD,outline=(255,255,255,30),width=2)
yy,xx=np.mgrid[0:OH,0:OW]; vig=(1-0.6*np.clip(((xx-540)/780)**2+((yy-960)/1180)**2,0,1))[...,None].astype(np.float32)
TOTAL=SC[-1]['o1']
def zoom_at(s,t):
    k=s.get('zk')  # keyframes [[t_rel, z, fx, fy], ...]
    if not k: return 1.0,540,-1
    tr=t-s['o0']
    if tr<=k[0][0]: return k[0][1],k[0][2],k[0][3]
    for a,b in zip(k,k[1:]):
        if a[0]<=tr<=b[0]:
            p=ease((tr-a[0])/(b[0]-a[0])); return a[1]+(b[1]-a[1])*p, a[2]+(b[2]-a[2])*p, (a[3]+(b[3]-a[3])*p) if a[3]>=0 and b[3]>=0 else b[3]
    return k[-1][1],k[-1][2],k[-1][3]
def frame(t):
    s=next((x for x in SC if x['o0']<=t<x['o1']), SC[-1])
    i=int(round((t-s['o0'])*FPS))+s.get('off',0)
    im=src(s['dir'],i)
    z,fx,fy=zoom_at(s,t)
    if t-s['o0']<0.2 and s.get('punch',1): z*=1+0.03*(1-ease((t-s['o0'])/0.2))
    cw,ch=1080/z,1920/z
    x0=min(max(fx-cw/2,0),1080-cw); y0=0 if fy<0 else min(max(fy-ch/2,0),1920-ch)
    card=im.resize((CW,CH),Image.LANCZOS,box=(x0,y0,x0+cw,y0+ch)).convert('RGBA')
    # overlays in native coords (highlight ring)
    for o in OV:
        if o['t0']<=t<o['t1']:
            a=ease((t-o['t0'])/0.3)*ease((o['t1']-t)/0.25); pulse=0.5+0.5*math.sin((t-o['t0'])*2*math.pi*1.1)
            r=o['rect']; sx=CW/cw; sy=CH/ch
            rx=[(r[0]-x0)*sx,(r[1]-y0)*sy,(r[2]-x0)*sx,(r[3]-y0)*sy]; rad=int(22*sx)
            dim=Image.new('L',(CW,CH),int(150*a)); ImageDraw.Draw(dim).rounded_rectangle((rx[0]-6,rx[1]-6,rx[2]+6,rx[3]+6),radius=rad+6,fill=0)
            dim=dim.filter(ImageFilter.GaussianBlur(6))
            card=Image.composite(Image.new('RGBA',(CW,CH),(3,4,9,255)),card,dim)
            ov=Image.new('RGBA',(CW,CH),(0,0,0,0)); od=ImageDraw.Draw(ov); g=int(7+3*pulse)
            od.rounded_rectangle((rx[0]-g,rx[1]-g,rx[2]+g,rx[3]+g),radius=rad+g,outline=(255,255,255,int(240*a)),width=4)
            card.alpha_composite(ov.filter(ImageFilter.GaussianBlur(9))); card.alpha_composite(ov)
    bg=im.resize((54,96),Image.BILINEAR).filter(ImageFilter.GaussianBlur(3)).resize((OW,OH),Image.BICUBIC)
    bga=np.asarray(bg).astype(np.float32)*0.38*vig+np.array([5,6,12],np.float32)
    out=Image.fromarray(np.clip(bga,0,255).astype(np.uint8)).convert('RGBA')
    out.alpha_composite(shadow); out.paste(card,(CX,CY),mask); out.alpha_composite(border)
    for c,img in CAPS:
        if c['t0']<=t<c['t1']:
            a=ease((t-c['t0'])/0.15)*(ease((c['t1']-t)/0.12) if c.get('fadeout',1) else 1)
            sc=0.95+0.05*ease((t-c['t0'])/0.15)
            im2=img.resize((int(img.width*sc),int(img.height*sc)),Image.LANCZOS) if sc<0.999 else img
            if a<1: al=np.asarray(im2).copy(); al[...,3]=(al[...,3]*a).astype(np.uint8); im2=Image.fromarray(al)
            out.alpha_composite(im2,(int(540-im2.width/2), int(c['y']-im2.height/2)))
    # global fade from black at start / to black at the very end
    rgb=out.convert('RGB')
    pass
    return rgb
if __name__=='__main__':
    if len(sys.argv)>2 and sys.argv[1]=='still':
        for t in sys.argv[2:]: frame(float(t)).save(f'v2still_{t}.png')
        sys.exit()
    n=int(round(TOTAL*FPS))
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{OW}x{OH}','-r',str(FPS),'-i','-','-c:v','libx264','-preset','slow','-crf','14','-tune','animation','-profile:v','high','-pix_fmt','yuv420p','v2_video.mp4'],stdin=subprocess.PIPE)
    for i in range(n): p.stdin.write(frame(i/FPS).tobytes())
    p.stdin.close(); p.wait(); print('frames',n)
