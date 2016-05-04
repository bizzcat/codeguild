"use strict";

var dataDomains = ["Biochemistry"]
var dataJournal = ["The Royal", "The Not So Royal", "The Flesh"]
var dataKeywords = [["Flesh", "CRISPR"], ["Nano", "Lightning"], ["Hello", "hell yeah"]]
var dataArticles = [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]


var branches = [];
var seed = {i: 0, x: 420, y: 600, a: 0, l: 100, d: 0};
var da = 0.3;
var dl = 0.85;
var ar = 0.3;
var maxDepth = 4;


function branch(b) {
  var end = endPt(b), deR, newB;

  branches.push(b);

  if (b.d === maxDepth)
    return;

  var z = 0;
  while ()

  daR = ar * Math.random() - ar * 0.5;
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

}
