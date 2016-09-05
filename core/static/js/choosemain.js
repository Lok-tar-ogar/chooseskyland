// JavaScript Document

function showTxt(head,number,num) {
	for(var i=1;i<=num;i++) {
		if(i == number) {
			document.getElementById(head + i).style.display = "inline";
		}else{
			document.getElementById(head + i).style.display = "none";
			
		}
	}
}