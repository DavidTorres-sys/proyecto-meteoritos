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

  ngOnInit(): void {
    this.map = new mapboxgl.Map({
      accessToken: environment.mapboxKey,
      container: 'map', // Use 'map' as the container ID
      style: 'mapbox://styles/mapbox/streets-v12',
      center: [this.lng, this.lat], // Use the stored values
      zoom: 9,
    });

    this.marker(this.lng, this.lat);
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
    console.log('longitud', this.lng, 'latitud' ,this.lat);
    // You can use this.lng and this.lat here for further processing.
  }
}
