import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/app/environments/environments';
import { Form } from '../interfaces/form';

@Injectable({
  providedIn: 'root',
})
export class EarthquakeService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  // Define a method to get earthquakes near a location
  getEarthquakesNear(latitude: number, longitude: number, limit:number): Observable<any[]> {
    const url = `${this.apiUrl}earthquakes/near/${limit}/${latitude}/${longitude}`;
    return this.http.get<any[]>(url);
  }

  getEarthquake(id: number): Observable<any> {
    const url = `${this.apiUrl}earthquakes/${id}`;
    return this.http.get<any>(url);
  }

  calculateEarthquakeProbability(
    modelAnswers: Form, 
    userLatitude: number,
    userLongitude: number
  ): Observable<any> {
    const endpoint = `earthquakes/calculate_earthquake_probability/${userLatitude}/${userLongitude}`;
    const url = `${this.apiUrl}${endpoint}`;

    return this.http.post<any>(url, modelAnswers);
  }

  getEarthquakeProbability(
    userLatitude: number,
    userLongitude: number,
    limit: number
  ): Observable<any> {
    const url = `${this.apiUrl}earthquakes/near/${limit}/${userLatitude}/${userLongitude}/probability`;
    return this.http.get(url);
  }

}
