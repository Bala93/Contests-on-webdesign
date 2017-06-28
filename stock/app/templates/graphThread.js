
//http://www.htmlgoodies.com/html5/tutorials/introducing-html-5-web-workers-bringing-multi-threading-to-javascript.html#fbid=SM1qm0sfYpQ
var i;
var value;
var str;
function graphThread(strloc){
	var str = strloc.split(" ");
    for(i=1;i<str.length-1;i++){
    	value=parseInt(str[i]);
    	self.postMessage({'value': value});
    }
}


self.onmessage = function(event){
	graphThread(event.data.value);
}