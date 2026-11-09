import asyncio, sys, json, os
from playwright.async_api import async_playwright
sys.path.insert(0,'.'); from harness import *
END = r"""(() => { const S = LJ.S; S.tx = null; document.getElementById('tx')?.remove(); const d = document.createElement('div'); d.id = 'adend';
  d.innerHTML = `<style>#adend{position:fixed;inset:0;z-index:9999;display:grid;place-items:center;align-content:center;gap:18px;text-align:center;padding:28px;background:radial-gradient(120% 70% at 50% 40%, rgba(163,40,58,.22), rgba(5,7,13,0) 62%), #05070D;animation:adIn .5s cubic-bezier(.2,.8,.2,1) both}
  #adend .av{margin:0 auto;filter:drop-shadow(0 10px 30px rgba(163,40,58,.45));animation:adPop .7s cubic-bezier(.3,1.4,.4,1) .1s both}
  #adend h1{font-family:Unbounded,system-ui;font-weight:600;font-size:40px;letter-spacing:.06em;margin:6px 0 0;color:#fff;animation:adUp .6s cubic-bezier(.2,.8,.2,1) .25s both}
  #adend p{font-family:Geist,system-ui;font-size:17px;line-height:1.45;color:rgba(255,255,255,.72);margin:0;animation:adUp .6s cubic-bezier(.2,.8,.2,1) .4s both}
  #adend small{font-family:'Geist Mono',monospace;font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:#E36A7C;margin-top:10px;animation:adUp .6s cubic-bezier(.2,.8,.2,1) .55s both}
  @keyframes adIn{from{opacity:0}to{opacity:1}} @keyframes adPop{from{opacity:0;transform:scale(.6)}to{opacity:1;transform:none}} @keyframes adUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}</style>
  ${av('sm',132)}<h1>SPACEMAN</h1><p>The road trip party game.<br>You and your friends vs an AI that cheats.</p><small>Every phone in the car plays</small>`;
  document.body.appendChild(d); })()"""
