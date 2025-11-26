// effects.js
function createDrop(emoji, x, speed, size) {
  const root = document.getElementById('effectsRoot');
  if (!root) return;
  const el = document.createElement('div');
  el.className = 'emoji-drop';
  el.innerText = emoji;
  el.style.left = x + 'vw';
  el.style.top = '-5vh';
  el.style.fontSize = size + 'px';
  el.style.position = 'fixed';
  el.style.zIndex = 9999;
  el.style.pointerEvents = 'none';
  el.style.transition = `transform ${speed}s linear`;
  root.appendChild(el);
  setTimeout(()=> {
    el.style.transform = `translateY(110vh) rotate(${Math.random()*360}deg)`;
  }, 20);
  setTimeout(()=> { if (root.contains(el)) root.removeChild(el); }, (speed*1000)+200);
}

let snowInterval = null;
function startSnow(duration=4000) {
  stopEffects();
  snowInterval = setInterval(()=> {
    createDrop('❄️', Math.random()*100, 3 + Math.random()*3, 14 + Math.random()*10);
  }, 200);
  setTimeout(stopEffects, duration);
}

let skullInterval = null;
function startSkullRain(duration=4000) {
  stopEffects();
  skullInterval = setInterval(()=> {
    createDrop('💀', Math.random()*100, 2 + Math.random()*3, 20 + Math.random()*12);
  }, 180);
  setTimeout(stopEffects, duration);
}

function stopEffects() {
  if (snowInterval) { clearInterval(snowInterval); snowInterval = null; }
  if (skullInterval) { clearInterval(skullInterval); skullInterval = null; }
}
