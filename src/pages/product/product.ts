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
	search: string[];
	results: string[];
	current_name: string[];
	// Store products in json object.
	tmp: any;

  constructor(public navCtrl: NavController, public http: Http) {
  }

  checkRemote()
  {
	  return new Promise(resolve => {
	 
	       //this.http.request('https://www.reddit.com/r/gifs/top/.json?limit=10&sort=hot')
	       this.http.request('http://127.0.0.1:8000/api/products/?format=json')
	        .map(res => res.json()).subscribe(data => {
	          console.log(data);
	          this.data = data;
	          this.current_name = data.name;
	          resolve(this.data)
	        });
	    });
  }

  searchProduct()
  {
  	console.log(this.search);
  	// Get product name to search in db.
  	if(this.search == {}){ 
  		this.products = {};
  		return false;
  	}
  	var val = this.search;
  	console.log(this);
		var url = 'http://127.0.0.1:8000/api/products/?name='+val;
		
		return new Promise(resolve => {
			this.http.request(url).map(res => res.json()).
			subscribe(data => {
				console.log(data);
				// If none is returned, abort.
				if(!data.length)
					return false;
				this.tmp = data;

				resolve(this.products);
				this.showProducts(data)
				this.current_name = data;
			})
		});
  }

  products: any;

  showProducts(json)
  {



  	var url = 'http://127.0.0.1:8000/api/storage/?product='+json[0].id;
		
		return new Promise(resolve => {
			this.http.request(url).map(res => res.json()).
			subscribe(data => {
				console.log(data);
				this.products = data;
				resolve(this.products);

			})
		});
  }

}
