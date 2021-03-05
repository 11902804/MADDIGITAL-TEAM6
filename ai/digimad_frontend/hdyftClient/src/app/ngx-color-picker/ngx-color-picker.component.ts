import { Component, OnInit, ViewChild } from '@angular/core';
import { Subject } from 'rxjs';
import { debounceTime } from 'rxjs/operators';
import { NgbAlert } from '@ng-bootstrap/ng-bootstrap';

import { LightService } from '../services/light.service';
import { ColorService } from '../services/color.service';
declare var require: any;

var hexToHsl = require('hex-to-hsl');

@Component({
  selector: 'app-ngx-color-picker',
  templateUrl: './ngx-color-picker.component.html',
  styleUrls: ['./ngx-color-picker.component.css'],
})
export class NgxColorPickerComponent implements OnInit {
  public color: string = '#dbf7d9';
  public colorHSL: string[];
  public colorName: string;

  private _success = new Subject<string>();
  private _error = new Subject<string>();

  staticAlertClosed = false;
  successMessage = '';
  errorMessage = '';

  @ViewChild('staticAlert', { static: false }) staticAlert: NgbAlert;
  @ViewChild('selfClosingAlert', { static: false }) selfClosingAlert: NgbAlert;
  @ViewChild('selfClosingErrorAlert', { static: false }) selfClosingErrorAlert: NgbAlert;

  constructor(
    private lightService: LightService,
    private colorService: ColorService
  ) {}

  ngOnInit(): void {
    setTimeout(() => this.staticAlert.close(), 20000);

    this._success.subscribe((message) => (this.successMessage = message));
    this._success.pipe(debounceTime(2000)).subscribe(() => {
      console.log('Color saved:', this.color);
      console.log('Color HSL: ', this.colorHSL);
      if (this.selfClosingAlert) {
        this.selfClosingAlert.close();
      }
    });

    this._error.subscribe((message) => (this.errorMessage = message));
    this._error.pipe(debounceTime(2000)).subscribe(() => {
      if (this.selfClosingErrorAlert) {
        this.selfClosingErrorAlert.close();
      }
    });
  }

  public changeSuccessMessage() {
    this.colorService.createColor(this.colorName, this.color).subscribe(
      (res: any) => {
        this._success.next(`Your color has been saved!`);
      },
      (err) => {
        this._error.next('Something went wrong saving the color. Please try again!');
      }
    );
  }

  public onChangeColor(color: string): void {
    console.log('Color HEX: ', color);
    console.log('Hex to HSL: ', hexToHsl(color)); // Prints [206, 100, 51]
    this.colorHSL = hexToHsl(color);
    console.log('Color HSL: ', this.colorHSL);
    this.lightService.updateLight(this.colorHSL).subscribe(() => {
      console.log('succeeded!');
    });
  }
}
