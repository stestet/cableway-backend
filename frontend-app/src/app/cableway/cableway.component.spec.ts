import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CablewayComponent } from './cableway.component';

describe('CablewayComponent', () => {
  let component: CablewayComponent;
  let fixture: ComponentFixture<CablewayComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CablewayComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CablewayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
