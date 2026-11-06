#!/usr/bin/env node
/* Spaceman balance simulation.
   Runs the real mission engine from index.html with every player played by an equally skilled bot,
   then reports how often each role becomes Journey Spaceman compared with a fair share.
   p0 is always the Captain. The Co-Pilot is assigned at random after launch and can change hands,
   so the report splits passengers by their Co-Pilot history.
   Since v1.0 Spaceman is an opponent too. Role fairness is measured on the best crew member (Engine.topCrew),
   and a separate column reports how often Spaceman retains control (no crew member finishes above it).
   Usage: node tools/balance-sim.js [runs=4000] [variant=final|noperks|noallow|allow<s>|co<s>|bonus<n>|supply<x>|noshield|slots2] [index.html] [pacing=party|chill|competitive]
   The third argument is a path to an index.html to test (defaults to ../index.html). Pacing: chill = Relaxed, party = Balanced, competitive = Chaotic. */
const fs = require('fs'), path = require('path');
const html = fs.readFileSync(process.argv[4] || path.join(__dirname, '..', 'index.html'), 'utf8');
const missions = html.match(/const MISSIONS = \{[\s\S]*?\n\};/)[0];
const engine = html.slice(html.indexOf('/* ENGINE:START */'), html.indexOf('/* ENGINE:END */'));
const { Engine, PT } = new Function(`${missions}\n${engine}\nreturn { Engine, PT, MISSIONS };`)();

const runs = +process.argv[2] || 4000, variant = process.argv[3] || 'final';
if (variant === 'noallow'){ PT.proxyAllow = 0; PT.copilotAllow = 0; }
if (variant === 'noperks'){ PT.coWinBonus = 0; PT.coSlots = PT.slots; PT.coShield = false; PT.coSupply = 1; }
if (variant === 'noshield') PT.coShield = false;
if (variant === 'slots2') PT.coSlots = PT.slots;
if (variant.startsWith('allow')) PT.proxyAllow = +variant.slice(5);
if (variant.startsWith('co') && !isNaN(+variant.slice(2))) PT.copilotAllow = +variant.slice(2);
if (variant.startsWith('bonus')) PT.coWinBonus = +variant.slice(5);
if (variant.startsWith('supply')) PT.coSupply = +variant.slice(6);
const MODE = process.argv[5] || 'party';
const DT = .02;                                  /* journey minutes per step; the prototype runs 10 real seconds per journey minute */

function run(N, mins){
  const c = {cap:0, pass:0, start:0, startN:0, fin:0, finN:0, ever:0, everN:0, never:0, neverN:0}; let lead = 0, moves = 0, pts = {cap:0, pass:0}, smWins = 0, smPts = 0;
  for (let r = 0; r < runs; r++){
    const crew = Array.from({length:N}, (_, i) => 'p' + i);
    const S = Engine.create({crew, captain:'p0', names:Object.fromEntries(crew.map(x => [x, x])), lineup:[], mode:MODE});
    S.bots = crew; let leader = null;
    for (let t = 0; t < mins; t += DT){
      Engine.step(S, DT, DT*10); S.out.length = 0;
      const max = Math.max(...crew.map(x => S.pts[x])), l = crew.filter(x => S.pts[x] === max).join();
      if (max > 0 && l !== leader){ if (leader) lead++; leader = l; }
    }
    if (!Engine.winner(S)) smWins++; smPts += S.sm;
    const w = Engine.topCrew(S), P = crew.slice(1), start = S.coLog[0] && S.coLog[0].id, fin = S.copilot, ever = new Set(S.coLog.map(x => x.id));
    moves += Math.max(0, S.coLog.length - 1);
    if (w === 'p0') c.cap++; else if (w) c.pass++;
    pts.cap += S.pts.p0; P.forEach(x => { pts.pass += S.pts[x]/P.length; });
    if (start){ c.startN++; if (w === start) c.start++; }
    if (fin){ c.finN++; if (w === fin) c.fin++; }
    P.forEach(x => { if (ever.has(x)){ c.everN++; if (w === x) c.ever++; } else { c.neverN++; if (w === x) c.never++; } });
  }
  const pct = (x, n = runs) => n ? (100*x/n).toFixed(1).padStart(5) + '%' : '    –';
  console.log(`${N} players · ${String(mins).padStart(2)} min | Captain ${pct(c.cap)} · each passenger ${pct(c.pass/(N - 1))} | fair ${(100/N).toFixed(1)}% | started as Co-Pilot ${pct(c.start, c.startN)} · final Co-Pilot ${pct(c.fin, c.finN)} · ever ${pct(c.ever, c.everN)} · never ${pct(c.never, c.neverN)} | seat changes ${(moves/runs).toFixed(2)} | avg pts ${(pts.cap/runs).toFixed(1)} / ${(pts.pass/runs).toFixed(1)} | lead changes ${(lead/runs).toFixed(1)} | Spaceman retains control ${pct(smWins)} (avg ${(smPts/runs).toFixed(1)} credits)`);
}
console.log(`Spaceman balance simulation · ${runs} missions per row · variant: ${variant} · pacing: ${MODE} · Co-Pilot perks: +${PT.coWinBonus} per win, ${PT.coSlots} slots, shield ${PT.coShield}, supply ×${PT.coSupply}`);
for (const N of [4, 5, 6]) for (const mins of [20, 45, 60]) run(N, mins);
