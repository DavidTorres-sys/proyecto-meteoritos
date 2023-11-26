import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import * as L from 'leaflet';
import { EarthquakeService } from 'src/app/core/services/earthquake.service';

@Component({
  selector: 'app-earthquake-view',
  templateUrl: './earthquake-view.component.html',
  styleUrls: ['./earthquake-view.component.css'],
})
export class EarthquakeViewComponent implements OnInit {
  private map: any;
  isLoading: boolean = false;
  id: number = 0;
  latitude: number = 0;
  longitude: number = 0;
  earthquake: any;

  magnitude_thresholds = {
    "Very High": 7.0,
    "High": 6.0,
    "Medium": 5.0,
    "Low": 3.0,
    "Very Low": 0.0,
  };

  constructor(
    private earthquakeSvc: EarthquakeService,
    private route: ActivatedRoute
  ) {
    this.isLoading = true;
  }

  ngOnInit(): void {
    this.loadEarthquakeDetails();
  }

  private initMap(): void {
    if (!this.map) {
      this.map = L.map('map', {
        center: [this.latitude, this.longitude],
        zoom: 5,
      });

      const tiles = L.tileLayer(
        'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        {
          maxZoom: 18,
          minZoom: 3,
          attribution:
            '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        }
      ).addTo(this.map);
    }
  }

  private loadEarthquakeDetails() {
    const earthquakeId = this.route.snapshot.paramMap?.get('id');
    if (earthquakeId) {
      const id = parseInt(earthquakeId, 10); // Convert string to number
      
      this.earthquakeSvc.getEarthquake(id).subscribe(

        (data) => {
          this.latitude = data.location_earthquake[0].latitude;
          this.longitude = data.location_earthquake[0].longitude;
          this.earthquake = data;
          console.log('Earthquake details:', this.earthquake);
          this.initMap();
          const marker = L.marker([this.latitude, this.longitude], {
            draggable: false,
          }).addTo(this.map);
        },
        (error) => {
          console.error('Error fetching earthquake details:', error);
          this.isLoading = false;
        }
      );
    }
    this.isLoading = false;
  }
}
