var diameter = 1000;

var margin = {top: 20, right: 120, bottom: 20, left: 120},
    width = diameter,
    height = diameter;

var i = 0,
    duration = 550,
    root;

var tree = d3.layout.tree()
    .size([360, diameter/2 - 80])
    .separation(function(a, b) { return (a.parent == b.parent ? 1 : 10) / a.depth; });

var diagonal = d3.svg.diagonal.radial()
    .projection(function(d) { return [d.y, d.x / 180 * Math.PI]; });

var svg = d3.select("body").append("div").attr("id", "visualization").append("svg")
    .attr("width", width + 500 )
    .attr("height", height - 100 )
    .call(d3.behavior.zoom()
      .scaleExtent([0, 3])
      .on("zoom", function () {
        d3.select('g').attr("transform", "translate(" + d3.event.translate + ")" + " scale(" + d3.event.scale + ")")
    }))
  .append("g")
    .attr("transform", "translate(" + diameter / 2 + "," + diameter / 2 + ")");

root = data_json_str;
root.x0 = 0;
root.y0 = 0;

root.children.forEach(collapse); // start with all children collapsed
update(root);

d3.select(self.frameElement).style("height", "1300px"); // beginning frame

function update(source) {

  // Compute the new tree layout.
  var nodes = tree.nodes(root),
      links = tree.links(nodes);

  // Normalize for fixed-depth.
  nodes.forEach(function(d) { d.y = d.depth * 380; });

  // Update the nodes…
  var node = svg.selectAll("g.node")
      .data(nodes, function(d) { return d.id || (d.id = ++i); });

  // Enter any new nodes at the parent's previous position.
  var nodeEnter = node.enter().append("g")
      .attr("class", "node")
      //.attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + d.y + ")"; })
      .on("click", click);

  nodeEnter.append("circle")
      .attr("r", 1e-6)
      .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

  nodeEnter.append("text")
      // .style("fill", function(d) { return d.depth === 1 ? "green" : "black"; }) ***************************USE THIS METHOD TO GENERATE AND APPEND A TEXT BOX WHEN SOMEONE CLICKS ON AN ARTICLE
      .attr("x", 10)
      .attr("dy", ".35em")
      .attr("font-size", function(d) {
        if (d.depth === 0) { return "10px" }
        else if (d.depth === 1) { return "15px" }
        else if (d.depth === 2) { return "20px"}
        else if (d.depth === 3) { return "25px"}
        else { return "10px" }
      })
      .attr("text-anchor", "start")
      .attr("transform", function(d) { return d.x < 180 ? "translate(0)" : "rotate(180)translate(-" + (d.name.length * 8.5)  + ")"; })
      .text(function(d) { return d.name; })
      .style("fill-opacity", 1e-6);

  // Transition nodes to their new position.
  var nodeUpdate = node.transition()
      .duration(duration)
      .attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + d.y + ")"; })

  nodeUpdate.select("circle")
      .attr("r", 4.5)
      .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; })
      // .attr('y', function(d) { return d.y * 300 } );

  nodeUpdate.select("text")
      .style("fill-opacity", 1)
      .attr("transform", function(d) { return "translate(0)"; });

  // TODO: appropriate transform
  var nodeExit = node.exit().transition()
      .duration(duration)
      //.attr("transform", function(d) { return "diagonal(" + source.y + "," + source.x + ")"; })
      .remove();

  nodeExit.select("circle")
      .attr("r", 1e-6);

  nodeExit.select("text")
      .style("fill-opacity", 1e-6);

  // Update the links…
  var link = svg.selectAll("path.link")
      .data(links, function(d) { return d.target.id; });

  // Enter any new links at the parent's previous position.
  link.enter().insert("path", "g")
      .attr("class", "link")
      .attr("d", function(d) {
        var o = {x: source.x0, y: source.y0};
        return diagonal({source: o, target: o});
      });

  // Transition links to their new position.
  link.transition()
      .duration(duration)
      .attr("d", diagonal);

  // Transition exiting nodes to the parent's new position.
  link.exit().transition()
      .duration(duration)
      .attr("d", function(d) {
        var o = {x: source.x, y: source.y};
        return diagonal({source: o, target: o});
      })
      .remove();

  // Stash the old positions for transition.
  nodes.forEach(function(d) {
    d.x0 = d.x;
    d.y0 = d.y;
  });
}

// Toggle children on click.
function click(d) {
  if (d.children) {
    d._children = d.children;
    d.children = null;
  }
  else {
    d.children = d._children;
    d._children = null;
  }
  // .call(d3.behavior.zoom()
  //   .scaleExtent([0, 3])
  //   .on("zoom", function () {
  //     d3.select('g').attr("transform", "translate(" + d3.event.translate + ")" + " scale(" + d3.event.scale + ")")
  // }))

  update(d);
}

// Collapse nodes
function collapse(d) {
  if (d.children) {
      d._children = d.children;
      d._children.forEach(collapse);
      d.children = null;
    }
}
