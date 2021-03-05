import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import * as io from 'socket.io-client';

@Injectable({
  providedIn: 'root',
})
export class SocketService {
  socket: any;

  // Socket.IO server
  // readonly uri: string = 'wss://10.128.14.10:31400/';
 
  readonly uri: string = 'ws://0.0.0.0:4000/' // LOCAL

  constructor() {
    // Creating connection with server
    this.socket = io(this.uri, { transports: ['websocket', 'polling'] });
  }

  // Function for listening to an event
  listen(eventName: string) {
    return new Observable((subscriber) => {
      this.socket.on(eventName, (data) => {
        subscriber.next(data);
      });
    });
  }

  // Function for emiting (posting) to an event
  emit(eventName: string, data: any) {
    this.socket.emit(eventName, data);
  }
}
