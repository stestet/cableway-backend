import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent implements OnInit {

  constructor(private http: HttpClient) {

  }

  ngOnInit() {
  }

  onShutdown(): void {
    this.http.get('shutdown').subscribe();
  }

}
