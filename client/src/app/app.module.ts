import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { NzGridModule } from 'ng-zorro-antd/grid';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MapboxComponent } from './modules/mapbox/mapbox.component';
import { HomeComponent } from './modules/home/home.component';
import { NavbarComponent } from './shared/navbar/navbar.component';
import { EarthAnimationComponent } from './modules/earth-animation/earth-animation.component';

@NgModule({
  declarations: [
    AppComponent,
    MapboxComponent,
    HomeComponent,
    NavbarComponent,
    EarthAnimationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NzGridModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
