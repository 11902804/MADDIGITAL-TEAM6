import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http';

const DATABASE_EMOTIONS_URL: string = 'http://localhost:8000/api/emotionlab'; // 'https://10.128.14.10:31800/api/emotionlab'

@Injectable({
    providedIn: 'root'
  })

export class EmotionLabService {
    
    constructor(private http: HttpClient) {}

    getAllEmotionsColors() {
        return this.http.get(DATABASE_EMOTIONS_URL).toPromise();
    }

    public updateEmotionColors(emotionName: string, nth_color:number, color_name:string){
        var DATABASE_EMOTIONSUPDATE_URL = DATABASE_EMOTIONS_URL.concat('/');
        console.log('Saving new color to database...');

        return this.http.put(DATABASE_EMOTIONSUPDATE_URL, {
            "emotion_name": emotionName,
            "nth_color": nth_color,
            "color_name": color_name
        });
    }
}
