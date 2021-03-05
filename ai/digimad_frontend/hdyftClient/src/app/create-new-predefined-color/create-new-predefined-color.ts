import { Component } from '@angular/core';

@Component({
    selector: 'app-create-new-predefined-color',
    templateUrl: './create-new-predefined-color.html',
    styleUrls: ['./create-new-predefined-color.css'],
  })
  

export class CreateNewPredefinedTableComponent {
    title = 'NewPredefinedColorTable';
    public color: string = '#dbf7d9';
    private colorcount: number;

    constructor() {
      this.colorcount=1;
    }      

    colorChoose(){
      var chosenColor = (<HTMLInputElement>document.getElementById("newColorPicker")).style.backgroundColor;
      var currentId = "color" + this.colorcount;

      (<HTMLInputElement>document.getElementById(currentId)).style.backgroundColor = chosenColor;
      this.colorcount++;
      if (this.colorcount > 3){
        (<HTMLInputElement>document.getElementById("newColorButton")).disabled = true;
        (<HTMLInputElement>document.getElementById("saveButton")).disabled = false;
      }

    }

    resetChoice(){
      (<HTMLInputElement>document.getElementById("color1")).style.backgroundColor = "white";
      (<HTMLInputElement>document.getElementById("color2")).style.backgroundColor = "white";
      (<HTMLInputElement>document.getElementById("color3")).style.backgroundColor = "white";
      (<HTMLInputElement>document.getElementById("newColorButton")).disabled = false;
      this.colorcount=1;
    }

    saveColor(){
      console.log("flag 1");
      var name = (<HTMLInputElement>document.getElementById("namePredefined")).value;
       var colors = this.hexc((<HTMLInputElement>document.getElementById("color1")).style.backgroundColor)+ "," +
       this.hexc((<HTMLInputElement>document.getElementById("color2")).style.backgroundColor) + "," +
       this.hexc((<HTMLInputElement>document.getElementById("color3")).style.backgroundColor);

      console.log(colors);
    }

    //implemented code to convert rgb to hex, might be temporary
    hexc(colorval) {
      var parts = colorval.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
      delete(parts[0]);
      for (var i = 1; i <= 3; ++i) {
        parts[i] = parseInt(parts[i]).toString(16);
        if (parts[i].length == 1) parts[i] = '0' + parts[i];
      }
      return('#' + parts.join(''));
    }
}