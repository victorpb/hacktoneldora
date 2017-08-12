import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { ProductPage } from '../product/product';
@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
 
	
  constructor(public navCtrl: NavController) {

  }

  pushPage(){
    // push another page onto the navigation stack
    // causing the nav controller to transition to the new page
    // optional data can also be passed to the pushed page.
    this.navCtrl.setRoot(ProductPage, {
      id: "123",
      name: "Carl"
    });
  }
}
