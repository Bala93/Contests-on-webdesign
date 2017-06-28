//why it is 51 - becoz domain is 0 to 50. Initial set up of random 50 points
var n = 51; 

var de = [];

//set all the points to 0;
// for(var i=0;i<n;i++){
// 	var newnumber = 20;//Math.random() * 100;
// 	de.push(newnumber);
// }

//set up width, height and four side margins of SVG
var margin = {top: 20, right: 20, bottom: 20, left: 40},
	//width = 960 - margin.left - margin.right,
    //height = 500 - margin.top - margin.bottom;
	width = 470,
	height = 225;

	
//Scaling X coordinate to svg sapce
var x =  d3.scale.linear()
			//.domain([0,d3.max(de, function(d){ return de.xval;})])
			.domain([0,16])
			.range([0,width]);

//Scaling Y coordinates to svg space
var y = d3.scale.linear()
			//.domain([0,d3.max(de, function(d){ return de.yval;})])
			.domain([0,100])
			.range([height,0]);

//conversion function from domain to range
var line = d3.svg.line()
			.x(function(d,i) { return x(i)})  //corresponding index
			.y(function(d,i) { return y(d)}); //corresponding data


//create svg and append it to the container (id of div) that is specified in your html file			
var svg2 = d3.select("#Hchart_svg_container").append("svg")
	.attr("class","chart-svg-component")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  	.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

//element is used to embed definitions that can be reused inside an SVG image
svg2.append("defs").append("clipPath")
    .attr("id", "clip")
  .append("rect")
    .attr("width", width)
    .attr("height", height);

//Displaying X and Y axis text
var xAxis = d3.svg.axis()
			.scale(x)
			.orient("bottom");
	
svg2.append("g")
    .attr("class", "xaxis")
    .attr("transform", "translate(0," + y(0) + ")")
    .call(xAxis);
	
var yAxis = d3.svg.axis()
			.scale(y)
			.orient("left");

svg2.append("g")
    .attr("class", "yaxis")
    .call(yAxis);

//appending rectangle element to SVG
var rec = svg2.append("g")
				.append("rect")
				.attr("x",0)
				.attr("y",0)
				.attr("width",width)
				.attr("height",height)
				.attr("stroke","silver")
				.attr("stroke-width",2)
				.attr("fill","#edf4f8");

//defs element is reused here
var path1 = svg2.append("g")
    .attr("clip-path", "url(#clip)")
  .append("path")
    .datum(de)
    .attr("class", "chartline")
    .attr("d", line)
	.attr("fill","none")
	.attr("stroke","#365899")
	.attr("stroke-width",2);
				
//tick2();




 
function temp(de) {
	
	/*var ry = Math.floor((Math.random() * 50) + 1);
	//var rx = Math.floor((Math.random() * ) + 1);
	//Math.floor(Math.random() * (max - min + 1)) + min;
	var rx = Math.floor(Math.random() * (100 - 1 + 1)) + 1;
	//rx = 150;
	var da = new Object();
	da = {'xval': rx, 'yval': ry};
	da.xval = rx;
	da.yval = ry;

	//push a new data point onto the back
	de.push(da);*/
	
	//find minimum and maximum in the data to set as domain
	//y.domain(d3.extent(de, function(d) {return d.yval; }));
	var minmax = d3.extent(de, function(d) {return d; });
	//console.log(minmax);
	var min = minmax[0];
	var max = minmax[1];
	//if(min!=max)
		//set up domain
		//y.domain([min,max]);
	//else
		//y.domain([-0.0004,0.0004]);
	
	/*svg.select(".yaxis")
			.transition().duration(0).ease("linear")
			.call(yAxis);*/
	
	//console.log(line(de));
  //redraw the line, and slide it to the left
  path1
	  .attr("d", line(de))
      .attr("transform", null)
    .transition()
      .duration(0)
      .ease("linear")
      .attr("transform", "translate(" + x(0) + ",0)")
      //.each("end", tick2);
	  
  //pop the old data point off the front
//de.shift();
}
