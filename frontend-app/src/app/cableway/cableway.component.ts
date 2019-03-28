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
    let resp = this.http.get<string>('startLeft');
    alert(resp);
  }

  onStartRight(): void {

  }

  onStop(): void {

  }

  onFaster(): void {

  }

  onSlower(): void {

  }
}