TICK = "(dt) => { if (!window.__man) return; const S = LJ.S; S.bots = []; Engine.step(S, dt*SIM_RATE, dt); drain(); paint(); }"
async def main():
    async with async_playwright() as p:
        R=Rec(); await R.open(p)
        async def run(sec, name=None, at=None):
            """advance sec seconds at 30fps, manual engine tick each frame; at = {frame_idx: js}"""
            if name: R.dir=f'c3/{name}'; os.makedirs(R.dir, exist_ok=True); R.n=0
            for i in range(int(round(sec*30))):
                if at and i in at:
                    for code in (at[i] if isinstance(at[i], list) else [at[i]]): await R.js(code)
                await R.js(TICK, 1/30); await R.step()
                if name: await R.shot(f'{R.dir}/{R.n:05d}.jpg'); R.n+=1
            R.dir=None
        F = lambda s: int(round(s*30))
        await R.js("(() => { const u = cur(); u.name='Charlie'; ME.name='Charlie'; const L = u.launch; L.pace='sim'; L.dest='Cornwall'; L.crew=['megan','connor','zac','thomas']; L.captain=ME.id; persist(); })()")
        await R.js("setTimeout(() => startJourney(), 0)")
        await R.adv(0.2)
        R.dir='c3/s01'; os.makedirs(R.dir, exist_ok=True); R.n=0
        await R.adv(3.6, rec=True); R.dir=None
        await R.adv(1.5)
        # freeze the app's loop; from here we drive the engine ourselves
        await R.js("""(() => { cancelAnimationFrame(LJ.raf); window.tick = () => {}; window.__man = true; const S = LJ.S;
          S.ev = null; S.ch = null; S.q = []; S.agenda = []; S.tx = null; S.txq = []; S.copilot = S.copilot || null;
          S.min = 22; S.lastChEnd = 21; S.nextAt = 0; S.nextDrop = 1e9; S.nextRoastCheck = 1e9; S.nextStruggle = 1e9; S.mi = 14.2;
          Object.assign(S.pts, {megan:34, connor:31, zac:22, thomas:17}); S.pts[ME.id] = 23; S.sm = 40;
          S.ae = {}; S.aeNext = Object.fromEntries(S.crew.map(id => [id, 1e9]));
          LJ.viewer = 'megan'; S.pick = 'bluff'; renderHud(); paint(); })()""")
        await run(0.2)
        st = await R.js("JSON.stringify({ch:LJ.S.ch&&[LJ.S.ch.id,LJ.S.ch.phase], ev:LJ.S.ev&&LJ.S.ev.type, q:LJ.S.q.map(x=>x.type)})"); print('after pick', st)
        await R.js("(() => { LJ.S.nextAt = 1e9; })()")
        await run(0.3)
        await run(2.7, 's02_intro')
        # move into the question
        await R.js("(() => { const ch = LJ.S.ch; if (ch.phase === 'intro') ch.introUntil = LJ.S.rt; })()"); await run(0.15)
        await R.js("(() => { LJ.S.ch.f = {s:'The first computer mouse was made of wood.', t:true, n:'1964.'}; paint(); })()")
        f = await R.js("JSON.stringify({ph:LJ.S.ch.phase, f:LJ.S.ch.f, voters:LJ.S.ch.voters})"); print('bluff', f)
        t = json.loads(f)['f']['t']; tj = 'true' if t else 'false'; fj = 'false' if t else 'true'
        pick = lambda who, v: f"Engine.act(LJ.S, {{type:'tf', by:{who}, v:{v}}})"
        await run(2.3, 's03_question', {F(0.5):pick("'zac'", fj), F(0.9):pick("'megan'", tj), F(1.3):pick("'thomas'", fj), F(1.7):pick("'connor'", tj)})
        await R.js(pick("ME.id", fj)); 
        await run(2.6, 's04_reveal')
        print('after reveal', await R.js("JSON.stringify({pts:LJ.S.pts, sm:LJ.S.sm})"))
        # hijack Megan
        await R.js("(() => { const S = LJ.S; S.ch = null; S.min = 31; S.lastChEnd = 31; S.agenda = [{at:S.min, type:'hijack'}]; S.nextAt = 0; })()")
        await R.js(TICK, 1/30)
        await R.js("(() => { const S = LJ.S; S.nextAt = 1e9; S.q = []; S.agenda = []; if (S.ev){ S.ev.sm = 'Megan is with me now.'; S.ev.atlas = ''; S.ev.until = 1e9; } S.hj.nextTick = 1e9; S.hj.retryAt = 1e9; paint(); })()")
        print('hijack', await R.js("JSON.stringify({ev:LJ.S.ev&&LJ.S.ev.type, hj:LJ.S.hj&&LJ.S.hj.who, pts:LJ.S.pts, sm:LJ.S.sm})"))
        await run(4.8, 's05_hijack', {F(2.7):"Engine.act(LJ.S, {type:'avemote', by:'megan', e:'😭'})"})
        don = lambda who, n: f"Engine.act(LJ.S, {{type:'hj-donate', by:{who}, n:{n}}})"
        await run(3.1, 's06_donate', {F(0.5):don("'zac'",5), F(1.3):don("ME.id",5), F(2.1):don("'thomas'",10)})
        await run(4.0, 's07_connor_tile')
        await R.js("(() => { LJ.viewer = 'connor'; renderHud(); paint(); })()")
        await run(6.8, 's08_connor_phone')
        await R.js("(() => { LJ.viewer = 'megan'; renderHud(); const S = LJ.S; S.tx = {kind:'roast', id:++S.txId, phase:'play', text:'Connor is thinking about it.', at:S.min, reacts:{}, said:{}, dur:14, until:S.rt+1e9, atRt:S.rt}; paint(); })()")
        await run(1.95)
        await run(4.2, 's09_tx1')
        await R.js("(() => { const S = LJ.S; S.tx = null; document.getElementById('tx')?.remove(); paint(); })()")
        await run(3.8, 's10_megan_connor', {F(0.15):"Engine.act(LJ.S, {type:'avemote', by:'megan', e:'😡'})", F(1.9):"Engine.act(LJ.S, {type:'avemote', by:'connor', e:'🫡'})"})
        await run(4.7, 's11_ransom', {F(2.0):"(() => { const h = LJ.S.hj; h.lvl = 1; h.nextTick = LJ.S.min; })()", F(2.1):"(() => { LJ.S.hj.nextTick = 1e9; LJ.S.q = LJ.S.q.filter(x => x.type !== 'roast'); })()"})
        print('after ransom', await R.js("JSON.stringify({pts:LJ.S.pts, sm:LJ.S.sm, toast:document.querySelector('.toast')?.innerText})"))
        await R.js("(() => { const S = LJ.S; S.tx = {kind:'roast', id:++S.txId, phase:'play', text:'Thank you, Connor.', at:S.min, reacts:{}, said:{}, dur:14, until:S.rt+1e9, atRt:S.rt}; paint(); })()")
        await run(1.95)
        await run(2.6, 's12_tx2')
        await R.js(END)
        await run(3.4, 's13_end')
        print(R.errs)
asyncio.run(main())
