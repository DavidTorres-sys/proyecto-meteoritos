import { Component, Input, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-loader',
  templateUrl: './loader.component.html',
  styleUrls: ['./loader.component.css']
})
export class LoaderComponent implements OnDestroy{
  @Input() loading: boolean = false;

  constructor() { 
    console.log('LoaderComponent');
  }

  ngOnDestroy(): void {
    this.loading = false;
  }
}
