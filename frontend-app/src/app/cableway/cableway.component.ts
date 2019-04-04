import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { timer } from 'rxjs';

@Component({
  selector: 'app-cableway',
  templateUrl: './cableway.component.html',
  styleUrls: ['./cableway.component.css']
})

export class CablewayComponent implements OnInit {

  speed = '?';

  constructor(private http: HttpClient) {
    const statusPoller = timer(500, 1000);
    statusPoller.subscribe( t => this.getStatus());
  }

  ngOnInit() {
  }

  onStartLeft(): void {
    this.http.get('startLeft').subscribe();
  }

  onStartRight(): void {
    this.http.get('startRight').subscribe();
  }

  onStop(): void {
    this.http.get('stop').subscribe();
  }

  onFaster(): void {
    this.http.get('faster').subscribe(
      data => null,
      error => this.speed = '?');
    this.getStatus();
  }

  onSlower(): void {
    this.http.get('slower').subscribe(
      data => null,
      error => this.speed = '?');
    this.getStatus();
  }

  getStatus() : void {
    this.http.get('status').subscribe(
      data => this.speed = data['speed'],
      error => this.speed = '?');
  }
}