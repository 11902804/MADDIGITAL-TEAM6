import { ViewUserSimulationCameraComponent } from './views/view-user-simulation-camera/view-user-simulation-camera.component';
import { AuthGuardService } from './services/auth-guard.service';
import { Routes } from '@angular/router';
import { CameraComponent } from './camera/camera.component';
import { PredefinedColorTableComponent } from './predefined-color-table/predefined-color-table';
import { loginComponent } from './login/login';
import { EmotionLabComponent } from './emotion-lab/emotion-lab';
import { CanvasComponent } from './simulation/app.canvas';
import { ViewErrorNotFoundComponent } from './views/view-error-not-found/view-error-not-found.component';
import { ViewHomeComponent } from './views/view-home/view-home.component';
import { ViewLabComponent } from './views/view-lab/view-lab.component';

export const appRoutes: Routes = [
  { path: '', component: ViewHomeComponent },
  { path: 'lab', component: ViewLabComponent, canActivate: [AuthGuardService] },
  { path: 'simulation', component: CanvasComponent, canActivate: [AuthGuardService] },
  { path: 'camera', component: CameraComponent },
  { path: 'predefined', component: PredefinedColorTableComponent, canActivate: [AuthGuardService] },
  { path: 'login', component: loginComponent },
  { path: 'user', component: ViewUserSimulationCameraComponent},
  { path: '**', component: ViewErrorNotFoundComponent },
];
