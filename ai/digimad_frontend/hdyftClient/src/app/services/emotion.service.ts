import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';

const DATABASE_EMOTIONS_URL: string = 'http://localhost:8000/api/emotions'; // 'https://10.128.14.10:31800/api/emotions'

@Injectable({
    providedIn: 'root'
  })

export class EmotionService {

    constructor(private http: HttpClient) {}

    public getAllEmotions(){
        return this.http.get(DATABASE_EMOTIONS_URL);
    }

    public getEmotionById(id:number){
      var DATABASE_EMOTIONSGETBYID_URL = DATABASE_EMOTIONS_URL.concat("/"+id);
      return this.http.get(DATABASE_EMOTIONSGETBYID_URL);
    }

    public createEmotion(newEmotion:string){
      var httpCreateOptions = {
        params:{emotion_name: newEmotion}
      }
      return this.http.post(DATABASE_EMOTIONS_URL,httpCreateOptions);
    }

    public updateEmotion(id:number, newEmotion:string){
      var DATABASE_EMOTIONSPUT_URL = DATABASE_EMOTIONS_URL.concat("/"+id);
      var httpUpdateOptions = {
        params:{emotion_name: newEmotion}
      }
      return this.http.put(DATABASE_EMOTIONSPUT_URL,httpUpdateOptions);
    }

    public deleteEmotion(id:number){
      var DATABASE_DELETEEMOTIONS_URL = DATABASE_EMOTIONS_URL.concat("/"+id);
      return this.http.delete(DATABASE_DELETEEMOTIONS_URL);
    }


    
}
