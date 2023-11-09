import { Component, OnInit } from '@angular/core';
import { environment } from 'src/app/environments/environments';
import * as mapboxgl from 'mapbox-gl';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-mapbox',
  templateUrl: './mapbox.component.html',
  styleUrls: ['./mapbox.component.css'],
})
export class MapboxComponent implements OnInit {
  map: mapboxgl.Map | null = null;
  lng: number = -75.5700356; // Initialize with default values
  lat: number = 6.269942;
  isAtStart = true;

  ngOnInit(): void {
    // Initialize Mapbox

    this.map = new mapboxgl.Map({
      accessToken: environment.mapboxKey,
      container: 'map', // Use 'map' as the container ID
      style: 'mapbox://styles/mapbox/satellite-streets-v12',
      center: [this.lng, this.lat], // Set your initial center coordinates
      zoom: 1, // Set your initial zoom level
    });

    this.marker(this.lng, this.lat);

    this.map.on('style.load', () => {
      // Custom atmosphere styling
      this.map!.setFog({
        color: 'rgb(220, 159, 159)', // Pink fog / lower atmosphere
        'high-color': 'rgb(36, 92, 223)', // Blue sky / upper atmosphere
        'horizon-blend': 0.4, // Exaggerate atmosphere (default is .1)
      });

      this.map!.addSource('mapbox-dem', {
        type: 'raster-dem',
        url: 'mapbox://mapbox.terrain-rgb',
      });

      this.map!.setTerrain({
        source: 'mapbox-dem',
        exaggeration: 1.5,
      });
    });
  }

  marker(lng: number, lat: number) {
    const marker = new mapboxgl.Marker({
      draggable: true,
    })
      .setLngLat([lng, lat])
      .addTo(this.map!);

    marker.on('drag', () => {
      const lngLat = marker.getLngLat();
      this.lng = lngLat.lng; // Update the stored lng
      this.lat = lngLat.lat; // Update the stored lat
    });
  }

  send() {
    // Define start and end coordinates
    const start = {
      center: [this.lng, this.lat], // Replace with your actual coordinates
      zoom: 6, // Replace with your desired zoom level
    };

    const end = {
      center: [this.lng, this.lat], // Replace with your actual coordinates
      zoom: 6, // Replace with your desired zoom level
    };

    console.log('longitud', this.lng, 'latitud', this.lat);
    // You can use this.lng and this.lat here for further processing.
    // depending on whether we're currently at point a or b,
    // aim for point a or b
    const target = this.isAtStart ? end : start;
    this.isAtStart = !this.isAtStart;

    this.map!.flyTo({
      center: target.center as [number, number], // Cast center to [number, number]
      zoom: target.zoom,
      duration: 12000, // Animate over 12 seconds
      essential: true, // This animation is considered essential with
      // respect to prefers-reduced-motion
    });
  }
}
