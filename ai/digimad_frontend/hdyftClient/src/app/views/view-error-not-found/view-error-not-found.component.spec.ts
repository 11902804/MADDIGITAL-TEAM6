import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewErrorNotFoundComponent } from './view-error-not-found.component';

describe('ViewErrorNotFoundComponent', () => {
  let component: ViewErrorNotFoundComponent;
  let fixture: ComponentFixture<ViewErrorNotFoundComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ViewErrorNotFoundComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewErrorNotFoundComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
