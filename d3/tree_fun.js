'use strict';


// Tree configuration
var branches = [];
// var seed1 = {i: 0, x: 1000, y: 1300, a: 0, l: 220, d: 0}; // a = angle, l = length, d = depth

// var seed2 = {i: 0, x: 650, y: 650, a: 2.095, l: 160, d: 0};
// var seed3 = {i: 0, x: 650, y: 650, a: -2.095, l: 160, d: 0};

// var seed2 = {i: 0, x: 650, y: 650, a: 0, l: 120, d: 0};
// var seed3 = {i: 0, x: 650, y: 650, a: 0, l: 120, d: 0};
// var seed4 = {i: 0, x: 650, y: 650, a: 0, l: 120, d: 0};
// var seed4 = {i: 0, x: 650, y: 650, a: 0, l: 120, d: 0};

// var seed1 = {i: 0, x: 650, y: 650, a: 0, l: 160, d: 0};
// var seed2 = {i: 0, x: 650, y: 650, a: 2.095, l: 160, d: 0};
// var seed3 = {i: 0, x: 650, y: 650, a: -2.095, l: 160, d: 0};
// var seed4 = {i: 0, x: 650, y: 650, a: 3.14, l: 80, d: 0};
// var seed5 = {i: 0, x: 650, y: 650, a: -1.045, l: 80, d: 0};
// var seed6 = {i: 0, x: 650, y: 650, a: 1.045, l: 80, d: 0};
//
var seed1 = {i: 0, x: 650, y: 650, a: 0, l: 135, d: 0};
// var seed2 = {i: 0, x: 650, y: 650, a: 1, l: 120, d: 0};
// var seed3 = {i: 0, x: 650, y: 650, a: 2, l: 100, d: 0};
// var seed4 = {i: 0, x: 650, y: 650, a: 3, l: 90, d: 0};
// var seed5 = {i: 0, x: 650, y: 650, a: 4, l: 80, d: 0};
// var seed6 = {i: 0, x: 650, y: 650, a: 5, l: 70, d: 0};
// var seed7 = {i: 0, x: 650, y: 650, a: 6, l: 60, d: 0};
// var seed8 = {i: 0, x: 650, y: 650, a: 1, l: 50, d: 0};
// var seed9 = {i: 0, x: 650, y: 650, a: 2, l: 40, d: 0};
// var seed10 = {i: 0, x: 650, y: 650, a: 3, l: 30, d: 0};
// var seed11 = {i: 0, x: 650, y: 650, a: 4, l: 20, d: 0};
// var seed12 = {i: 0, x: 650, y: 650, a: 5, l: 10, d: 0};
// var seed13 = {i: 0, x: 650, y: 650, a: 6, l: 4, d: 0};

var da = 0.6; // Angle delta
var dl = 0.85; // Length delta (factor)
var ar = 0; // Randomness
var maxDepth = 7;


