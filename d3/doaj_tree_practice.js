'use strict';


// Tree configuration
var branches = [];
var seed1 = {i: 0, x: 650, y: 650, a: 0, l: 120, d: 0}; // a = angle, l = length, d = depth
// var seed2 = {i: 0, x: 650, y: 650, a: 2.095, l: 100, d: 0};
// var seed3 = {i: 0, x: 650, y: 650, a: -2.095, l: 80, d: 0};
var seed2 = {i: 0, x: 650, y: 650, a: 1, l: 110, d: 0};
var seed3 = {i: 0, x: 650, y: 650, a: 2, l: 100, d: 0};
var seed4 = {i: 0, x: 650, y: 650, a: 3, l: 90, d: 0};
var seed5 = {i: 0, x: 650, y: 650, a: 4, l: 80, d: 0};
var seed6 = {i: 0, x: 650, y: 650, a: 5, l: 70, d: 0};
var seed7 = {i: 0, x: 650, y: 650, a: 6, l: 60, d: 0};
var seed8 = {i: 0, x: 650, y: 650, a: 1, l: 50, d: 0};
var seed9 = {i: 0, x: 650, y: 650, a: 2, l: 40, d: 0};
var seed10 = {i: 0, x: 650, y: 650, a: 3, l: 30, d: 0};
var seed11 = {i: 0, x: 650, y: 650, a: 4, l: 20, d: 0};
var seed12 = {i: 0, x: 650, y: 650, a: 5, l: 10, d: 0};
var seed13 = {i: 0, x: 650, y: 650, a: 6, l: 4, d: 0};

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



function regenerate(initialise) {
  branches = [];
  branch(seed13);
  branch(seed12);
  branch(seed11);
  branch(seed10);
  branch(seed9);
  branch(seed8);
  branch(seed7);
  branch(seed6);
  branch(seed5);
  branch(seed4);
  branch(seed3);
  branch(seed2);
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
    .domain([0, maxDepth])
    .range(["white","purple"]);

function x1(d) {return d.x;}
function y1(d) {return d.y;}
function x2(d) {return endPt(d).x;}
function y2(d) {return endPt(d).y;}
function highlightParents(d) {
  var colour = d3.event.type === 'mouseover' ? 'green' : color(d.d);
  var depth = d.d;
  for (var i = 0; i <= depth; i++) {
    d3.select('#id-'+parseInt(d.i)).style('stroke', colour);
    d = branches[d.parent];
  }
}

function create() {
  d3.select('svg')
    .selectAll('line')
    .data(branches)
    .enter()
    .insert('line',":first-child")
    .attr('x1', x1)
    .attr('y1', y1)
    .attr('x2', x2)
    .attr('y2', y2)
    .style('stroke-width', function(d) {
        var t = parseInt(maxDepth*.5 +1 - d.d*.5);
        return  t + 'px';
    })
    .style('stroke', function(d) {
        return color(d.d);
    })
    .attr('id', function(d) {
      return 'id-'+d.i;
    })
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
