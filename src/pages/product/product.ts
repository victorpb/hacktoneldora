import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';
import { Injectable } from '@angular/core';

@Component({
  selector: 'page-product',
  templateUrl: 'product.html'
})
@Injectable()
export class ProductPage {

	posts: any;
	data: any;
	results: string[];
  constructor(public navCtrl: NavController, public http: Http) {
  }

  checkRemote()
  {
	  return new Promise(resolve => {
	 
	      this.http.request('https://www.reddit.com/r/gifs/top/.json?limit=10&sort=hot')
	        .map(res => res.json()).subscribe(data => {
	          console.log(data);
	          this.data = data;
	          
	          resolve(this.data);
	        });
	    });
  }

}
