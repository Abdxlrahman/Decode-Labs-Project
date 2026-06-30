/* ═══════════════════════════════════════════════════════
   CYBER NETWORK CONSTELLATION BACKGROUND
   ══════════════════════════════════════════════════════ */
(function(){
  const cv = document.getElementById('cyber-canvas');
  const cx = cv.getContext('2d');
  let pts = [];
  const numPts = 45;
  const maxDist = 135;

  function rsz(){
    cv.width=innerWidth; cv.height=innerHeight;
    pts = [];
    for(let i=0; i<numPts; i++){
      pts.push({
        x: Math.random() * cv.width,
        y: Math.random() * cv.height,
        vx: (Math.random() - 0.5) * 0.7,
        vy: (Math.random() - 0.5) * 0.7,
        r: Math.random() * 2 + 1
      });
    }
  }

  function drawGrid() {
    cx.strokeStyle = 'rgba(255, 107, 0, 0.015)';
    cx.lineWidth = 1;
    const gridSz = 60;
    for(let x=0; x<cv.width; x+=gridSz) {
      cx.beginPath();
      cx.moveTo(x, 0);
      cx.lineTo(x, cv.height);
      cx.stroke();
    }
    for(let y=0; y<cv.height; y+=gridSz) {
      cx.beginPath();
      cx.moveTo(0, y);
      cx.lineTo(cv.width, y);
      cx.stroke();
    }
  }

  function loop(){
    cx.clearRect(0,0,cv.width,cv.height);
    drawGrid();
    
    // Draw connections
    cx.lineWidth = 1;
    for(let i=0; i<pts.length; i++){
      const p1 = pts[i];
      for(let j=i+1; j<pts.length; j++){
        const p2 = pts[j];
        const dx = p1.x - p2.x;
        const dy = p1.y - p2.y;
        const dist = Math.sqrt(dx*dx + dy*dy);
        if(dist < maxDist){
          const alpha = (1 - dist / maxDist) * 0.12;
          cx.strokeStyle = `rgba(255, 107, 0, ${alpha})`;
          cx.beginPath();
          cx.moveTo(p1.x, p1.y);
          cx.lineTo(p2.x, p2.y);
          cx.stroke();
        }
      }
    }

    // Draw points
    cx.fillStyle = 'rgba(255, 107, 0, 0.25)';
    for(let p of pts){
      cx.beginPath();
      cx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      cx.fill();
      
      // Move points
      p.x += p.vx;
      p.y += p.vy;
      
      // Boundary collision
      if(p.x < 0 || p.x > cv.width) p.vx *= -1;
      if(p.y < 0 || p.y > cv.height) p.vy *= -1;
    }
    
    requestAnimationFrame(loop);
  }

  rsz(); addEventListener('resize',rsz); loop();
})();


/* ═══════════════════════════════════════════════════════
   TYPEWRITER
   ══════════════════════════════════════════════════════ */
(function(){
  const el=document.getElementById('typewriter');
  const lines=[
    'Real-time entropy analysis & pattern detection.',
    'Checks against millions of breached passwords via HIBP.',
    'Estimates crack time using GPU-speed simulation.',
    'Generates cryptographically strong passwords instantly.',
  ];
  let li=0,ci=0,del=false;
  function tick(){
    const line=lines[li];
    if(!del){ el.textContent=line.slice(0,++ci); if(ci===line.length){del=true;setTimeout(tick,2400);return;} }
    else     { el.textContent=line.slice(0,--ci); if(ci===0){del=false;li=(li+1)%lines.length;setTimeout(tick,400);return;} }
    setTimeout(tick,del?32:55);
  }
  setTimeout(tick,1200);
})();

/* ═══════════════════════════════════════════════════════
   ANALYZER ENGINE
   ══════════════════════════════════════════════════════ */
const COMMON=new Set(['password','123456','12345678','admin','welcome','qwerty','password123',
  'letmein','iloveyou','football','abc123','111111','monkey','dragon','master',
  'sunshine','princess','shadow','michael','superman','charlie','donald','pass','login']);