// Tree creation functions
function branch(b) {
  var end = endPt(b), daR, newB;
  branches.push(b);

  if (b.d === maxDepth) {
    return;
  }

  if (b.d === 0) {
    daR = ar * Math.random() - ar * 0.5; // 0.3 * 0.5 = 0.15 - 0.3 = -0.15 * 0.5 = -0.15
    newB = {
      i: branches.length,
      x: end.x,
      y: end.y,
      a: b.a - da + daR - 0.4,
      l: b.l * dl,
      d: 1,
      parent: b.i
    };
    branch(newB);

    // Right branch
    daR = ar * Math.random() - ar * 0.5;
    newB = {
      i: branches.length,
      x: end.x,
      y: end.y,
      a: b.a + da + daR + 0.4,
      l: b.l * dl,
      d: 1,
      parent: b.i,
    };
    branch(newB);

    daR = ar * Math.random() - ar * 0.5;
    newB = {
      i: branches.length,
      x: end.x,
      y: end.y,
      a: b.a + daR,
      l: b.l * dl,
      d: 1,
      parent: b.i,
    };
    branch(newB);
  }

  if (b.d === 4) {
    daR = ar * Math.random() - ar * 0.5; // 0.3 * 0.5 = 0.15 - 0.3 = -0.15 * 0.5 = -0.15
    newB = {
      i: branches.length,
      x: end.x,
      y: end.y,
      a: b.a - da + daR,
      l: b.l * dl,
      d: 5,
      parent: b.i
    };
    branch(newB);

    // Right branch
    daR = ar * Math.random() - ar * 0.5;
    newB = {
      i: branches.length,
      x: end.x,
      y: end.y,
      a: b.a + da + daR,
      l: b.l * dl,
      d: 5,
      parent: b.i,
    };
    branch(newB);

    daR = ar * Math.random() - ar * 0.5; // 0.3 * 0.5 = 0.15 - 0.3 = -0.15 * 0.5 = -0.15
    newB = {
      i: branches.length,
      x: end.x,
      y: end.y,
      a: (b.a - da) * 1.3,
      l: b.l * dl,
      d: 5,
      parent: b.i
    };
    branch(newB);

    // Right branch
    daR = ar * Math.random() - ar * 0.5;
    newB = {
      i: branches.length,
      x: end.x,
      y: end.y,
      a: (b.a + da) * 1.3,
      l: b.l * dl,
      d: 5,
      parent: b.i,
    };
    branch(newB);

    daR = ar * Math.random() - ar * 0.5;
    newB = {
      i: branches.length,
      x: end.x,
      y: end.y,
      a: b.a + daR,
      l: b.l * dl,
      d: 5,
      parent: b.i,
    };
    branch(newB);
  }

  // Left branch
  daR = ar * Math.random() - ar * 0.5; // 0.3 * 0.5 = 0.15 - 0.3 = -0.15 * 0.5 = -0.15
  newB = {
    i: branches.length,
    x: end.x,
    y: end.y,
    a: b.a - da + daR,
    l: b.l * dl,
    d: b.d + 1,
    parent: b.i
  };
  branch(newB);

  // Right branch
  daR = ar * Math.random() - ar * 0.5;
  newB = {
    i: branches.length,
    x: end.x,
    y: end.y,
    a: b.a + da + daR,
    l: b.l * dl,
    d: b.d + 1,
    parent: b.i,
  };
  branch(newB);
}

// var width = 2000;
// var height = 1300;
//
// var randomX = d3.random.normal(width / 2, 80),
//     randomY = d3.random.normal(height / 2, 80);
//
// var newdata = d3.range(2000).map(function() {
//   return [
//     randomX(),
//     randomY()
//   ];
// });
//
// var svg = d3.select("body")
//   .append("g")
//     .call(d3.behavior.zoom().scaleExtent([1, 8]).on("zoom", zoom))
//   .append("g");
//
// svg.append("rect")
//     .attr("class", "overlay")
//     .attr("width", width)
//     .attr("height", height);
//
//
// svg.selectAll("line")
//     .attr("r", 2.5)
//     .attr("transform", function(d) { return "translate(" + d + ")"; });

    // .style('stroke-width', function(d) {
    //     var t = parseInt( maxDepth * .5 + 4 - d.d * .75 );
    //     return  t + 'px';
    // })

// var x = d3.scale.linear()
//     .domain([0, width])
//     .range([0, width]);
//
// var y = d3.scale.linear()
//     .domain([0, height])
//     .range([height, 0]);

// var svg = d3.select("body").append("svg")
//     .attr("width", width)
//     .attr("height", height)
//   .append("g")
//     .call(d3.behavior.zoom().x(x).y(y).scaleExtent([1, 8]).on("zoom", zoom));

// svg.append("rect")
//     .attr("class", "overlay")
//     .attr("width", width)
//     .attr("height", height);

// var line = svg.selectAll("line")
//     .data(newdata)
//   .enter().append("circle")
//     .attr("r", 2.5)
//     .attr("transform", transform);

// function zoom() {
//   svg.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
// }

// function transform(d) {
//   return "translate(" + x(d[0]) + "," + y(d[1]) + ")";
// }

// .append("g")
//   .call(d3.behavior.zoom().x(x).y(y).scaleExtent([1, 8]).on("zoom", zoom))




function regenerate(initialise) {
  branches = [];
  // branch(seed13);
  // branch(seed12);
  // branch(seed11);
  // branch(seed10);
  // branch(seed9);
  // branch(seed8);
  // branch(seed7);
  // branch(seed6);
  // branch(seed5);
  // branch(seed4);
  // branch(seed3);
  // branch(seed2);
  branch(seed1);
  initialise ? create() : update();
}



function endPt(b) {
  // Return endpoint of branch
  var x = b.x + b.l * Math.sin( b.a );
  var y = b.y - b.l * Math.cos( b.a );
  return {x: x, y: y};
}


// D3 functions
var color = d3.scale.linear()
    .domain([0, maxDepth * 0.4, maxDepth * 0.99, maxDepth])
    .range(["green","red","yellow","blue"]);
    // .range(["black","blue","white","black"]);

