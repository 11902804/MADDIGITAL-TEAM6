import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private REST_API_SERVER = "http://localhost:8000"; // "https://10.128.14.10:31800"
  constructor(private httpClient: HttpClient) { }

  get(endpoint: string) {
    return this.httpClient.get(this.REST_API_SERVER + endpoint).pipe(map(res => {
      return res;
    }));
  }

  async post(endpoint: string, data: any) {
    console.log('Connection with database...')
    return this.httpClient.post(this.REST_API_SERVER + endpoint, data).pipe(map(res => {
      console.log('Return: ' + res)
      return res;
    }));
  }

  put(endpoint: string, data: any) {
    return this.httpClient.put(this.REST_API_SERVER + endpoint, data).pipe(map(res => {
      return res;
    }));
  }
}
