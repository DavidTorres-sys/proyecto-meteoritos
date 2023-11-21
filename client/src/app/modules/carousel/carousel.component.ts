import { Component } from '@angular/core';

@Component({
  selector: 'app-carousel',
  templateUrl: './carousel.component.html',
  styleUrls: ['./carousel.component.css']
})
export class CarouselComponent {
  public slides: any[] = [];

  public labels = {
    alaska: 'Alaska, USA (1964)',
    descripcion: 'Con una magnitud de 9.2, este terremoto afectó a Alaska y generó un tsunami que afectó la '
    + 'costa oeste de los Estados Unidos y otras áreas del Pacífico.',
  }

  constructor() {
    this.slides.push({
      src: 'assets/quakes/japon.jpg',
      nombre: 'Japón (2011)',
      descripcion: 'Un terremoto de magnitud 9.0 ocurrió frente a la costa de Japón, desencadenando un '
      + 'poderoso tsunami que afectó gravemente a la planta de energía nuclear de Fukushima y causó daños '
      + 'significativos en la región.',
    });
    this.slides.push({
      src: 'assets/quakes/valdivia.jpg',
      nombre: 'Valdivia, Chile (1960)',
      descripcion: 'Este es el terremoto más fuerte registrado en la historia, con una magnitud de 9.5. '
      + 'Además de los daños causados por el temblor en sí, un tsunami resultante afectó a áreas tan lejanas '
      + 'como Hawái, Japón y Filipinas.',
    });
  }
}
