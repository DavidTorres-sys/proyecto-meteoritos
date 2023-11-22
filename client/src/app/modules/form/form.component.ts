import { Component } from '@angular/core';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent {
  public labels = {
    formulario: '¿Qué medidas está tomando en caso de un terremoto?'
  }
}