function analyzePassword(pwd){
  if(!pwd) return null;
  const chars = Array.from(pwd);
  
  // 1. Zero Point Policy checks
  const length_ok = pwd.length >= 8;
  
  let has_upper = false;
  let has_lower = false;
  let has_digit = false;
  let has_special = false;
  
  for (let char of chars) {
    if (/[a-z]/.test(char)) has_lower = true;
    else if (/[A-Z]/.test(char)) has_upper = true;
    else if (/\d/.test(char)) has_digit = true;
    else if (/[^a-zA-Z0-9]/.test(char)) has_special = true;
  }
  
  const notCommon = !COMMON.has(pwd.toLowerCase());
  
  // Repeated check (avoid aaa, 111, etc.)
  let noRepeat = true;
  for (let i = 0; i < chars.length - 2; i++) {
    if (chars[i] === chars[i+1] && chars[i] === chars[i+2]) {
      noRepeat = false;
      break;
    }
  }
  
  // Sequence check
  let noSeq = true;
  const password_lower = pwd.toLowerCase();
  for (let i = 0; i < password_lower.length - 2; i++) {
    const c1 = password_lower.charCodeAt(i);
    const c2 = password_lower.charCodeAt(i+1);
    const c3 = password_lower.charCodeAt(i+2);
    if ((c2 === c1 + 1 && c3 === c2 + 1) || (c2 === c1 - 1 && c3 === c2 - 1)) {
      noSeq = false;
      break;
    }
  }
  
  if (noSeq) {
    const keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"];
    for (let row of keyboard_rows) {
      for (let i = 0; i < password_lower.length - 2; i++) {
        const seq = password_lower.substring(i, i+3);
        if (row.includes(seq) || row.includes(seq.split('').reverse().join(''))) {
          noSeq = false;
          break;
        }
      }
      if (!noSeq) break;
    }
  }
  
  const checks = {
    length: length_ok,
    uppercase: has_upper,
    lowercase: has_lower,
    digit: has_digit,
    special: has_special,
    notCommon: notCommon,
    noRepeat: noRepeat,
    noSeq: noSeq
  };
  
  const policy_passed = length_ok && has_upper && has_lower && has_digit && has_special;
  
  // 2. Score Calculation
  let score = 0;
  if (policy_passed) {
    // Length (up to 30)
    if (pwd.length >= 16) score += 30;
    else if (pwd.length >= 12) score += 25;
    else if (pwd.length >= 8) score += 15;
    
    // Variety (up to 40)
    if (has_upper) score += 10;
    if (has_lower) score += 10;
    if (has_digit) score += 10;
    if (has_special) score += 10;
    
    // Security patterns (up to 30)
    if (notCommon) score += 10;
    if (noRepeat) score += 10;
    if (noSeq) score += 10;
  }
  
  score = Math.min(score, 100);
  
  // 3. Unicode Curveball (Entropy & Charset Size)
  let has_ascii_lower = false;
  let has_ascii_upper = false;
  let has_ascii_digit = false;
  let has_ascii_special = false;
  
  let has_unicode_lower = false;
  let has_unicode_upper = false;
  let has_unicode_digit = false;
  let has_unicode_special = false;
  
  for (let char of chars) {
    const code = char.charCodeAt(0);
    if (code < 128) {
      if (/[a-z]/.test(char)) has_ascii_lower = true;
      else if (/[A-Z]/.test(char)) has_ascii_upper = true;
      else if (/\d/.test(char)) has_ascii_digit = true;
      else has_ascii_special = true;
    } else {
      // Use Unicode property checks
      try {
        if (/^\p{Ll}$/u.test(char)) has_unicode_lower = true;
        else if (/^\p{Lu}$/u.test(char)) has_unicode_upper = true;
        else if (/^\p{Nd}$/u.test(char)) has_unicode_digit = true;
        else has_unicode_special = true;
      } catch (e) {
        // Fallback if browser doesn't support unicode properties
        has_unicode_special = true;
      }
    }
  }
  
  let charset = 0;
  charset += has_ascii_lower ? 26 : 0;
  charset += has_ascii_upper ? 26 : 0;
  charset += has_ascii_digit ? 10 : 0;
  charset += has_ascii_special ? 32 : 0;
  
  charset += has_unicode_lower ? 2100 : 0;
  charset += has_unicode_upper ? 1800 : 0;
  charset += has_unicode_digit ? 650 : 0;
  charset += has_unicode_special ? 140000 : 0;
  
  const entropy = charset > 0 ? +(Math.log2(charset) * pwd.length).toFixed(1) : 0;
  const unique = new Set(chars).size;
  const diversity = pwd.length > 0 ? +((unique / pwd.length) * 100).toFixed(1) : 0;
  
  let strength = '';
  if (!policy_passed) {
    strength = 'IMMEDIATE FAIL (Weak Policy)';
  } else if (score < 50) {
    strength = 'Weak (Needs Hardening)';
  } else if (score < 75) {
    strength = 'Medium (Acceptable)';
  } else if (score < 90) {
    strength = 'Strong (Highly Secure)';
  } else {
    strength = 'Excellent (Enterprise Grade)';
  }
  
  return {
    checks,
    score,
    entropy,
    diversity,
    unique,
    length: pwd.length,
    strength,
    charset,
    policy_passed
  };
}

