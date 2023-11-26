import { AfterViewInit, Component, ElementRef, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { BreakpointObserver } from '@angular/cdk/layout';
import * as L from 'leaflet';
import * as bootstrap from 'bootstrap';
import { EarthquakeService } from 'src/app/core/services/earthquake.service';
import { Form } from 'src/app/core/interfaces/form';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css'],
})
export class FormComponent implements OnInit, AfterViewInit{
  private map: any;
  formResponse: any;
  isLoading: boolean = false;    
  send:boolean = false;
  latitude: number = 6.267268249530994;
  longitude: number = -75.568882901833;

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
    private fb: FormBuilder,
    private earthquakeSvc: EarthquakeService,
    private elementRef: ElementRef,
  ) {
  }

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
      console.log(this.latitude, this.longitude);
    });
  }
  // Combine all form groups into a single form group
  public form = this.fb.group({
    housing_type: ['', Validators.required],
    emergency_resources: [false, Validators.required],
    evacuation_plan: [false, Validators.required],
    experience_emergency: [false, Validators.required],
    medical_conditions: [false, Validators.required],
    participation_drills: [false, Validators.required],
    comunication_device: [false, Validators.required],
  });

  submitForm() {
    this.send = true;
    this.isLoading = true;
    // Explicitly specify the type when calling the service method
    const formData: Form = {
      housing_type: this.form.value.housing_type ?? '',
      emergency_resources: !!this.form.value.emergency_resources,
      evacuation_plan: !!this.form.value.evacuation_plan,
      experience_emergency: !!this.form.value.experience_emergency,
      medical_conditions: !!this.form.value.medical_conditions,
      participation_drills: !!this.form.value.participation_drills,
      comunication_device: !!this.form.value.comunication_device,
    };
    console.log('Form data:', formData);
    this.earthquakeSvc
      .calculateEarthquakeProbability(
        formData,
        this.latitude,
        this.longitude
      )
      .subscribe(
        (response) => {
          // Handle the response from the service
          console.log('Earthquake probability calculated:', response);
          this.formResponse = response;
          this.isLoading = false;
        },
        (error) => {
          // Handle errors from the service
          console.error('Error calculating earthquake probability:', error);
          this.isLoading = false;
          this.send = false;
        }
      );
  }
}
