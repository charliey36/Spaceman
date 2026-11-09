from kokoro_onnx import Kokoro
import soundfile as sf, numpy as np, json
k = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
SR=24000
def trim(x):
    nz=np.where(np.abs(x)>0.008)[0]; return x[max(0,nz[0]-int(.03*SR)):nz[-1]+int(.08*SR)]
def say(t, v, sp): s,_=k.create(t, voice=v, speed=sp, lang='en-gb'); return trim(s)
def join(*parts):
    out=[]
    for p in parts: out.append(np.zeros(int(p*SR)) if isinstance(p,float) else p)
    return np.concatenate(out)
M,C,S='bf_emma','bm_fable','bm_george'
L={
 'n1': say("So we played this road trip game called Spaceman.", M, 1.0),
 'n2': say("Everyone plays mini games on their own phone.", M, 1.0),
 'n3': say("And there's an AI called Spaceman, who steals your points when you get things wrong.", M, 1.0),
 'n4': say("Then, halfway through, he kidnapped me.", M, 0.98),
 'n5': say("To get me back, my friends had to pay thirty points.", M, 1.0),
 'n6': join(say("Twenty in. Ten to go.", M, 0.98), 0.25, say("And Connor had thirty six.", M, 0.95)),
 'd1': say("Connor. It's ten points.", M, 1.02),
 'd2': say("Yeah, but if I pay, you're back in first place.", C, 1.0),
 'd3': say("I've been kidnapped!", M, 1.05),
 'd4': say("He is not thinking about it.", M, 1.05),
 'd5': say("I'm thinking about it.", C, 0.95),
 'n7': join(say("He did not pay.", M, 0.95), 0.3, say("Spaceman drained my points, and Connor took first place.", M, 1.0)),
 'sm1': say("Megan is with me now.", S, 0.86),
 'sm2': join(say("Connor.", S, 0.84), 0.5, say("is thinking about it.", S, 0.84)),
 'sm3': say("Thank you, Connor.", S, 0.84),
}
d={}
for n,x in L.items(): sf.write(f'v2_{n}.wav', x, SR); d[n]=round(len(x)/SR,3)
json.dump(d, open('v2_dur.json','w'), indent=0); print(d)