/* Crack Time Estimator */
function crackTime(pwd,charset){
  if(!charset||!pwd.length) return 'Instantly';
  const secs=Math.pow(charset,pwd.length)/1e10;
  if(secs<1)             return 'Instantly';
  if(secs<60)            return `${Math.round(secs)} seconds`;
  if(secs<3600)          return `${Math.round(secs/60)} minutes`;
  if(secs<86400)         return `${Math.round(secs/3600)} hours`;
  if(secs<31536000)      return `${Math.round(secs/86400)} days`;
  if(secs<31536000*1e3)  return `${Math.round(secs/31536000)} years`;
  if(secs<31536000*1e6)  return `${(secs/31536000/1e3).toFixed(0)} thousand years`;
  if(secs<31536000*1e9)  return `${(secs/31536000/1e6).toFixed(0)} million years`;
  return `${(secs/31536000/1e9).toFixed(0)} billion years`;
}

/* HIBP k-anonymity */
async function checkHIBP(password){
  try{
    const buf=await crypto.subtle.digest('SHA-1',new TextEncoder().encode(password));
    const hex=Array.from(new Uint8Array(buf)).map(b=>b.toString(16).padStart(2,'0')).join('').toUpperCase();
    const prefix=hex.slice(0,5), suffix=hex.slice(5);
    const res=await fetch(`https://api.pwnedpasswords.com/range/${prefix}`,{headers:{'Add-Padding':'true'}});
    if(!res.ok) throw new Error();
    for(const line of (await res.text()).split('\n')){
      const [h,c]=line.split(':');
      if(h.trim()===suffix) return {pwned:true,count:parseInt(c)||1};
    }
    return {pwned:false};
  }catch(e){ return {error:true}; }
}

/* Password Generator */
function generatePassword(){
  const u='ABCDEFGHJKLMNPQRSTUVWXYZ', l='abcdefghjkmnpqrstuvwxyz',
        d='0123456789', s='!@#$%^&*()_+-=[]{}|;:,.<>?';
  const all=u+l+d+s;
  let p=[u[~~(Math.random()*u.length)],l[~~(Math.random()*l.length)],
         d[~~(Math.random()*d.length)],s[~~(Math.random()*s.length)]];
  for(let i=4;i<18;i++) p.push(all[~~(Math.random()*all.length)]);
  for(let i=p.length-1;i>0;i--){ const j=~~(Math.random()*(i+1));[p[i],p[j]]=[p[j],p[i]]; }
  return p.join('');
}

/* Animated Counter */
function animCounter(el,target,ms=1100){
  const t0=Date.now();
  (function loop(){
    const p=Math.min((Date.now()-t0)/ms,1);
    el.textContent=Math.round(p*p*target);
    if(p<1) requestAnimationFrame(loop); else el.textContent=target;
  })();
}

