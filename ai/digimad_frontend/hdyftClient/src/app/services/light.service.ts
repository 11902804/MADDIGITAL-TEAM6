import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

const EMULATOR_PUT_REQUEST_URL: string = 'http://localhost:8000/api/newdeveloper/lights/1/state';
const IRL_PUT_REQUEST_URL: string = 'http://localhost:6970/changeColor/';

@Injectable()
export class LightService {
    isIRL: boolean = true;

    constructor(private http: HttpClient) {}

    //TODO: Color conversion to hue, bri, sat is not the best => Check LightService
    updateLight(data: any): Observable<any> { 

        if (this.isIRL) {
            return this.http.put(IRL_PUT_REQUEST_URL, {
                "hue": data[0]*186,
                "bri": 200,
                "sat": 87,
                "id": 1,
                "on": true,
            });
        }

        return this.http.put(EMULATOR_PUT_REQUEST_URL, {
            "hue": data[0]*186,
            // "sat": data[1],
            // "bri": data[2],
            // "hue": 50000,
            "bri": 200,
            "sat": 87,
            "on": true,
        });
    }
}
