import { Component, OnInit, AfterViewInit } from '@angular/core';
import { SocketService } from './services/socket.service';
import { AuthService } from './services/auth.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'hdyftClient';
  isLoggedIn$: Observable<boolean>;
  username$: Observable<string>;

  constructor(private socketService: SocketService, private authService: AuthService) { }

  ngOnInit() {
    // Connection to Socket.IO server
    this.socketService.listen('connect').subscribe((data) => {
      console.log(data);
    });

    this.isLoggedIn$ = this.authService.isLoggedIn();
    this.username$ = this.authService.getUsername();
  }

  logout() {
    this.authService.logout();
  }
}