/* ═══════════════════════════════════════════════════════
   STRENGTH COLORS / WIDTHS
   ══════════════════════════════════════════════════════ */
const SC={
  'IMMEDIATE FAIL (Weak Policy)': '#ef4444',
  'Weak (Needs Hardening)': '#ef4444',
  'Medium (Acceptable)': '#fbbf24',
  'Strong (Highly Secure)': '#00f5ff',
  'Excellent (Enterprise Grade)': '#00ff88'
};
const SW={
  'IMMEDIATE FAIL (Weak Policy)': '15%',
  'Weak (Needs Hardening)': '30%',
  'Medium (Acceptable)': '55%',
  'Strong (Highly Secure)': '80%',
  'Excellent (Enterprise Grade)': '100%'
};
const SM={
  'IMMEDIATE FAIL (Weak Policy)': '🔴 IMMEDIATE FAIL (Weak Policy)',
  'Weak (Needs Hardening)': '🔴 WEAK (Needs Hardening)',
  'Medium (Acceptable)': '🟡 MEDIUM (Acceptable)',
  'Strong (Highly Secure)': '🔵 STRONG (Highly Secure)',
  'Excellent (Enterprise Grade)': '🟢 EXCELLENT (Enterprise Grade)'
};
const SCLS={
  'IMMEDIATE FAIL (Weak Policy)': 'cv-red',
  'Weak (Needs Hardening)': 'cv-red',
  'Medium (Acceptable)': 'cv-yellow',
  'Strong (Highly Secure)': 'cv-cyan',
  'Excellent (Enterprise Grade)': 'cv-green'
};
const CIRC=2*Math.PI*52; // ≈326.73

/* ═══════════════════════════════════════════════════════
   DOM REFS
   ══════════════════════════════════════════════════════ */
const $=id=>document.getElementById(id);
const pwdInput=$('pwdInput'), toggleBtn=$('togglePwd'), analyzeBtn=$('analyzeBtn');
const generateBtn=$('generateBtn'), strengthBar=$('strengthBar'), strengthTxt=$('strengthText');
const charCount=$('charCount'), genBar=$('genBar'), genPwdText=$('genPwdText'), copyBtn=$('copyBtn');
const modalOverlay=$('modalOverlay'), scoreCounter=$('scoreCounter'), scoreRing=$('scoreRing');
const crackVal=$('crackVal'), hibpVal=$('hibpVal'), strengthLbl=$('strengthLbl');
const entropyTxt=$('entropyTxt'), entropyFill=$('entropyFill');
const diversityTxt=$('diversityTxt'), diversityFill=$('diversityFill');
const checksGrid=$('checksGrid'), recsDiv=$('recsDiv'), exportBtn=$('exportBtn');

let visible=false;
toggleBtn.addEventListener('click',()=>{
  visible=!visible;
  pwdInput.type=visible?'text':'password';
  toggleBtn.textContent=visible?'🙈':'👁️';
});

/* Live strength bar */
pwdInput.addEventListener('input',()=>{
  const pwd=pwdInput.value;
  charCount.textContent=pwd.length;
  const r=analyzePassword(pwd);
  if(!r){strengthBar.style.width='0%';strengthTxt.textContent='—';strengthTxt.style.color='';return;}
  strengthBar.style.width=SW[r.strength];
  strengthBar.style.background=SC[r.strength];
  strengthTxt.textContent=r.strength;
  strengthTxt.style.color=SC[r.strength];
});

/* Generate */
generateBtn.addEventListener('click',()=>{
  const pwd=generatePassword();
  pwdInput.value=pwd; pwdInput.type='text'; visible=true; toggleBtn.textContent='🙈';
  genPwdText.textContent=pwd; genBar.classList.add('show');
  charCount.textContent=pwd.length;
  pwdInput.dispatchEvent(new Event('input'));
});

/* Copy */
copyBtn.addEventListener('click',async()=>{
  try{
    await navigator.clipboard.writeText(pwdInput.value);
    copyBtn.textContent='✅ Copied!'; setTimeout(()=>copyBtn.textContent='📋 Copy',2000);
  }catch(e){ copyBtn.textContent='❌ Failed'; setTimeout(()=>copyBtn.textContent='📋 Copy',2000); }
});

