import { Component, AfterViewInit } from '@angular/core';
import { ColorService } from '../services/color.service';
import { element } from 'protractor';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-predefined-color-table',
  templateUrl: './predefined-color-table.html',
  styleUrls: ['./predefined-color-table.css'],
})
export class PredefinedColorTableComponent implements AfterViewInit {
  title = 'PredefinedColorTable';
  colors: Array<any>;
  values: Array<any>;

  IdToColorNameMap: Map<string, string> = new Map();
  IdToColorValueMap: Map<string, string> = new Map();

  constructor(private colorService: ColorService) {
    this.colors = [];
    this.values = [];
  }

  ngAfterViewInit(): void {
    //get the colors
    this.colorService.getAllColors().subscribe((data: any[]) => {
      for (var object in data) {
        this.IdToColorNameMap.set(object, data[object][0]);
        this.IdToColorValueMap.set(object, data[object][1]);
        this.colors.push(data[object][0]);
        this.values.push(data[object][1]);
      }
    });

    //var colorArray: Array<string>;

    /*var colorIterator = this.ColorMap.values();
        var mapIndex = 0;
        for (let colorMapping of IdToColorNameMap){
            //var colorArray = colorMapping.split(',');
            for (let i = 1; i <= this.colors.length; i++){
                var colorDivId = "predefinedColorDiv"+ mapIndex;
                console.log(colorDivId);
                (<HTMLInputElement>document.getElementById(colorDivId)).style.backgroundColor = this.colors[i-1];
            }
            mapIndex++;
        } */
  }

  deletePredefinedColor($element_id: string): void {
    var inputId = 'colorInput' + $element_id.substring(12);
    var name = (<HTMLInputElement>document.getElementById(inputId)).value;
    if (confirm('Are you sure you want to delete ' + name)) {
      console.log(name);
      console.log('Deleting predefined color...');
      this.colorService.deleteColorByName(name).subscribe(
        (res: any) => {
          console.log('After deleting: ' + res);
        },
        (err: any) => {
          console.log('Something went wrong when deleting: ' + err);
        }
      );
      //reload page to show the changed colors
      //location.reload();
    }
  }

  saveNewNames($element_id: string): void {
    var oldName = this.colors[$element_id.substring(10)];
    var inputId = 'colorInput' + $element_id.substring(10);
    var newName = (<HTMLInputElement>document.getElementById(inputId)).value;
    console.log('Updating color name...');
    this.colorService.updateColor(oldName, newName).subscribe(
      (res: any) => {
        console.log('After updating: ' + res);
      },
      (err: any) => {
        console.log('Something went wrong when updating: ' + err);
      }
    );
  }

  nameIsChanged($element_id: string): void {
    var saveButtonId = 'saveButton' + $element_id.substring(10);

    (<HTMLInputElement>document.getElementById(saveButtonId)).disabled = false;
    //console.log(saveButtonId);
  }
}
