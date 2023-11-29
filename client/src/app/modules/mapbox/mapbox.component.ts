import { AfterViewInit, Component, ElementRef, OnInit, Renderer2 } from '@angular/core';
import { EarthquakeService } from 'src/app/core/services/earthquake.service';
import * as L from 'leaflet';
import * as bootstrap from 'bootstrap';
import { Router } from '@angular/router';

@Component({
  selector: 'app-mapbox',
  templateUrl: './mapbox.component.html',
  styleUrls: ['./mapbox.component.css'],
})
export class MapboxComponent implements AfterViewInit, OnInit {
  private map: any;

  currentPage = 1;
  itemsPerPage = 20;

  magnitude_thresholds = {
    "Very High": 7.0,
    "High": 6.0,
    "Medium": 5.0,
    "Low": 3.0,
    "Very Low": 0.0,
  };


  showTable: boolean = false;
  latitude: number = 6.267268249530994;
  longitude: number = -75.568882901833;
  isLoading: boolean = false;

  earthquakes: any[] = [];
  private initMap(): void {
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
    );

    tiles.addTo(this.map);
  }

  private showModal() {
    const modalElement = this.elementRef.nativeElement.querySelector('#exampleModal');
    const modal = new bootstrap.Modal(modalElement);
    modal.show();
  }

  constructor(
    private earthquakeSvc: EarthquakeService,
    private router: Router,
    private elementRef: ElementRef,
  ) {}

  ngOnInit(): void {
    this.showModal();
  }

  ngAfterViewInit(): void {
    this.initMap();

    const marker = L.marker([this.latitude, this.longitude], {
      draggable: true, // Set the draggable option to true
    }).addTo(this.map);

    marker.on('dragend', (e) => {
      this.latitude = marker.getLatLng().lat;
      this.longitude = marker.getLatLng().lng;
      // console.log(this.latitude, this.longitude);
    });
  }

  setCurrentPage(page: number): void {
    if (page >= 1 && page <= this.getTotalPages()) {
      this.currentPage = page;
    }
  }
  
  getTotalPages(): number {
    return Math.ceil(this.earthquakes.length / this.itemsPerPage);
  }
  
  getPages(): number[] {
    return Array.from({ length: this.getTotalPages() }, (_, i) => i + 1);
  }
  

  send() {
    this.isLoading = true;
    this.earthquakeSvc
      .getEarthquakesNear(this.latitude, this.longitude, 50)
      .subscribe(
        (data) => {
          //console.log(data);
          this.earthquakes = data;
          this.isLoading = false;
          this.showTable = true;
          console.log(this.isLoading)
        },
        (error) => {
          console.error('Error fetching earthquake data:', error);
          this.isLoading = false; // Make sure to stop the loader in case of an error
        }
      );
  }

  getEarthquake(id: number) {
    this.earthquakeSvc.getEarthquake(id).subscribe((data) => {
      this.router.navigate(['/earthquake-view', id]);
    });
  }
}
