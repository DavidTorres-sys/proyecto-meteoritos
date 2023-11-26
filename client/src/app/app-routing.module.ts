import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MapboxComponent } from './modules/mapbox/mapbox.component';
import { HomeComponent } from './modules/home/home.component';
import { FormComponent } from './modules/form/form.component';
import { EarthquakeViewComponent } from './modules/earthquake-view/earthquake-view.component';
import { MapChartComponent } from './modules/map-chart/map-chart.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
  },
  {
    path: 'home',
    component: HomeComponent,
  },
  {
    path: 'form',
    component: FormComponent,
  },
  {
    path: 'mapbox',
    component: MapboxComponent,
  },
  {
    path: 'earthquake-view/:id',
    component: EarthquakeViewComponent,
  },
  {
    path: 'map-chart',
    component: MapChartComponent,
  },
  {
    path: '**',
    redirectTo: 'home',
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