/* Analyze */
let curAnalysis=null, curPwd='';

analyzeBtn.addEventListener('click',async()=>{
  const pwd=pwdInput.value;
  if(!pwd){pwdInput.focus();return;}
  analyzeBtn.classList.add('loading');
  await new Promise(r=>setTimeout(r,950));
  const r=analyzePassword(pwd);
  curAnalysis=r; curPwd=pwd;
  analyzeBtn.classList.remove('loading');
  openModal(r,pwd);
});

pwdInput.addEventListener('keydown',e=>{ if(e.key==='Enter') analyzeBtn.click(); });

function openModal(r,pwd){
  /* Reset */
  scoreCounter.textContent='0';
  scoreRing.style.strokeDashoffset=CIRC;
  scoreRing.style.stroke=SC[r.strength];
  hibpVal.innerHTML='<div class="hibp-loading"><div class="hibp-spin"></div>Checking breach database…</div>';

  modalOverlay.classList.add('open');
  document.body.style.overflow='hidden';

  /* Donut + counter */
  setTimeout(()=>{
    scoreRing.style.strokeDashoffset=CIRC*(1-r.score/100);
    animCounter(scoreCounter,r.score,1100);
    scoreCounter.style.color=SC[r.strength];
  },120);

  /* Strength label */
  strengthLbl.textContent=SM[r.strength];
  strengthLbl.className='mcard-val '+SCLS[r.strength];

  /* Crack time */
  crackVal.textContent=crackTime(pwd,r.charset);

  /* Bars */
  setTimeout(()=>{
    entropyTxt.textContent=r.entropy+' bits — '+(r.entropy<40?'Low':r.entropy<70?'Medium':'High');
    entropyFill.style.width=Math.min(100,(r.entropy/128)*100)+'%';
    diversityTxt.textContent=r.diversity+'% ('+r.unique+' unique / '+r.length+' total)';
    diversityFill.style.width=r.diversity+'%';
  },180);

  /* Checks */
  const CHECKS=[
    {k:'length',   icon:'📏',name:'8+ Characters',        sub:'Minimum secure length'},
    {k:'uppercase',icon:'🔠',name:'Uppercase Letters',    sub:'Contains A–Z'},
    {k:'lowercase',icon:'🔡',name:'Lowercase Letters',    sub:'Contains a–z'},
    {k:'digit',    icon:'🔢',name:'Numeric Digits',       sub:'Contains 0–9'},
    {k:'special',  icon:'⚡',name:'Special Characters',   sub:'!@#$%^&* etc.'},
    {k:'notCommon',icon:'🛡️',name:'Not Common Password', sub:'Not in top breached list'},
    {k:'noRepeat', icon:'🔄',name:'No Repeated Chars',    sub:'Avoids aaa, 111 patterns'},
    {k:'noSeq',    icon:'📶',name:'No Sequential Pattern',sub:'Avoids 1234, abc, qwerty'},
  ];
  checksGrid.innerHTML=CHECKS.map(c=>`
    <div class="chk ${r.checks[c.k]?'pass':'fail'}">
      <div class="chk-icon">${c.icon}</div>
      <div>
        <div class="chk-name">${c.name}</div>
        <div class="chk-sub">${c.sub}</div>
      </div>
    </div>`).join('');

  /* Recommendations */
  const tips=[];
  if(!r.checks.length)    tips.push('Critical: Password must be at least 8 characters long.');
  else if(r.length < 12)  tips.push('Recommend: Increase length to 12+ characters for exponential brute-force resistance.');
  
  if(!r.checks.uppercase) tips.push('Mandatory: Add at least one uppercase letter [A-Z].');
  if(!r.checks.lowercase) tips.push('Mandatory: Add at least one lowercase letter [a-z].');
  if(!r.checks.digit)     tips.push('Mandatory: Add at least one decimal digit [0-9].');
  if(!r.checks.special)   tips.push('Mandatory: Add at least one symbol or special character.');
  
  if(!r.checks.notCommon) tips.push('Critical: Avoid highly common or leaked passwords.');
  if(!r.checks.noRepeat)  tips.push('Avoid repeating the same character 3 or more times.');
  if(!r.checks.noSeq)     tips.push('Avoid sequential patterns (123, abc, qwerty, etc.).');
  
  recsDiv.innerHTML=tips.length===0
    ? '<div class="rec good">🎉 Excellent! Your password meets all security requirements.</div>'
    : tips.map(t=>`<div class="rec">⚠️ ${t}</div>`).join('');

  /* HIBP async */
  checkHIBP(pwd).then(res=>{
    if(res.error)
      hibpVal.innerHTML='<div class="mcard-val cv-yellow">⚠️ Unavailable (requires internet)</div>';
    else if(res.pwned)
      hibpVal.innerHTML=`<div class="mcard-val cv-red">🚨 FOUND IN ${res.count.toLocaleString()} BREACHES</div>`;
    else
      hibpVal.innerHTML='<div class="mcard-val cv-green">✅ NOT FOUND IN BREACH DATABASE</div>';
  });
}

