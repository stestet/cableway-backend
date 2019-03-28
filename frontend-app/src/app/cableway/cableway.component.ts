import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-cableway',
  templateUrl: './cableway.component.html',
  styleUrls: ['./cableway.component.css']
})
export class CablewayComponent implements OnInit {

  constructor(private http: HttpClient) {

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
    this.http.get('faster').subscribe();
  }

  onSlower(): void {
    this.http.get('slower').subscribe();
  }
}
