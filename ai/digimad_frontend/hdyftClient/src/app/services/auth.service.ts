import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private loggedIn = new BehaviorSubject<boolean>(false);
  private username = new BehaviorSubject<string>('');

  constructor(private router: Router) {
    this.checkForUser();
  }

  checkForUser() {
    if (this.getToken()) {
      this.username.next(this.getName());
      this.loggedIn.next(true);
    } else {
      this.loggedIn.next(false);
    }
  }

  isLoggedIn() {
    return this.loggedIn.asObservable();
  }

  setDataInLocalStorage(variableName, data) {
    localStorage.setItem(variableName, data);
  }

  login(token: string, username: string, route: string) {
    this.setDataInLocalStorage('hdyft-token', token);
    this.setDataInLocalStorage('hdyft-username', username);
    this.loggedIn.next(true);
    this.username.next(username);
    this.router.navigate(['/' + route]);
  }

  logout() {
    this.clearStorage();
    this.loggedIn.next(false);
    this.username.next('');
    this.router.navigate(['/']);
  }

  getToken() {
    return localStorage.getItem('hdyft-token');
  }

  clearStorage() {
    localStorage.clear();
  }

  getUsername() {
    return this.username.asObservable();
  }

  getName() {
    return localStorage.getItem('hdyft-username');
  }
}