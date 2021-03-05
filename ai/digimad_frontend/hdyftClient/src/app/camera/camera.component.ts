import { SocketService } from '../services/socket.service';
import { AfterViewInit, Component, ViewChild } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-camera',
  templateUrl: './camera.component.html',
  styleUrls: ['./camera.component.css']
})
export class CameraComponent implements AfterViewInit {

  @ViewChild('videoElement') videoElement: any;
  video: any;

  @ViewChild('canvasElement') canvasElement: any;
  canvas: any;

  @ViewChild('errorElement') errorElement: any;
  error: any;

  @ViewChild('cameraStatusElement') cameraStatusElement: any;
  status: any;

  context: any;
  height: any;
  width: any;
  fps: any;

  cameraStatus: Boolean;
  cameraStatusMessage: String;
  recoveryMessage: String;

  wristbandId: number;
  serverSessionId: any;
  detectedEmotion: string;

  cameraAccessible: boolean = false;

  constructor(private socketService: SocketService, private cookieService: CookieService) { }

  ngAfterViewInit(): void {
    this.video = this.videoElement.nativeElement;
    this.canvas = this.canvasElement.nativeElement;
    this.error = this.errorElement.nativeElement;
    this.status = this.cameraStatusElement.nativeElement;


    // Hardcoded height and width
    this.height = 480; // TODO: get video height
    this.width = 640; // TODO: get video width
    this.canvas.height = this.height;
    this.canvas.width = this.width;


    // Sending speed
    this.fps = 7;

    // Listen for received sid
    this.socketService.listen('sid').subscribe((data) => {
      this.serverSessionId = data;
      console.log('Connected with Socket.IO server');
    });

    // Checking connection and asking for sid
    this.socketService.emit('connect', 'Connected!');

    // Listen for responses (emotions)
    this.socketService.listen('emotion').subscribe((data: string) => {
      if (data == 'null') return;
      this.detectedEmotion = data;
      this.cookieService.set('hdyft-emotion', data);
    });

    // Listen for errors
    this.socketService.listen('error').subscribe((data) => {
      console.log('Socket.IO error: ', data)
    });

    // Start camera
    this.initCamera({ video: true, audio: false });

    // Get wristband id out of cookie
    // If no cookie/wristband id -> id will be 0
    this.wristbandId = Number(this.cookieService.get('hdyft-wid'));
    console.log('Wristband id: ' + this.wristbandId);

    // Start sending frames
    this.start();
  };

  start() {
    this.sendFrames();
  }

  async initCamera(config: any) {
    let browser = <any>navigator;

    browser.getUserMedia = (browser.getUserMedia ||
      browser.webkitGetUserMedia ||
      browser.mozGetUserMedia ||
      browser.msGetUserMedia);

    await browser.mediaDevices.getUserMedia(config).then(stream => {
      this.cameraAccessible = true;
      this.showCameraError(false);
      this.video.srcObject = stream;
      this.video.play();
    }).catch(() => {
      this.showCameraError(true);
    });

    if (!this.cameraAccessible) { this.showCameraError(true); }
  }

  showCameraError(error: boolean) {
    this.status.hidden = !error
    this.cameraStatus = !error
    this.video.hidden = error;
    this.error.hidden = !error;

    if (error) {
      this.cameraStatusMessage = 'Camera does not work as it should. Make sure that the camera is not being used by another application and allow this website to use your camera.'
      this.recoveryMessage = 'Hint: On the top right of the address bar there is a camera icon. Click there to turn your camera on and refresh this page.'
      this.recoveryMessage += ' Not all mobile browsers support camera usage.  If you\'re using iOS (Apple iPhone/Apple iPad) try to use Safari.'
    }
  }

  sendOneFrame() {
    let data = this.getConvertedImage();
    console.log(data);
    this.socketService.emit('image', data);
  }

  getConvertedImage() {
    this.context = this.canvas.getContext('2d');
    this.context.drawImage(this.video, 0, 0);
    let data = this.canvas.toDataURL('image/jpeg');
    return (data);
  }

  sendFrames() {
    let rate = 1000 / this.fps;
    console.log('Sending frames at ', this.fps, ' FPS. (', rate, ')');
    setInterval(() => {
      let convertedData = this.getConvertedImage();
      let dataToSend = { 'image': convertedData, 'wristbandId': this.wristbandId }
      // Emitting converted image and wristband id to 'image'
      this.socketService.emit('image', dataToSend);
    }, rate);
  }
}
