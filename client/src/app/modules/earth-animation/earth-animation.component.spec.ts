import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EarthAnimationComponent } from './earth-animation.component';

describe('EarthAnimationComponent', () => {
  let component: EarthAnimationComponent;
  let fixture: ComponentFixture<EarthAnimationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EarthAnimationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EarthAnimationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
