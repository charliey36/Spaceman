import asyncio, base64, os, json
from playwright.async_api import async_playwright
W,H,DPR = 414, 736, 1080/414
FONTS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'fonts.css')).read()
class Rec:
    async def open(self, p, email='charlie.ad@example.com'):
        self.b = await p.chromium.launch()
        self.ctx = await self.b.new_context(viewport={'width':W,'height':H}, device_scale_factor=DPR, is_mobile=True, has_touch=True)
        await self.ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=FONTS))
        self.pg = await self.ctx.new_page(); self.errs=[]; self.pg.on('pageerror', lambda e: self.errs.append(str(e)))
        await self.pg.add_init_script("speechSynthesis.speak=u=>{setTimeout(()=>u.onend&&u.onend(),50)};")
        await self.pg.goto('http://127.0.0.1:8771/index.html'); await self.pg.wait_for_timeout(1200)
        await self.pg.fill('#auth-email', email); await self.pg.click('#auth-go'); await self.pg.wait_for_timeout(1300)
        self.cdp = await self.ctx.new_cdp_session(self.pg); self.n=0; self.dir=None; self.marks={}
        await self.cdp.send('Emulation.setVirtualTimePolicy', {'policy':'pause'})
    async def step(self, ms=1000/30):
        fut = asyncio.get_event_loop().create_future()
        self.cdp.once('Emulation.virtualTimeBudgetExpired', lambda e: fut.done() or fut.set_result(1))
        await self.cdp.send('Emulation.setVirtualTimePolicy', {'policy':'advance', 'budget':ms})
        await asyncio.wait_for(fut, 20)
    async def shot(self, path, scale=DPR):
        r = await self.cdp.send('Page.captureScreenshot', {'format':'jpeg','quality':95,'clip':{'x':0,'y':0,'width':W,'height':H,'scale':scale}})
        open(path,'wb').write(base64.b64decode(r['data']))
    async def adv(self, sec, rec=False):
        for i in range(int(round(sec*30))):
            await self.step()
            if rec and self.dir:
                await self.shot(f'{self.dir}/{self.n:05d}.jpg'); self.n+=1
    def mark(self, k): self.marks[k]=self.n; print('mark', k, self.n, round(self.n/30,2))
    async def js(self, code, arg=None):
        return await self.pg.evaluate(code, arg) if arg is not None else await self.pg.evaluate(code)
