#!/usr/bin/env node
/* Spaceman audit (v1.3): Spaceman vs crew win rate, who becomes Journey Spaceman, hostages.
   Usage: node tools/spaceman-audit.js [runs] [players] [minutes] [index.html]   env PACE=real|sim MODE=party|chill|competitive FINAL=1 MS=1 */
const fs=require('fs');const html=fs.readFileSync(process.argv[5]||require('path').join(__dirname,'..','index.html'),'utf8');
const missions=html.match(/const MISSIONS = \{[\s\S]*?\n\};/)[0];const engine=html.slice(html.indexOf('/* ENGINE:START */'),html.indexOf('/* ENGINE:END */'));
const {Engine}=new Function(`${missions}\n${engine}\nreturn {Engine};`)();
const runs=+process.argv[2]||100, n=+process.argv[3]||4, mins=+process.argv[4]||60, real=(process.env.PACE||'real')==='real', fin=process.env.FINAL==='1';
let smWin=0, cap=0, co=0, crewT=0, smT=0, held=0, hj=0, margin=[], noWinner=0, msK={}, pu=0;
for(let r=0;r<runs;r++){
  const crew=Array.from({length:n},(_,i)=>'p'+i);
  const S=Engine.create({crew,captain:'p0',names:Object.fromEntries(crew.map(x=>[x,x])),lineup:[],mode:process.env.MODE||'party',pace:real?'real':'sim'});S.bots=[...crew];
  let asked=false, lastEv=null;
  while(S.min<mins){
    if(fin&&!asked&&S.min>=mins-12){asked=true;Engine.act(S,{type:'final',by:'p1'});}
    Engine.step(S,real?.05:.05,real?3:.5); S.out.length=0;
    if(S.ev&&S.ev!==lastEv){lastEv=S.ev; if(S.ev.type==='milestone') msK[S.ev.k]=(msK[S.ev.k]||0)+1; if(S.ev.type==='drop') pu++;}
  }
  Engine.finale(S); (global.cp=global.cp||[]).push(S.pts.p0 - S.crew.slice(1).reduce((a,id)=>a+S.pts[id],0)/(S.crew.length-1));
  const cw=Engine.crewWins(S); if(!cw) smWin++;
  const w=Engine.winner(S); if(cw&&!w) noWinner++;
  if(w==='p0') cap++; if(w&&w===S.copilot) co++;
  crewT+=Engine.crewTotal(S); smT+=Engine.smTotal(S); if(S.hj) held++; hj+=S.hjLog.length+(S.hj?1:0);
  margin.push(Engine.crewTotal(S)-Engine.smTotal(S));
}
margin.sort((a,b)=>a-b);
const p=x=>(100*x/runs).toFixed(1)+'%';
console.log(`${n}p ${mins}m ${real?'real':'sim'} ${process.env.MODE||'party'} x${runs}: SPACEMAN ${p(smWin)} | crew ${p(runs-smWin)} | captain JS ${p(cap)} (fair ${(100/n*(runs-smWin)/runs).toFixed(1)}%) | copilot JS ${p(co)} | avg crew ${(crewT/runs).toFixed(0)} vs sm ${(smT/runs).toFixed(0)} | median margin ${margin[runs>>1]} | hostages/mission ${(hj/runs).toFixed(2)} held at end ${p(held)} | crew-win no-JS ${noWinner}`);
if(process.env.MS) console.log('  milestones', JSON.stringify(msK), 'drops/mission', (pu/runs).toFixed(2));
console.log('  captain minus avg passenger:', (cp.reduce((a,b)=>a+b,0)/runs).toFixed(1));
