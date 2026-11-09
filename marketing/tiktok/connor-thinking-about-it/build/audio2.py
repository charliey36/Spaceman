import numpy as np, json, subprocess
SR=48000; T=48.6; N=int(T*SR); rng=np.random.default_rng(7)
mix=np.zeros(N); voice=np.zeros(N)
t_=lambda d: np.arange(int(d*SR))/SR
def add(buf, sig, t, g=1.0):
    i=int(t*SR); j=min(N,i+len(sig)); buf[i:j]+=sig[:j-i]*g
def lp(x,k):
    from scipy.signal import lfilter
    return lfilter([k],[1,-(1-k)],x)
def noise(d): return rng.standard_normal(int(d*SR))
def tone(f,d,dec=6,a=0.004,typ='sin'):
    t=t_(d); w=np.sin(2*np.pi*f*t) if typ=='sin' else np.sign(np.sin(2*np.pi*f*t))*0.5
    e=np.minimum(1,t/a)*np.exp(-t*dec); return w*e
# --- sfx ---
def whoosh_up(d):
    t=t_(d); n=noise(d); y=np.zeros_like(n); 
    from scipy.signal import butter, sosfilt
    out=np.zeros_like(n); seg=int(0.05*SR)
    for k in range(0,len(n),seg):
        f=200+3800*(k/len(n))**2; sos=butter(2,[max(60,f*0.6),f*1.4],btype='band',fs=SR,output='sos'); out[k:k+seg]=sosfilt(sos,n[k:k+seg])
    return out*(t/d)**1.5*0.5
def chord(fs,d,dec=2.2,g=0.25): return sum(tone(f,d,dec) for f in fs)*g
def chime(): a=tone(740,0.6,7)*0.35; b=np.concatenate([np.zeros(int(.08*SR)),tone(988,0.52,6)*0.35]); n=min(len(a),len(b)); return a[:n]+b[:n]
def tick(): return tone(1500,0.08,40)*0.25+tone(3000,0.08,60)*0.1
def pop(): t=t_(0.18); return np.sin(2*np.pi*(500+900*t/0.18)*t)*np.exp(-t*22)*0.35
def ping(): return tone(1318,0.9,4.5)*0.18+tone(1976,0.9,6)*0.08
def squelch():
    from scipy.signal import butter, sosfilt
    n=sosfilt(butter(2,[900,3500],btype='band',fs=SR,output='sos'),noise(0.16))*np.linspace(1,0,int(.16*SR))*0.5
    o=np.zeros(int(.35*SR)); o[:len(n)]+=n; b=tone(1150,0.12,25)*0.22; o[int(.15*SR):int(.15*SR)+len(b)]+=b; return o
def sting():
    t=t_(1.4); sub=np.sin(2*np.pi*(65*np.exp(-t*1.1))*t)*np.exp(-t*2.4)
    from scipy.signal import butter, sosfilt
    hit=sosfilt(butter(2,[80,900],btype='band',fs=SR,output='sos'),noise(1.4))*np.exp(-t*8)
    al=np.concatenate([tone(880,0.2,8,typ='sq'),tone(659,0.5,5,typ='sq')]); al=sosfilt(butter(2,2500,fs=SR,output='sos'),al)
    o=sub*0.7+hit*0.5; o[:len(al)]+=al*0.35; return o
def smgain():
    t=t_(0.7); return np.sin(2*np.pi*(520*np.exp(-t*1.6))*t)*np.exp(-t*3.5)*0.3+tone(196,0.7,3)*0.2
def thud():
    t=t_(0.8); return np.sin(2*np.pi*(80*np.exp(-t*2))*t)*np.exp(-t*5)*0.8
add(mix, whoosh_up(2.4), 0.1, 0.45); add(mix, chord([523.3,659.3,784,1046.5],2.4,1.6,0.12), 2.5)
add(mix, chord([784,1174.7],1.2,3,0.18), 3.6)
for x in [6.8,7.2,7.6,8.0]: add(mix, tick(), x)
add(mix, smgain(), 8.62)
add(mix, sting(), 11.22, 0.33)
add(mix, pop(), 13.9, 0.8)
for x in [16.5,17.3,18.1]: add(mix, chime(), x, 0.7)
add(mix, ping(), 21.15)
add(mix, squelch(), 29.9, 0.7)
add(mix, pop(), 34.25, 0.8); add(mix, pop(), 36.0, 0.8); add(mix, ping(), 35.95, 0.8)
add(mix, thud(), 39.9, 0.45); add(mix, smgain(), 39.95, 0.45); add(mix, ping(), 40.3, 0.8)
add(mix, squelch(), 42.6, 0.7)
add(mix, chord([220,329.6,440,554.4,659.3],3.2,1.0,0.1), 45.2)
# --- voices ---
VO=[('n1',0.30),('n2',3.70),('n3',6.40),('n4',11.35),('sm1',13.55),('n5',16.10),('n6',19.25),('d1',23.40),('d2',25.10),('d3',28.40),('sm2',30.30),('d4',34.25),('d5',36.05),('n7',38.00),('sm3',42.95)]
def load(f):
    raw=subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-ac','1','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.float32).astype(float)
vlen=[]
for n,t in VO:
    s=load(f'vo2/{n}.wav'); act=s[np.abs(s)>0.02]; s=s/np.sqrt((act**2).mean())*0.13*(1.08 if n.startswith('sm') else 1.22 if n.startswith('d') else 1.0); s=np.clip(s,-0.95,0.95); add(voice, s, t); vlen.append((t,t+len(s)/SR))
# --- music bed ---
t=t_(T)
pad=sum(np.sin(2*np.pi*f*t+ph)*g for f,ph,g in [(55,0,.5),(82.41,1,.28),(110,2,.22),(130.8,.4,.12),(164.8,.5,.1),(220,1.3,.04)])
pad*=0.65+0.35*np.sin(2*np.pi*0.2*t)
beat=((t*2)%1); kick=np.sin(2*np.pi*(55+40*np.exp(-beat*30))*t)*np.exp(-beat*10)
hat=lp(noise(T),0.6)-lp(noise(T),0.2); hat*=np.exp(-((t*4)%1)*40)*0.08
bed=pad*0.5+kick*0.45+hat
g=np.ones(N)
def ramp(a,b,v0,v1): i,j=int(a*SR),int(b*SR); g[i:j]=np.linspace(v0,v1,j-i)
ramp(0,2.5,0.3,1)
for a,b in vlen:  # duck under speech
    i,j=int((a-0.05)*SR),int((b+0.1)*SR); g[i:j]=np.minimum(g[i:j],0.45)
g[int(33.55*SR):int(34.15*SR)]=0; ramp(33.45,33.6,0.45,0); ramp(34.15,34.4,0,0.45)
ramp(45.2,46.2,0.45,0.25); ramp(T-0.8,T,0.25,0)
from scipy.signal import lfilter
gs=lfilter([0.0015],[1,-0.9985],g)  # smooth gain
mix=mix*0.9+bed*gs*0.11+voice
mix/=np.abs(mix).max()/0.9
st=np.stack([mix,mix],1)
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','f64le','-ar',str(SR),'-ac','2','-i','-','-af','loudnorm=I=-14:TP=-2:LRA=9,alimiter=limit=0.75:level=false','-ar','48000','-c:a','pcm_s16le','mix2.wav'],input=st.tobytes())
print('ok')
