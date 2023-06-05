// esm

import { Three } from 'three';

class SimpleArray {

  constructor() {
    this.numbers = new Array(5);
    this.numbers[0] = 10;
    this.numbers[1] = 20;
    this.numbers[2] = 30;
    this.numbers[3] = 40;
    this.numbers[4] = 50;
  }

  render() {
    for (let i = 0; i < this.numbers.length; i++) {
      let number = this.numbers[i];
      let text = document.createElement('text');
      text.textContent = number.toString();
      text.position.set(i, 0, 0);
      scene.add(text);
    }
  }
}

var scene = new Scene();
var camera = new PerspectiveCamera(75, innerWidth / innerHeight, 1, 1000);
var renderer = new WebGLRenderer();
renderer.setSize(innerWidth, innerHeight);
document.body.appendChild(renderer.domElement);

var array = new SimpleArray();

function animate() {
  requestAnimationFrame(animate);
  array.render();
}

animate();
