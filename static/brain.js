const scene=new THREE.Scene();
const camera=new THREE.PerspectiveCamera(45,1,0.1,1000);
camera.position.z=4;

const renderer=new THREE.WebGLRenderer({alpha:true,antialias:true});
renderer.setSize(340,340);
document.getElementById("brain3d")?.appendChild(renderer.domElement);

const geo=new THREE.IcosahedronGeometry(1.3,6);
const mat=new THREE.MeshPhysicalMaterial({
 color:0x9ddcff,
 transmission:0.45,
 roughness:0.2,
 metalness:0.1,
 clearcoat:1
});

const brain=new THREE.Mesh(geo,mat);
scene.add(brain);

scene.add(new THREE.AmbientLight(0xffffff,.9));
const light=new THREE.PointLight(0x38bdf8,2);
light.position.set(3,3,3);
scene.add(light);

let t=0;
function animate(){
 requestAnimationFrame(animate);
 t+=0.01;
 brain.rotation.y+=0.003;
 brain.rotation.x+=0.002;
 brain.position.y=Math.sin(t)*0.08;
 renderer.render(scene,camera);
}
animate();
