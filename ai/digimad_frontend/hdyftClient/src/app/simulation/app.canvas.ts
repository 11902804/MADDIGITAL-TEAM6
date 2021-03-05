import { Router } from '@angular/router';
import { EmotionLabService } from './../services/emotionlab.service';
import { CookieService } from 'ngx-cookie-service';
import { Component, Input, AfterViewInit, OnInit, ViewChild } from '@angular/core';
import {
  animate,
  state,
  style,
  transition,
  trigger,
} from '@angular/animations';
import { Emotion } from '../models/emotion.model';
import { Color } from '../models/color.model';

@Component({
  selector: 'app-canvas',
  templateUrl: './app.canvas.html',
  styleUrls: ['./app.canvas.css'],
  animations: [
    trigger('colorbackground', [
      state(
        'start',
        style({
          backgroundColor: '{{firstColor}}',
        }),
        { params: { firstColor: 'white' } }
      ),

      state(
        'middle',
        style({
          backgroundColor: '{{secondColor}}',
        }),
        { params: { secondColor: 'white' } }
      ),

      state(
        'end',
        style({
          backgroundColor: '{{thirdColor}}',
        }),
        { params: { thirdColor: 'white' } }
      ),

      transition('* <=> *', animate('1.5s ease-out')),
    ]),
  ],
})
export class CanvasComponent implements OnInit, AfterViewInit {
  title = 'canvas';
  state: string = 'start';
  colorOne: string = 'white';
  colorTwo: string = 'white';
  colorThree: string = 'white';

  emotions: Array<Emotion>;

  @Input() interactive: boolean = false;

  countOfTries: number = 0;

  @ViewChild('errorElement') errorElement: any;
  error: any;

  @ViewChild('simulationElement') simulationElement: any;
  simulation: any;

  constructor(
    private emotionLabService: EmotionLabService,
    private cookieService: CookieService,
    private router: Router) {
  }

  async ngOnInit() {
    this.emotions = [];
  }

  ngAfterViewInit(): void {
    this.error = this.errorElement.nativeElement;
    this.simulation = this.simulationElement.nativeElement;

    this.fetchAllEmotionsAndColors();

    this.useCamera(); // if interactive is true
  }

  public colorChange(color1: string, color2: string, color3: string) {
    this.colorOne = color1;
    this.colorTwo = color2;
    this.colorThree = color3;
  }

  toggleAnimation() {
    switch (this.state) {
      case 'start': {
        this.state = 'middle';
        break;
      }
      case 'middle': {
        this.state = 'end';
        break;
      }
      case 'end': {
        this.state = 'start';
        break;
      }
      default: {
        this.state = 'start';
        break;
      }
    }
  }

  lampChange(element_value: string) {
    console.log(element_value);

    let colors: Array<Color>;
    colors = [];

    let index = this.emotions.findIndex(x => x.name == element_value);
    this.emotions[index].colors.forEach((element: Color) => {
      colors.push(element);
    });
    console.log(colors);

    this.colorChange(colors[0].hex, colors[1].hex, colors[2].hex);
  }


  useCamera() {
    if (!this.interactive) return;
    setInterval(() => {
      try {
        let emotion: string = this.cookieService.get('hdyft-emotion');
        this.lampChange(emotion.toUpperCase());
      } catch {
        console.log('');
      }
    }, 1000 / 7);
  }

  async fetchAllEmotionsAndColors() {
    this.countOfTries = 0;
    console.log('Fetching all emotions and colors data...')
    while (this.emotions.length == 0 && this.countOfTries < 5) {
      this.emotions = await this.getAllEmotionsAndColors();
      this.countOfTries++;
    }

    if (this.emotions.length == 0) {
      this.simulation.hidden = true;
      this.error.hidden = false;
    } else {
      this.simulation.hidden = false;
      this.error.hidden = true
      console.log('Fetched all data in ' + this.countOfTries + ' tr(y)(ies).');
    }
  }

  async getAllEmotionsAndColors() {
    let emotions_array: Array<Emotion> = [];

    await this.emotionLabService.getAllEmotionsColors().then(
      (data: any) => {
        for (let object in data) {

          // creating emotions
          let emotion_name = data[object].emotion_name;
          let index = this.getEmotionIndex(emotion_name, emotions_array);

          // if emotion doesn't exists: create one
          if (index < 0) {
            let emotion = new Emotion();
            emotion.name = data[object].emotion_name;
            emotions_array.push(emotion);
          }

          // creating color
          let color_data = data[object];
          let color = new Color();
          color.name = color_data.color_name;
          color.hex = color_data.hex_value;

          // update index
          index = this.getEmotionIndex(emotion_name, emotions_array);

          // creating color
          emotions_array[index].colors.push(color);
        }
      }).catch(
        (error: any) => {
          console.log('An error occured while fetching the data.', error)
        });

    return emotions_array;
  }

  getEmotionIndex(emotion: string, emotions_array: Array<Emotion>) {
    // if emotion doesn't exists: returns -1
    // if emotion already exists: return index
    return emotions_array.findIndex(x => x.name == emotion);
  }
}