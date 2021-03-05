import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { map } from 'rxjs/operators';

const DATABASE_COLORS_URL: string = 'http://localhost:8000/api/colors'; // 'https://10.128.14.10:31800/api/colors'

@Injectable({
  providedIn: 'root',
})
export class ColorService {
  constructor(private http: HttpClient) {}

  public getAllColors() {
    return this.http.get(DATABASE_COLORS_URL);
  }

  public getColorByName(name: string) {
    var DATABASE_COLORSGETBYNAME_URL = DATABASE_COLORS_URL.concat('/' + name);
    return this.http.get(DATABASE_COLORSGETBYNAME_URL);
  }

  public createColor(newColorName: string, newColorHex: string) {
    let data = {
      color_name: newColorName,
      hex_value: newColorHex,
    };

    console.log('Saving new color to database...');
    return this.http.post(DATABASE_COLORS_URL, data);
  }

  public updateColor(oldColorName: string, newColorName: string) {
    let data = {
      old_name: oldColorName,
      new_name: newColorName,
    };

    var DATABASE_COLORSPUT_URL = DATABASE_COLORS_URL;

    console.log('Updating color name in database...');
    return this.http.put(DATABASE_COLORSPUT_URL, data);
  }

  public deleteColorByName(name: string) {
    var DATABASE_DELETECOLORBYNAME_URL = DATABASE_COLORS_URL.concat('/' + name);
    return this.http.delete(DATABASE_DELETECOLORBYNAME_URL);
  }
}
