import { EmotionLabService } from './services/emotionlab.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppComponent } from './app.component';
import { NgxColorPickerComponent } from './ngx-color-picker/ngx-color-picker.component';

import { ColorPickerModule } from 'ngx-color-picker';
import { CameraComponent } from './camera/camera.component';
import { HttpClientModule } from '@angular/common/http';
import { LightService } from './services/light.service';
import { CanvasComponent } from './simulation/app.canvas';

import { appRoutes } from './app.route';
import { RouterModule } from '@angular/router';

import { EmotionLabComponent } from './emotion-lab/emotion-lab';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ViewLabComponent } from '../app/views/view-lab/view-lab.component';
import { ViewHomeComponent } from './views/view-home/view-home.component';
import { ViewErrorNotFoundComponent } from './views/view-error-not-found/view-error-not-found.component';

import { PredefinedColorTableComponent } from './predefined-color-table/predefined-color-table'
import { CreateNewPredefinedTableComponent } from './create-new-predefined-color/create-new-predefined-color'
import { loginComponent } from './login/login';
import { HomepageComponent } from './homepage/homepage';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { CookieService } from 'ngx-cookie-service';
import { ViewUserSimulationCameraComponent } from './views/view-user-simulation-camera/view-user-simulation-camera.component';

@NgModule({
  declarations: [
    AppComponent,
    NgxColorPickerComponent,
    CameraComponent,
    PredefinedColorTableComponent,
    CreateNewPredefinedTableComponent,
    EmotionLabComponent,
    CameraComponent,
    CanvasComponent,
    loginComponent,
    HomepageComponent,
    ViewLabComponent,
    ViewHomeComponent,
    ViewErrorNotFoundComponent,
    ViewUserSimulationCameraComponent,
  ],
  imports: [
    BrowserModule,
    ColorPickerModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    RouterModule.forRoot(appRoutes),
    NgbModule,
    ReactiveFormsModule
  ],
  providers: [LightService, CookieService, EmotionLabService],
  bootstrap: [
    AppComponent,
  ],
})
export class AppModule {}
