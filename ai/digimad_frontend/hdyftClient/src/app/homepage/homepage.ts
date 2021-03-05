import { AuthService } from './../services/auth.service';
import { Component } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.html',
  styleUrls: ['./homepage.css']
})

export class HomepageComponent {
    id: number
    isLoggedIn$: Observable<boolean>;
    isNotLoggedIn$: Observable<boolean>;

    constructor(private cookieService: CookieService, private authService: AuthService) {
      this.isLoggedIn$ = this.authService.isLoggedIn();
      this.isNotLoggedIn$ = this.authService.isLoggedIn();
    }

    enterId(){
        var enteredId= (<HTMLInputElement>document.getElementById("idNumber"));
      
        console.log(enteredId.value);
    }

    saveWristbandId() {
      let idNumberElement = (<HTMLInputElement>document.getElementById("idNumber"));
      let wristbandId = idNumberElement.value;
      console.log(wristbandId);
      this.cookieService.set('hdyft-wid', wristbandId);
    }

    logoutUser() {
      this.authService.logout();
      alert('Logged out successfully!');
    }
}
