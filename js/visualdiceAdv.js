"use strict";

function getUserNumber() {
  return parseInt($("#user-number").val());
}

function getDieMax() {
  return parseInt($("#die-max").val());
}

function getDieValues(userNumber, dieMax) {
  var dieValues = [];
  for (var i = 1; i <= userNumber; i += 1) {
    var value = Math.ceil(Math.random() * dieMax);
    dieValues.push(value);
  }
  return dieValues;
}

function updateValueheader(dieValues) {
  var sum = _.sum(dieValues);
  $("h2").text(sum);
}

function deletePreviousDie() {
  $("button").remove();
}

function addButtonToDie(die) {

  die.mouseover(function () {
    die.css({ "background-color": "lightyellow" });
  })

  var buttonWithDie = $("<button>").append(die);

  die.mouseout(function () {
    die.css({ "background-color": "rgba(0, 0, 0, 0.275)" });
    var dieMax = getDieMax();
    var value = getDieValues(1, dieMax);
    for (var i in value) {
      var newDie = generateDie(value[i]);
      var newDieWithButton = addButtonToDie(newDie);
    }
    setTimeout( function() { die.attr("id", "spin"); }, 200);
    setTimeout( function() { buttonWithDie.replaceWith(newDieWithButton); }, 1400);
  })
  return buttonWithDie;
}

function generateDie(dieValue) {
  var die = $("<article></article>");

  if (dieValue === 1) {
    for (i = 1; i <= dieValue; i += 1) {
      die.append($("<div></div>").addClass("first-six"));
    }
    die.addClass("die-one");
  }

  if (dieValue === 2) {
    for (i = 1; i <= dieValue; i += 1) {
      die.append($("<div></div>").addClass("first-six"));
    }
    die.addClass("die-two");
  }

  if (dieValue === 3) {
    for (i = 1; i <= dieValue; i += 1) {
      die.append($("<div></div>").addClass("first-six"));
    }
    die.addClass("die-three");
  }

  if (dieValue === 4) {
    for (i = 1; i <= dieValue; i += 1) {
      if (i % 2) {
        var column = $("<p></p>").addClass("column");
        column.append($("<div></div>").addClass("first-six"));
        column.append($("<div></div>").addClass("first-six"));
      }
      die.append(column);
    }
    die.addClass("die-four");
  }

  if (dieValue === 5) {
    for (i = 1; i <= dieValue; i += 1) {
      if (i % 2 === 0) {
        var column = $("<p></p>").addClass("column");
        column.append($("<div></div>").addClass("first-six"));
        column.append($("<div></div>").addClass("first-six"));
      }
      die.append(column);

      if (i % 3 === 0) {
        var column = $("<p></p>").addClass("column");
        column.append($("<div></div>").addClass("first-six"));
      }
      die.append(column);

    }
    die.addClass("die-five");
  }

  if (dieValue === 6) {
    for (i = 1; i <= dieValue; i += 1) {
      if (i % 3 === 0) {
        var column = $("<p></p>").addClass("column");
        column.append($("<div></div>").addClass("first-six"));
        column.append($("<div></div>").addClass("first-six"));
        column.append($("<div></div>").addClass("first-six"));
      }
      die.append(column);

    }
    die.addClass("die-six");
  }

  if (dieValue > 6) {
    var fontSize = ((110 / dieValue) * 1.1) + "px";
    var marginSize = (Math.sqrt(dieValue) / 1.8) + "px";
    for (var i = 0; i < dieValue; i += 1) {
      die.append($("<div></div>").attr("class", "dot").css({"margin": marginSize, "height": fontSize, "width": fontSize}));
    }
  }

  return die;
}


function callAllFunctions() {
  deletePreviousDie();
  var userNumber = getUserNumber();
  var dieMax = getDieMax();
  var dieValues = getDieValues(userNumber, dieMax);
  updateValueheader(dieValues);
  for (var i in dieValues) {
    var die = generateDie(dieValues[i]);
    var buttonWithDie = addButtonToDie(die);
    $("section").append(buttonWithDie);
  }
}

function uponFormSubmission() {
  $("form").on("submit", function(event) {
    event.preventDefault();
    callAllFunctions();
  });
}

uponFormSubmission();
