import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';
import { Injectable } from '@angular/core';

@Component({
  selector: 'page-chat',
  templateUrl: 'chat.html'
})

@Injectable()

export class ChatPage {

	// JSON with users.
  users: any;
  // Selected User.
  userSelected: any;
  // Current Chat.
  currentChat: any;
  // Message
  message: string;
  constructor(public navCtrl: NavController, public http:Http)
  {
  	this.listUsers();
  }

  /**
   * List Users.
   *
   * Get by URL in database, and returns a json with users.
   *
   */
  listUsers()
  {
  	var url = 'http://127.0.0.1:8000/api/users/';
		return new Promise(resolve => {
			this.http.request(url).map(res => res.json()).
			subscribe(data => {
        this.users = data;
        console.log(data);
				resolve(this.users);
			})
		});
  }

  /**
   * Recover Chat.
   * 
   * This function, search by receptor user and, recover
   * all conversations from Database.
   */
  recoverChat()
  {
    console.log(this.userSelected);
    if(this.userSelected == undefined) return false;
    var url = 'http://127.0.0.1:8000/api/chat/?user='+this.userSelected;
		return new Promise(resolve => {
			this.http.request(url).map(res => res.json()).
			subscribe(data => {
        this.currentChat = data;
        if(data == {})
          this.currentChat = {};
        console.log(data);
				resolve(this.currentChat);
			})
		});
  }

  sendMessage()
  {
    console.log("OLOLOLO");
    var val = this.message;
    console.log(val);
    var send_user = 1;
    var receptor_user = this.userSelected;
    // POST TO SEND to DB
    var datab = {
      'send_user':send_user,
      'receive_user':receptor_user,
      'message':val,
    };
    this.message = '';
    return new Promise(resolve => {
			this.http.post('http://127.0.0.1:8000/api/chat/',datab).map(res => res.json()).
			subscribe(data => {
        console.log(data);
        this.recoverChat();
			})
		});
    
  }



}
