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
str = this.readTextFile('/home/chihun/Documents/SoftwareEngineering/CS3012-Software-Engineering-Module/Social Graph and Github Access/repoDetails.csv'); 
me = this.gh.getUser(); // no user specified defaults to the user for whom credentials were provide

readFile(file: File) {
  var reader = new FileReader();
  reader.onload = () => {
      console.log(reader.result);
  };
  reader.readAsText(file);
}
readTextFile(filepath) {
	var str = "";
	var txtFile = new File([""],filepath);
	txtFile.open("r");
	while (!txtFile.eof) {
		// read each line of text
		str += txtFile.readln() + "\n";
	}
	return str;
}
}

