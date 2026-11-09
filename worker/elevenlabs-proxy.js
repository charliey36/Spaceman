/* Spaceman → ElevenLabs proxy (Cloudflare Worker). App → this Worker → ElevenLabs → audio back.
   Secrets live here, never in the page:  wrangler secret put ELEVENLABS_API_KEY
   Vars (wrangler.toml):  ALLOWED_ORIGINS = "https://charliey36.github.io"  (comma separated)
   Only text-to-speech and read-only account checks are forwarded. Anything else is refused. */
const ALLOWED_PATHS = [/^\/v1\/text-to-speech\/[A-Za-z0-9]{10,40}$/, /^\/v1\/models$/, /^\/v1\/user\/subscription$/, /^\/v1\/voices\/[A-Za-z0-9]{10,40}$/];
const MAX_CHARS = 600;
export default {
  async fetch(req, env) {
    const origin = req.headers.get('Origin') || '';
    const allowed = String(env.ALLOWED_ORIGINS || '').split(',').map(s => s.trim()).filter(Boolean);
    const ok = allowed.includes(origin) || /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(origin);
    const cors = { 'Access-Control-Allow-Origin': ok ? origin : allowed[0] || 'null', 'Access-Control-Allow-Methods': 'GET,POST,OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type, Accept', 'Access-Control-Max-Age': '86400', 'Vary': 'Origin' };
    if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors });
    const json = (status, body) => new Response(JSON.stringify(body), { status, headers: { ...cors, 'Content-Type': 'application/json' } });
    if (!ok) return json(403, { detail: { status: 'origin_not_allowed', message: 'This origin is not allowed to use the proxy.' } });
    if (!env.ELEVENLABS_API_KEY) return json(500, { detail: { status: 'proxy_not_configured', message: 'The proxy has no ELEVENLABS_API_KEY secret.' } });
    const url = new URL(req.url);
    if (url.pathname === '/health') return json(200, { ok: true });
    if (!ALLOWED_PATHS.some(r => r.test(url.pathname))) return json(404, { detail: { status: 'path_not_allowed', message: 'That path is not proxied.' } });
    let body;
    if (req.method === 'POST') {
      const raw = await req.text();
      try { const j = JSON.parse(raw); if (typeof j.text !== 'string' || j.text.length > MAX_CHARS) return json(413, { detail: { status: 'text_too_long', message: `Text must be under ${MAX_CHARS} characters.` } }); } catch { return json(400, { detail: { status: 'bad_json', message: 'Body must be JSON.' } }); }
      body = raw;
    }
    const up = await fetch('https://api.elevenlabs.io' + url.pathname + url.search, { method: req.method, headers: { 'xi-api-key': env.ELEVENLABS_API_KEY, 'Content-Type': 'application/json', 'Accept': req.headers.get('Accept') || '*/*' }, body });
    const h = new Headers(cors); h.set('Content-Type', up.headers.get('Content-Type') || 'application/octet-stream');
    return new Response(up.body, { status: up.status, headers: h });
  }
};
