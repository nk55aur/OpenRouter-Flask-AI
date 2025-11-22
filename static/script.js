const form = document.getElementById('inputForm');
const input = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const outputEl = document.getElementById('output');

function setRobotThinking(on){
  const svg = document.getElementById('robot');
  if(!svg) return;
  if(on){
    svg.classList.add('robot-thinking');
  }else{
    svg.classList.remove('robot-thinking');
  }
}

function sleep(ms){return new Promise(r=>setTimeout(r,ms));}

async function typeEffect(el, text, interval=12){
  el.textContent = '';
  for(let i=0;i<text.length;i++){
    el.textContent += text[i];
    el.scrollTop = el.scrollHeight;
    await sleep(interval);
  }
}

async function sendMessage(msg){
  if(!msg) return;
  outputEl.textContent = '';
  setRobotThinking(true);
  sendBtn.disabled = true;

  try{
    const res = await fetch('/api/ask', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({user_input: msg})});
    const data = await res.json();
    const text = data.result || data.error || 'No response';
    await typeEffect(outputEl, text, 12);
  }catch(err){
    outputEl.textContent = '⚠️ Error: could not reach server';
  }finally{
    setRobotThinking(false);
    sendBtn.disabled = false;
  }
}

form.addEventListener('submit', e=>{
  e.preventDefault();
  const v = input.value.trim();
  if(!v) return;
  sendMessage(v);
});

// Expand textarea vertically as user types
input.addEventListener('input', ()=>{
  input.style.height = 'auto';
  input.style.height = Math.min(280, input.scrollHeight) + 'px';
});

document.addEventListener('DOMContentLoaded', ()=>{
  outputEl.textContent = 'Ready — type something and press Send.';
});
