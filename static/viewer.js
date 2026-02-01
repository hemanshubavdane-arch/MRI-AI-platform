const canvas = document.createElement("canvas");
canvas.width = 320;
canvas.height = 320;
canvas.style.borderRadius = "12px";
canvas.style.border = "1px solid #334155";

const container = document.getElementById("viewer");
if(container){
  container.appendChild(canvas);
}

const ctx = canvas.getContext("2d");

let t = 0;

function drawScan(){
  ctx.clearRect(0,0,320,320);

  // background
  ctx.fillStyle = "#020617";
  ctx.fillRect(0,0,320,320);

  // animated scan lines
  for(let i=0;i<20;i++){
    ctx.fillStyle = `rgba(56,189,248,${Math.random()*0.2})`;
    ctx.fillRect(
      Math.random()*320,
      (t+i*15)%320,
      320,
      2
    );
  }

  // center glow
  const g = ctx.createRadialGradient(160,160,20,160,160,140);
  g.addColorStop(0,"rgba(56,189,248,.25)");
  g.addColorStop(1,"transparent");

  ctx.fillStyle = g;
  ctx.beginPath();
  ctx.arc(160,160,140,0,Math.PI*2);
  ctx.fill();

  t+=1;
  requestAnimationFrame(drawScan);
}

drawScan();