function x1(d) {return d.x;}
function y1(d) {return d.y;}
function x2(d) {return endPt(d).x;}
function y2(d) {return endPt(d).y;}
function highlightParents(d) {
  var colour = d3.event.type === 'mouseover' ? 'green' : color(d.d);
  var depth = d.d;
  for (var i = 0; i <= depth; i++) {
    d3.select('#id-'+parseInt(d.i))
      .style('stroke', colour);
    d = branches[d.parent];
  }
}

// var circle = svg.selectAll("circle")
//     .data(data)
//   .enter().append("circle")
//     .attr("r", 2.5)
//     .attr("transform", transform);
//
// function zoom() {
//   .attr("transform", transform);
// }


// var width = 2000;
// var height = 1300;
//
// var xx = d3.scale.linear()
//     .domain([0, width])
//     .range([0, width]);
//
// var yy = d3.scale.linear()
//     .domain([0, height])
//     .range([height, 0]);
//
// // function transform(d) {
// //   return "translate(" + xx(d.x) + "," + yy(d.y) + ")";
//
// //
// // function translateWidth(d) {
// //   var t = parseInt( maxDepth * .5 + 4 - d.d * .75 );
// //   return d3.scale.linear()
// //     .domain([0, t])
// //     .range([0, t]);
// // }
//
// function transform(d) {
//   return "translate(" + xx(d) + "," + yy(d) + ")";
// }


function create() {
  d3.select('svg')
    .call(d3.behavior.zoom().scaleExtent([0.6, 10]).on("zoom", function () {
      d3.select('g').attr("transform", "translate(" + d3.event.translate + ")" + " scale(" + d3.event.scale + ")")
    }))
    .append("g")
    .selectAll('line')
    .data(branches)
    .enter()
    .insert('line',":first-child")
    .attr('x1', x1)
    .attr('y1', y1)
    .attr('x2', x2)
    .attr('y2', y2)
    .style('stroke-width', function(d) {
        var t = parseInt( maxDepth * .5 + 4 - d.d * .75 );
        return  t + 'px';
    })
    .style('stroke', function(d) {
        return color(d.d);
    })
    .attr('id', function(d) {
      return 'id-'+d.i;
    })
    // .on("click", function(d){
    //     d3.select(this)
    //       .transition()
    //       .duration(1000)
    //       // .ease(d)
    //       .attr("cx", width-xPadding)
    //       .each("end", function(){
    //           d3.select(this)
    //             .transition()
    //             .delay(500)
    //             .duration(500)
    //             .attr({
    //               cx: xPadding
    //             })
    //       })
    //   })
    .attr('class', function(d) {
      if (d.d === maxDepth) {
        return 'artcl';
      }
      if (d.d === maxDepth - 1) {
        return 'ctg-3';
      }
      if (d.d === maxDepth - 2) {
        return 'ctg-2';
      }
      if (d.d === maxDepth - 3) {
        return 'jrnl';
      }
      if (d.d === maxDepth - 4) {
        return 'ctg-1';
      }
    });
}

function update() {
  d3.select('svg')
    .selectAll('line')
    .data(branches)
    .transition()
    .attr('x1', x1)
    .attr('y1', y1)
    .attr('x2', x2)
    .attr('y2', y2);
}

d3.selectAll('.regenerate')
  .on('click', regenerate);

regenerate(true);



// var zoom = d3.behavior.zoom();
// d3.select('line').call(zoom);


// function zoom() {
//   svg.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
// }
//
// var width = 2000;
// var height = 1300;
//
// //
// // var randomX = d3.random.normal(width / 2, 80),
// //     randomY = d3.random.normal(height / 2, 80);
// //
// // var newData = d3.range(2000).map(function() {
// //   return [
// //     x1,
// //     y1,
// //     x2,
// //     y2,
// //   ];
// // });
//
// var svg = d3.select("svg")
//     .call(d3.behavior.zoom().scaleExtent([1, 8]).on("zoom", zoom))
//
// svg.append("rect")
//     .attr("class", "overlay")

//
// svg.selectAll("line")
//     .data(newData)
//   .enter().append("line")
//     .style('stroke-width', function(d) {
//         var t = parseInt( maxDepth * .2 + 4 - d.d * .75 );
//         return  t + 'px';
//     })
//     .attr("transform", function(d) { return "translate(" + d + ")"; });