/* Close modal */
function closeModal(){
  $('modalOverlay').classList.remove('open');
  document.body.style.overflow='';
}
$('closeModal').addEventListener('click',closeModal);
$('modalOverlay').addEventListener('click',e=>{ if(e.target===$('modalOverlay')) closeModal(); });

/* ═══════════════════════════════════════════════════════
   EXPORT PDF REPORT (print-to-PDF via new window)
   ══════════════════════════════════════════════════════ */
exportBtn.addEventListener('click',()=>{
  if(!curAnalysis) return;
  const r=curAnalysis, pwd=curPwd;
  const masked=pwd.slice(0,2)+'•'.repeat(Math.max(0,pwd.length-4))+pwd.slice(-2);
  const now=new Date().toLocaleString('en-IN',{timeZone:'Asia/Kolkata'});
  const ct=crackTime(pwd,r.charset);

  const CHECKS=[
    ['length','📏','8+ Characters'],['uppercase','🔠','Uppercase Letters'],
    ['lowercase','🔡','Lowercase Letters'],['digit','🔢','Numeric Digits'],
    ['special','⚡','Special Characters'],['notCommon','🛡️','Not Common Password'],
    ['noRepeat','🔄','No Repeated Chars'],['noSeq','📶','No Sequential Patterns'],
  ];
  const tips=[];
  if(!r.checks.length)    tips.push('Increase password length to at least 8 characters.');
  else if(r.length < 12)  tips.push('Increase length to 12+ characters for exponential resistance.');
  
  if(!r.checks.uppercase) tips.push('Add uppercase letters (A–Z).');
  if(!r.checks.lowercase) tips.push('Add lowercase letters (a–z).');
  if(!r.checks.digit)     tips.push('Include at least one digit (0–9).');
  if(!r.checks.special)   tips.push('Add special characters like !@#$%^&*.');
  if(!r.checks.noRepeat)  tips.push('Avoid repeating the same character 3+ times.');
  if(!r.checks.noSeq)     tips.push('Avoid sequential patterns (123, abc, qwerty).');
  if(!r.checks.notCommon) tips.push('⚠️ This password has been seen in known data breaches!');

  const scColor={
    'IMMEDIATE FAIL (Weak Policy)':'#dc2626',
    'Weak (Needs Hardening)':'#dc2626',
    'Medium (Acceptable)':'#d97706',
    'Strong (Highly Secure)':'#0891b2',
    'Excellent (Enterprise Grade)':'#16a34a'
  }[r.strength];

  const scBg={
    'IMMEDIATE FAIL (Weak Policy)':'#fee2e2',
    'Weak (Needs Hardening)':'#fee2e2',
    'Medium (Acceptable)':'#fef3c7',
    'Strong (Highly Secure)':'#cffafe',
    'Excellent (Enterprise Grade)':'#dcfce7'
  }[r.strength];

  const win=window.open('','_blank');
  win.document.write(`<!DOCTYPE html><html><head>
<title>Cyber Gatekeeper – Security Report</title>
<style>
  body{font-family:Arial,sans-serif;padding:48px;max-width:720px;margin:0 auto;color:#1e293b;font-size:14px;}
  .logo{display:flex;align-items:center;gap:12px;margin-bottom:6px;}
  .logo h1{font-size:22px;color:#0369a1;margin:0;}
  .sub{color:#64748b;font-size:12px;margin-bottom:20px;}
  .badge{display:inline-block;padding:5px 16px;border-radius:99px;font-weight:700;font-size:12px;
    margin-bottom:20px;background:${scBg};color:${scColor};}
  .score-row{display:flex;align-items:flex-end;gap:16px;margin-bottom:20px;}
  .score-num{font-size:60px;font-weight:900;color:${scColor};line-height:1;}
  .score-label{font-size:13px;color:#64748b;padding-bottom:10px;}
  hr{border:none;border-top:1px solid #e2e8f0;margin:20px 0;}
  .grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px;}
  .metric{background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:13px;}
  .ml{font-size:10px;color:#94a3b8;text-transform:uppercase;letter-spacing:1px;margin-bottom:5px;}
  .mv{font-size:15px;font-weight:700;color:#1e293b;}
  h3{font-size:14px;color:#334155;margin:18px 0 10px;text-transform:uppercase;letter-spacing:1px;}
  .chk{display:flex;align-items:center;gap:10px;padding:9px 12px;border-radius:8px;margin-bottom:6px;font-size:13px;}
  .chk.p{background:#f0fdf4;border:1px solid #bbf7d0;}
  .chk.f{background:#fef2f2;border:1px solid #fecaca;}
  .rec{background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:9px 13px;margin-bottom:6px;color:#92400e;}
  .rec.g{background:#f0fdf4;border-color:#bbf7d0;color:#166534;}
  .footer{font-size:11px;color:#94a3b8;text-align:center;margin-top:36px;padding-top:16px;border-top:1px solid #e2e8f0;}
</style></head><body>
<div class="logo"><span style="font-size:28px">🛡️</span><h1>CYBER GATEKEEPER</h1></div>
<div class="sub">Advanced Password Security Report &nbsp;·&nbsp; ${now}</div>
<div class="badge">${r.strength}</div>
<div class="score-row">
  <div class="score-num">${r.score}</div>
  <div class="score-label">Security Score<br/><span style="font-size:18px;color:#94a3b8">/100</span></div>
</div>
<p style="color:#64748b;font-size:12px;margin-bottom:6px;">Password analyzed: <code>${masked}</code> &nbsp;(${r.length} characters)</p>
<hr/>
<div class="grid">
  <div class="metric"><div class="ml">⏱ Crack Time</div><div class="mv">${ct}</div></div>
  <div class="metric"><div class="ml">🔢 Entropy</div><div class="mv">${r.entropy} bits</div></div>
  <div class="metric"><div class="ml">📊 Unique Chars</div><div class="mv">${r.unique} / ${r.length}</div></div>
  <div class="metric"><div class="ml">📈 Diversity</div><div class="mv">${r.diversity}%</div></div>
</div>
<hr/>
<h3>Security Checks</h3>
${CHECKS.map(([k,ic,nm])=>`<div class="chk ${r.checks[k]?'p':'f'}">${r.checks[k]?'✅':'❌'}&nbsp; <strong>${ic} ${nm}</strong></div>`).join('')}
<hr/>
<h3>Recommendations</h3>
${tips.length===0
  ? '<div class="rec g">🎉 Excellent! Password meets all security requirements.</div>'
  : tips.map(t=>`<div class="rec">⚠️ ${t}</div>`).join('')}
<div class="footer">
  Cyber Gatekeeper v3.0 · DecodeLabs Internship Project 2026 · Powered by HaveIBeenPwned API<br/>
  This report was auto-generated and is for educational purposes only.
</div>
</body></html>`);
  win.document.close();
  setTimeout(()=>win.print(),700);
});
