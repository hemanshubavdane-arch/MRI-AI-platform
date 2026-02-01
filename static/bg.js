const c=document.getElementById("bg-canvas");
const x=c.getContext("2d");

function resize(){
  c.width=innerWidth;
  c.height=innerHeight;
}
resize();
addEventListener("resize",resize);

let p=[...Array(120)].map(()=>({
 x:Math.random()*c.width,
 y:Math.random()*c.height,
 vx:(Math.random()-.5)*.4,
 vy:(Math.random()-.5)*.4
}));

function animate(){
 x.clearRect(0,0,c.width,c.height);
 p.forEach(o=>{
  o.x+=o.vx;
  o.y+=o.vy;
  if(o.x<0||o.x>c.width)o.vx*=-1;
  if(o.y<0||o.y>c.height)o.vy*=-1;
  x.beginPath();
  x.arc(o.x,o.y,2.3,0,7);
  x.fillStyle="rgba(56,189,248,.35)";
  x.fill();
 });
 requestAnimationFrame(animate);
}
animate();
