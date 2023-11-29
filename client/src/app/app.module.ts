import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { NzGridModule } from 'ng-zorro-antd/grid';
import { HttpClientModule } from '@angular/common/http';

import { MatStepperModule } from '@angular/material/stepper';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MapboxComponent } from './modules/mapbox/mapbox.component';
import { HomeComponent } from './modules/home/home.component';
import { NavbarComponent } from './shared/navbar/navbar.component';
import { EarthAnimationComponent } from './modules/earth-animation/earth-animation.component';
import { CarouselComponent } from './modules/carousel/carousel.component';
import { FormComponent } from './modules/form/form.component';
import { FormBuilder, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { LoaderComponent } from './shared/loader/loader.component';
import { FooterComponent } from './shared/footer/footer.component';
import { EarthquakeViewComponent } from './modules/earthquake-view/earthquake-view.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AsyncPipe } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatRadioModule } from '@angular/material/radio';
import { MapChartComponent } from './modules/map-chart/map-chart.component';

@NgModule({
  declarations: [
    AppComponent,
    MapboxComponent,
    HomeComponent,
    NavbarComponent,
    EarthAnimationComponent,
    CarouselComponent,
    FormComponent,
    LoaderComponent,
    FooterComponent,
    EarthquakeViewComponent,
    MapChartComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NzGridModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,  
    MatStepperModule,
    BrowserAnimationsModule, 
    ReactiveFormsModule,
    MatStepperModule,
    FormsModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    AsyncPipe,
    MatRadioModule,
    MatButtonModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
