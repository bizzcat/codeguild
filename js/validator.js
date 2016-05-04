// Create a sign-up form for a user to fill out and submit via a button.
//
// It should ask for:
//
// Full Name in "First Last" format
// Age in YYYY-MM-DD format
// Phone Number in 555-555-5555 format

// As the user is typing, you should validate that the fields are filled in the
// correct format. If the content is not currently valid, the field box should be
// yellow and a yellow warning notice describing which field is malformed displayed
// atop the form. If multiple forms are invalid, just show one. I don't care which.
// Otherwise, if valid or empty, the fields should be default and no warning notice
// displayed.
//
// If the user submits with valid info, display a green success notice atop the form,
// otherwise a red error notice.

function onFocusEvent() {
  $("#name-input").focus(function () {
    $("#name-input").attr("class", "focus-event");
  })
  $("#age-input").focus(function () {
    $("#age-input").attr("class", "focus-event");
  })
  $("#phone-input").focus(function () {
    $("#phone-input").attr("class", "focus-event");
  })
}

// function onBlurEvent() {
//   $("#name-input").blur(function() {
//     $("#name-input").attr("class", "blur-event");
//   })
//   $("#age-input").blur(function() {
//     $("#age-input").attr("class", "blur-event");
//   })
//   $("#phone-input").blur(function() {
//     $("#phone-input").attr("class", "blur-event");
//   })
// }

function onKeyUp() {
  $("#name-input").on("keyup", function() {
    validateEntry();
  })
  $("#age-input").on("keyup", function() {
    validateEntry();
  })
  $("#phone-input").on("keyup", function() {
  validateEntry();
  })
}

function onInvalidEntry(entryID) {
  $(entryID).attr("class", "invalid-entry");
  $("p").remove();
  $("#main-container").append($("<p></p>").append("error in " + entryID));

}

function onValidEntry(entryID) {
  $(entryID).attr("class", "valid-entry");
  $("p").remove();
}


function validateEntry() {

// VALIDATES NAME ENTRY
  var nameID = "#name-input";
  var firstLast = $(nameID).val().split(' ');

  if (firstLast.length === 1) {
  }

  else if (firstLast.length === 2) {
    var first = firstLast[0][0]
    var last = firstLast[1][0]
    if ((first === _.capitalize(first)) && (last === _.capitalize(last))) {
      onValidEntry(nameID);
    }
    else { onInvalidEntry(nameID); }
  }
  else { onInvalidEntry(nameID); }


  // VALIDATES AGE ENTRY
  var ageID = "#age-input";
  var birthDate = $(ageID).val().split('-');

  if (birthDate.length === 1) {
  }

  else if (birthDate.length === 3) {
    var year = (birthDate[0].length === 4);
    var month = (birthDate[1].length === 2);
    var day = (birthDate[2].length === 2);
    if (year && month && day) {
      onValidEntry(ageID);
    }
  }
  else { onInvalidEntry(ageID)}


// VALIDATES PHONE ENTRY
  var phoneID = "#phone-input";
  var phoneNumber = $(phoneID).val().split('-');

  if (phoneNumber.length === 1) {
  }

  else if (phoneNumber.length === 3) {
    var one = (phoneNumber[0].length === 3);
    var two = (phoneNumber[1].length === 3);
    var three = (phoneNumber[2].length === 4);
    if (one && two && three) {
      onValidEntry(phoneID);
    }
  }
  else { onInvalidEntry(phoneID) }
}

//
// function pushErrorMsg () {
//   if
// }

// IF INVALID APPEND AN ALERT <p> TO DIV
function onSubmission() {
  $("form").on("submit", function(event) {
    event.preventDefault();
    validateEntry();
  })
}

onFocusEvent();
onKeyUp();

onSubmission();
















//
