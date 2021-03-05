import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

const DATABASE_PREDEFINEDCOLORS_URL: string = 'http://localhost:8000/api/emotionlab'; // 'http://10.128.14.10:31800/api/emotionlab'

@Injectable({
    providedIn: 'root'
  })
export class PredefinedColorService {

    constructor(private http: HttpClient) {}

    public getAllPredefinedColors(){
        return this.http.get(DATABASE_PREDEFINEDCOLORS_URL);
    }

    public getPredefinedColorById(id:number){
        var DATABASE_PREDEFINEDCOLORSGETBYID_URL = DATABASE_PREDEFINEDCOLORS_URL.concat("/"+id);
        return this.http.get(DATABASE_PREDEFINEDCOLORSGETBYID_URL);
      }
  
      //need to figure out how 
/*       public createPredefinedColor(emotionId:number, nthColor:number, colorId:number){
        var httpCreateOptions = {
          params:{
                emotion_id: emotionId,
                nth_color: nthColor,
                color_id: colorId
            }
        }
        return this.http.post(DATABASE_PREDEFINEDCOLORS_URL,httpCreateOptions);
      }
  
      public updatePredefinedColor(emotionId:number, nthColor:number, colorId:number){
        var DATABASE_PREDEFINEDCOLORSPUT_URL = DATABASE_PREDEFINEDCOLORS_URL.concat("/"+emotionId);
        var httpUpdateOptions = {
            params:{
                emotion_id: emotionId,
                nth_color: nthColor,
                color_id: colorId
            }
        }
        return this.http.put(DATABASE_PREDEFINEDCOLORSPUT_URL,httpUpdateOptions);
      } */
  
      public deletePredefinedColor(id:number){
        var DATABASE_DELETEPREDEFINEDCOLORS_URL = DATABASE_PREDEFINEDCOLORS_URL.concat("/"+id);
        return this.http.delete(DATABASE_DELETEPREDEFINEDCOLORS_URL);
      }
}

