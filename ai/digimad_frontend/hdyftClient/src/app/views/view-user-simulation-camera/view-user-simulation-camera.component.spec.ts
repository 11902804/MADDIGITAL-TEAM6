import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewUserSimulationCameraComponent } from './view-user-simulation-camera.component';

describe('ViewUserSimulationCameraComponent', () => {
  let component: ViewUserSimulationCameraComponent;
  let fixture: ComponentFixture<ViewUserSimulationCameraComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ViewUserSimulationCameraComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewUserSimulationCameraComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
