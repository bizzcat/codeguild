"use strict";

var convertWordToLeet = function(originalWord) {
  var leetChars = {
    "o": "0", "l": "1", "e": "3", "a": "4", "t": "7",
  };

  var leetWord = originalWord.toLowerCase();
  for (var originalChar in leetChars) {
    var leetChar = leetChars[originalChar];
    while (leetWord.includes(originalChar)) {
      leetWord =  leetWord.replace(originalChar, leetChar);
    }
  }

  if (leetWord.slice(-1) === "s") {
    leetWord =leetWord.slice(0, -1) + "Z";
  }

  return "(" + leetWord + ")";
};

var convertSentenceToLeet = function(sentence) {
  var originalWords = sentence.split(" ");
  var leetWords = originalWords.map(convertWordToLeet);
  return leetWords.join(" ");
}

var sentence = "fathers brought forth on this continent";



console.log(sentence)
console.log(convertSentenceToLeet(sentence))
