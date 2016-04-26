"use strict";

var namesToAges = {
    "Alyssa": 22,
    "Charley": 25,
    "Dan": 25,
    "Jeff": 20,
    "Kasey": 20,
    "Kim": 20,
    "Morgan": 25,
    "Ryan": 25,
    "Stef": 22
};


var ageToCount = {};
var getRarestAge = function(namesToAges) {

  for (var name in namesToAges) {
    var temp = namesToAges[name];
    if (temp in ageToCount) {
      ageToCount[temp] += 1;
    }
    else {
      ageToCount[temp] = 1;
    }
  };

  var countToAge = {};
  for (var temp in ageToCount) {
    if (ageToCount.hasOwnProperty(temp)) {
      countToAge[ageToCount[temp]] = temp;
    }
  };

  var counts = Object.keys(countToAge);
  var lowestAge = Math.min( ...counts );

  return lowestAge;


};

console.log("The least common age among our group is: " + getRarestAge(namesToAges) + " years old.");
