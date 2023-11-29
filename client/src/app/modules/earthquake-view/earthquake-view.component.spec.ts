import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EarthquakeViewComponent } from './earthquake-view.component';

describe('EarthquakeViewComponent', () => {
  let component: EarthquakeViewComponent;
  let fixture: ComponentFixture<EarthquakeViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EarthquakeViewComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EarthquakeViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
