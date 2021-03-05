import { Component, OnInit } from '@angular/core';
import { ColorService } from '../services/color.service';
import { EmotionService } from '../services/emotion.service';
import { EmotionLabService } from '../services/emotionlab.service';
import { PredefinedColorService } from '../services/predefinedColor.service';

@Component({
    selector: 'app-emotion-lab',
    templateUrl: './emotion-lab.html',
    styleUrls: ['./emotion-lab.css'],
  })
  

export class EmotionLabComponent implements OnInit {
    title = 'EmotionLab';
    colors: Array<any>;
    emotions: Array<any>;
    predefinedColors: Array<any>;
    selectedValue:any;

    ColorMap:Map<string, string> =new Map();
    //EmotionsToColorMap:Map<string,string> = new Map();


    // public get selectedColor():colors {
    //   return this.selectedValue ? this.selectedValue.value: null; 
    //}
    
    constructor(  private emotionService : EmotionService,
                private colorService : ColorService,
                private emotionLabService : EmotionLabService) {
        this.colors = [];       
        this.emotions = [];
        this.predefinedColors = [];
    }


    ngOnInit(){
        //get the emotions
        this.emotionService.getAllEmotions().subscribe((data: any[])=>{
           for (var object in data) {
                this.emotions.push(data[object].emotion_name);
                //console.log(data[object].emotion_name);
            };

                    //get the colors
        this.colorService.getAllColors().subscribe((data: any[])=>{
            for (var object in data) {
                this.ColorMap.set(data[object][0],data[object][1])
                 this.colors.push(data[object][0]);
                 //console.log(data[object][0]);
             };
         })
 
         //Get the colors already assigned to emotions
         this.emotionLabService.getAllEmotionsColors().then((data:any[])=>{
             for (var object in data) {
                 this.predefinedColors.push(data[object])
             };

             var data = this.predefinedColors;
             for (var i = 0; i<=18 ;i+=3){
                 var currentEmotion = data[i].emotion_name;
                 console.log(currentEmotion);
     
     
                switch (currentEmotion){
                    case "HAPPY":{
                        this.loadPredefinedColorsForEmotion(data[i].nth_color,data[i].hex_value,0,data[i].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+1].nth_color,data[i+1].hex_value,0,data[i+1].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+2].nth_color,data[i+2].hex_value,0,data[i+2].color_name);
                        break;
                    }
                    
                    case "SURPRISED":{
                        this.loadPredefinedColorsForEmotion(data[i].nth_color,data[i].hex_value,1,data[i].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+1].nth_color,data[i+1].hex_value,1,data[i+1].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+2].nth_color,data[i+2].hex_value,1,data[i+2].color_name);
                        break;
                    }

                    case "NEUTRAL":{
                        this.loadPredefinedColorsForEmotion(data[i].nth_color,data[i].hex_value,2,data[i].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+1].nth_color,data[i+1].hex_value,2,data[i+1].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+2].nth_color,data[i+2].hex_value,2,data[i+2].color_name);
                        break;
                    }

                    case "DISGUST":{
                        this.loadPredefinedColorsForEmotion(data[i].nth_color,data[i].hex_value,3,data[i].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+1].nth_color,data[i+1].hex_value,3,data[i+1].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+2].nth_color,data[i+2].hex_value,3,data[i+2].color_name);
                        break;
                    }
                    case "SAD":{
                        this.loadPredefinedColorsForEmotion(data[i].nth_color,data[i].hex_value,4,data[i].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+1].nth_color,data[i+1].hex_value,4,data[i+1].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+2].nth_color,data[i+2].hex_value,4,data[i+2].color_name);
                        break;
                    }
                    case "SCARED":{
                        this.loadPredefinedColorsForEmotion(data[i].nth_color,data[i].hex_value,5,data[i].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+1].nth_color,data[i+1].hex_value,5,data[i+1].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+2].nth_color,data[i+2].hex_value,5,data[i+2].color_name);
                        break;
                    }
                    case "ANGRY":{
                        this.loadPredefinedColorsForEmotion(data[i].nth_color,data[i].hex_value,6,data[i].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+1].nth_color,data[i+1].hex_value,6,data[i+1].color_name);
                        this.loadPredefinedColorsForEmotion(data[i+2].nth_color,data[i+2].hex_value,6,data[i+2].color_name);
                        break;
                    }

                }
     
            }
 
         })     
        })
    }

    colorChange(element_id:string,element_value:string){
        var id = element_id.substring(11);
        var emotionId = element_id.substring(13);
        var nth_color:number = +id.substring(0,1) ;
        var color_name = element_value;

        var colorDivElement = <HTMLInputElement>document.getElementById("colorDiv"+id);
        colorDivElement.style.backgroundColor=this.ColorMap.get(element_value);

        this.emotionLabService.updateEmotionColors(this.emotions[emotionId],nth_color,color_name).subscribe(() => {
            console.log('succeeded!');
          });

    }

    loadPredefinedColorsForEmotion(nth_color:number,hex:string,numberofEmotion:number,colorName:string){
        
        console.log(("colorDiv"+nth_color+"."+numberofEmotion));
        console.log(("label"+nth_color+"."+numberofEmotion));
        var colorDivElement = <HTMLInputElement>document.getElementById("colorDiv"+nth_color+"."+numberofEmotion);
        colorDivElement.style.backgroundColor=hex;

        var colorLabelElement = <HTMLInputElement>document.getElementById("label"+nth_color+"."+numberofEmotion);
        colorLabelElement.textContent = colorName;

    } 
}