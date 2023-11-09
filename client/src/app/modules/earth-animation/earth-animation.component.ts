import { Component, NgZone, OnInit } from '@angular/core';
import * as THREE from 'three';

@Component({
  selector: 'app-earth-animation',
  templateUrl: './earth-animation.component.html',
  styleUrls: ['./earth-animation.component.css'],
})
export class EarthAnimationComponent implements OnInit {
  private scene: THREE.Scene;
  private camera!: THREE.PerspectiveCamera;
  private renderer!: THREE.WebGLRenderer;
  private earthMesh!: THREE.Mesh;
  private pointLight!: THREE.PointLight;
  private isDragging = false;
  private previousMousePosition = {
    x: 0,
    y: 0,
  };

  constructor(private ngZone: NgZone) {
    this.scene = new THREE.Scene();
  }

  ngOnInit() {
    this.initScene();
    this.createStarfield();
    this.createEarth();
    this.addLights();
  }

  createStarfield() {
    const starGeometry = new THREE.BufferGeometry();
    const starMaterial = new THREE.PointsMaterial({
      color: 0xffffff,
      size: 0.02, // Adjust the size of stars
      transparent: true,
    });

    const starVertices = [];

    // Generate random star positions
    for (let i = 0; i < 1000; i++) {
      const x = (Math.random() - 0.5) * 2000;
      const y = (Math.random() - 0.5) * 2000;
      const z = (Math.random() - 0.5) * 2000;
      starVertices.push(x, y, z);
    }

    starGeometry.setAttribute(
      'position',
      new THREE.Float32BufferAttribute(starVertices, 3)
    );

    const starfield = new THREE.Points(starGeometry, starMaterial);
    this.scene.add(starfield);
  }

  initScene() {
    // Set up the camera
    this.camera = new THREE.PerspectiveCamera(
      75,
      window.innerWidth / window.innerHeight,
      0.1,
      1000
    );
    this.camera.position.set(0, 0, 5);

    // Set up the renderer
    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    this.renderer.shadowMap.enabled = true;
    this.renderer.shadowMap.type = THREE.PCFSoftShadowMap; // Soft shadows
    document.body.appendChild(this.renderer.domElement);
    const canvas = this.renderer.domElement;

    canvas.addEventListener(
      'mousedown',
      (event) => this.onMouseDown(event),
      false
    );
    canvas.addEventListener(
      'mousemove',
      (event) => this.onMouseMove(event),
      false
    );
    canvas.addEventListener('mouseup', () => this.onMouseUp(), false);
  }

  onMouseDown(event: MouseEvent) {
    this.isDragging = true;
    this.previousMousePosition = {
      x: event.clientX,
      y: event.clientY,
    };
  }

  onMouseMove(event: MouseEvent) {
    if (this.isDragging) {
      const deltaX = event.clientX - this.previousMousePosition.x;
      const deltaY = event.clientY - this.previousMousePosition.y;

      this.earthMesh.rotation.x += deltaY * 0.001;
      this.earthMesh.rotation.y += deltaX * 0.001;

      this.previousMousePosition = {
        x: event.clientX,
        y: event.clientY,
      };
    }
  }

  onMouseUp() {
    this.isDragging = false;
  }

  createEarth() {
    const textureLoader = new THREE.TextureLoader();
    const earthTexture = textureLoader.load('/assets/earth.jpg');
    const geometry = new THREE.SphereGeometry(2, 32, 32);
    const material = new THREE.MeshStandardMaterial({
      map: earthTexture,
    });

    this.earthMesh = new THREE.Mesh(geometry, material);
    this.earthMesh.receiveShadow = true;
    this.earthMesh.castShadow = true;

    this.scene.add(this.earthMesh);

    this.animate();
  }

  addLights() {
    // Create a single point light
    this.pointLight = new THREE.PointLight(0xffffff, 200, 100);
    this.pointLight.position.set(5, 5, 5);
    this.pointLight.castShadow = true;
    this.scene.add(this.pointLight);

    // Optionally, you can add ambient light for additional overall illumination
    const ambientLight = new THREE.AmbientLight(0x000000); // Soft grayish light
    this.scene.add(ambientLight);
  }

  animate() {
    this.ngZone.run(() => {
      requestAnimationFrame(() => this.animate());
    });

    this.earthMesh.rotation.y += 0.001;
    this.renderer.render(this.scene, this.camera);
  }
}
