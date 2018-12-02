import { Component } from '@angular/core';
import GitHub from 'github-api';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {


  gh = new GitHub({
    token: '3944f1ef76fcd722b15e6d35a11e2fa93e01485f'
  
 });

me = this.gh.getUser(); // no user specified defaults to the user for whom credentials were provide


}

