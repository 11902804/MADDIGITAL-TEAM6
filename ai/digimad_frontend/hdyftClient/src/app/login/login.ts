import { Component, AfterViewInit, ViewChild } from '@angular/core';
import {
  FormBuilder,
  FormControl,
  FormGroup,
  Validators,
} from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { LoginService } from '../services/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.html',
  styleUrls: ['./login.css'],
})
export class loginComponent implements AfterViewInit {
  @ViewChild('loginElement') loginElement: any;
  loginEl: any;

  @ViewChild('logoutElement') logoutElement: any;
  logoutEl: any;

  @ViewChild('loadingElement') loadingElement: any;
  loading: any;

  @ViewChild('errorMessageElement') errorMessageElement: any;
  error: any;

  form = new FormGroup({
    email: new FormControl(),
    password: new FormControl(),
  });

  token: any;
  errorMessage: string;
  countTries: number = 0;

  constructor(
    public formBuilder: FormBuilder,
    private api: LoginService,
    private auth: AuthService,
    private router: Router
  ) {}

  ngAfterViewInit(): void {
    this.loginEl = this.loginElement.nativeElement;
    this.logoutEl = this.logoutElement.nativeElement;
    this.loading = this.loadingElement.nativeElement;
    this.error = this.errorMessageElement.nativeElement;

    this.token = this.auth.getToken();
    this.loginEl.hidden = this.token;
    this.logoutEl.hidden = !this.token;

    this.form = this.formBuilder.group({
      email: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  async login() {
    this.countTries++;
    this.error.hidden = true;
    this.loading.hidden = false;
    let formValue = this.form.value;
    (await this.api.post('/auth/login', formValue)).subscribe(
      (res: any) => {
        if (res.access_token) {
          let navigateTo = 'simulation';
          this.auth.login(res.access_token, res.name, navigateTo);
        } else {
          this.loading.hidden = true;
          this.error.hidden = false;
          this.errorMessage = res.error;
          console.log(res.error);
        }
      },
      (err) => {
        if (this.countTries < 10) {
          this.login();
          return;
        }
        this.loading.hidden = true;
        this.error.hidden = true;
        console.log(err);
        alert(
          'The application is currently unavailabe. Take a break and come back later!'
        );
      }
    );
  }

  logout() {
    this.auth.logout();
  }
}
