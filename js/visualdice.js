// Give the user a number input box with a button "roll". When they click that button,
// make that many 6-sided dice appear on the screen.
//
// The dice should appear visually as dice, although for testing you can just start
// with numbers. Come up with any reasonable way to display the visual dice.
//
// If the user clicks any of the dice, it re-rolls just that one. If they re-click
// the roll button, erase the dice and roll new ones.
//
// At the bottom of the screen, show the sum of all the dice currently out.


function getUserNumber() {
  return parseInt($("#user-number").val());
}

function getDieValues(userNumber) {
  var dieValues = [];
  for (var i = 1; i <= userNumber; i += 1) {
    var value = Math.ceil(Math.random() * 6);
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
      var value = getDieValues(1);
      for (i in value) {
        var newDie = generateDie(value[i]);
        var newDieWithButton = addButtonToDie(newDie);
        setTimeout( function() { buttonWithDie.replaceWith(newDieWithButton); }, 1400);
      }
    })
  return buttonWithDie;
}

function generateDie(dieValue) {
  var die = $("<article></article>");

  if (dieValue === 1) {
    for (i = 1; i <= dieValue; i += 1) {
      die.append($("<p></p>").addClass("dot"));
    }
    die.addClass("die-one");
  }

  if (dieValue === 2) {
    for (i = 1; i <= dieValue; i += 1) {
      die.append($("<p></p>").addClass("dot"));
    }
    die.addClass("die-two");
  }

  if (dieValue === 3) {
    for (i = 1; i <= dieValue; i += 1) {
      die.append($("<p></p>").addClass("dot"));
    }
    die.addClass("die-three");
  }

  if (dieValue === 4) {
    for (i = 1; i <= dieValue; i += 1) {
      if (i % 2) {
        var column = $("<section></section>").addClass("column");
        column.append($("<p></p>").addClass("dot"));
        column.append($("<p></p>").addClass("dot"));
      }
      die.append(column);
    }
    die.addClass("die-four");
  }

  if (dieValue === 5) {
    for (i = 1; i <= dieValue; i += 1) {
      if (i % 2 === 0) {
        var column = $("<section></section>").addClass("column");
        column.append($("<p></p>").addClass("dot"));
        column.append($("<p></p>").addClass("dot"));
      }
      die.append(column);

      if (i % 3 === 0) {
        var column = $("<section></section>").addClass("column");
        column.append($("<p></p>").addClass("dot"));
      }
      die.append(column);

    }
    die.addClass("die-five");
  }

  if (dieValue === 6) {
    for (i = 1; i <= dieValue; i += 1) {
      if (i % 3 === 0) {
        var column = $("<section></section>").addClass("column");
        column.append($("<p></p>").addClass("dot"));
        column.append($("<p></p>").addClass("dot"));
        column.append($("<p></p>").addClass("dot"));
      }
      die.append(column);

    }
    die.addClass("die-six");
  }
  return die;
}


function callAllFunctions() {
  var userNumber = getUserNumber();
  var dieValues = getDieValues(userNumber);
  for (i in dieValues) {
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
























//
