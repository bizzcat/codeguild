'use strict';

// Tree configuration
var branches = [];
var seed1 = {i: 0, x: 1000, y: 1200, a: 0, l: 160, d: 0}; // a = angle, l = length, d = depth


var da = 0.6; // Angle delta
var dl = 0.85; // Length delta (factor)
var ar = 0.5; // Randomness
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



function regenerate(initialise) {
  branches = [];
  branch(seed1);
  initialise ? create() : update();
  d3.selectAll('line')
    .on("mouseover", function() {
      d3.select(this).append("svg:title")
          .text("hehe")
      });
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
    .range(["lightgrey","crimson"]);

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

// d3.select('svg')
//   .enter().append("path")
//       .attr("class", "line")
//       .attr("d", 1)
//       .attr('x1', 100)
//       .attr('y1', 100)
//       .attr('x2', 300)
//       .attr('y2', 400)
//       .style("stroke", "black");

function create() {
  d3.select('svg')
    .selectAll('line')
    .data(branches)
    .enter()
    .insert('line',":first-child").on("mouseover", function(d) {
      d3.select(this).append("svg:title")
          .text(d.d)
          })
    .attr('x1', x1)
    .attr('y1', y1)
    .attr('x2', x2)
    .attr('y2', y2)
    .style('stroke-width', function(d) {
        var t = parseInt( maxDepth * .5 + 4 - d.d * .5 );
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


















    //
