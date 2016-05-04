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

function doNothing() {

}

function addButtonToDie(die) {
  var buttonWithDie = $("<button>").append(die);
    buttonWithDie.click(function(event) {
      event.preventDefault();
      buttonWithDie.find($("article")).attr("id", "spin");
      var dieMax = getDieMax();
      var value = getDieValues(1, dieMax);
      for (var i in value) {
        var newDie = generateDie(value[i]);
        var newDieWithButton = addButtonToDie(newDie);
        setTimeout( function() { buttonWithDie.replaceWith(newDieWithButton); }, 1400);
      }
    })
  return buttonWithDie;
}

function generateDie(dieValue) {
  var die = $("<article></article>");
  var fontSize = (90 / dieValue) + "px";

  for (var i = 0; i < dieValue; i += 1) {
    die.append($("<p></p>").attr("height", fontSize).attr("width", fontSize).attr("class", "dot"));
  }
  console.log(die);
  return die;
  // if (dieValue === 1) {
  //   for (i = 1; i <= dieValue; i += 1) {
  //     die.append($("<p></p>").addClass("dot"));
  //   }
  //   die.addClass("die-one");
  // }
  //
  // if (dieValue === 2) {
  //   for (i = 1; i <= dieValue; i += 1) {
  //     die.append($("<p></p>").addClass("dot"));
  //   }
  //   die.addClass("die-two");
  // }
  //
  // if (dieValue === 3) {
  //   for (i = 1; i <= dieValue; i += 1) {
  //     die.append($("<p></p>").addClass("dot"));
  //   }
  //   die.addClass("die-three");
  // }
  //
  // if (dieValue === 4) {
  //   for (i = 1; i <= dieValue; i += 1) {
  //     if (i % 2) {
  //       var column = $("<section></section>").addClass("column");
  //       column.append($("<p></p>").addClass("dot"));
  //       column.append($("<p></p>").addClass("dot"));
  //     }
  //     die.append(column);
  //   }
  //   die.addClass("die-four");
  // }
  //
  // if (dieValue === 5) {
  //   for (i = 1; i <= dieValue; i += 1) {
  //     if (i % 2 === 0) {
  //       var column = $("<section></section>").addClass("column");
  //       column.append($("<p></p>").addClass("dot"));
  //       column.append($("<p></p>").addClass("dot"));
  //     }
  //     die.append(column);
  //
  //     if (i % 3 === 0) {
  //       var column = $("<section></section>").addClass("column");
  //       column.append($("<p></p>").addClass("dot"));
  //     }
  //     die.append(column);
  //
  //   }
  //   die.addClass("die-five");
  // }
  //
  // if (dieValue === 6) {
  //   for (i = 1; i <= dieValue; i += 1) {
  //     if (i % 3 === 0) {
  //       var column = $("<section></section>").addClass("column");
  //       column.append($("<p></p>").addClass("dot"));
  //       column.append($("<p></p>").addClass("dot"));
  //       column.append($("<p></p>").addClass("dot"));
  //     }
  //     die.append(column);
  //
  //   }
  //   die.addClass("die-six");
  // }
  // return die;
}


function callAllFunctions() {
  var userNumber = getUserNumber();
  var dieMax = getDieMax();
  var dieValues = getDieValues(userNumber, dieMax);
  for (var i in dieValues) {
    var die = generateDie(dieValues[i]);
    var buttonWithDie = addButtonToDie(die);
    $("div").append(buttonWithDie);
  }
}

function uponFormSubmission() {
  $("form").on("submit", function(event) {
    event.preventDefault();
    callAllFunctions();
  });
}

uponFormSubmission();
