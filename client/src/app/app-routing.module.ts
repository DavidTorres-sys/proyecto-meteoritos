import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MapboxComponent } from './modules/mapbox/mapbox.component';
import { HomeComponent } from './modules/home/home.component';
import { FormComponent } from './modules/form/form.component';

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
    path: '**',
    redirectTo: 'home',
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
