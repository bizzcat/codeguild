// Write a function named find_sum_pairs. It takes two arguments: a list of ints to
// search, and a sum to find.
//
// Go through the search list and find all pairs of numbers that would add
// together to the sum.
//
// Example output:
//
// >>> find_sum_pairs([-1, 0, 1, 2], 3)
// [[1, 2]]
// >>> find_sum_pairs([-1, 0, 1, 2], 1)
// [[-1, 2], [0, 1]]
// >>> find_sum_pairs([2, -1, 2], 1)
// [[2, -1], [-1, 2]]
// >>> find_sum_pairs([-1, 1, 2, 2], 3)
// [[1, 2], [1, 2]]


intArray = [5, 7, 3, 9, 1, -4, 6, 3, 1, 0, 6, -2, -8, 20];
sampleSum = 10;

function findSumPairs(intArray, sampleSum) {
  var matchedPairs = [];

  for (var i = 0; i < intArray.length; i++) {
    var intTarget = sampleSum - intArray[i];

      for (var j = 0; j < intArray.length; j++) {
        if (i === j) { }     // this eliminates an integer from matching with itself
        else if (intArray[j] === intTarget) {
          var matchedPair = new Array(intArray[i], intArray[j]);
          matchedPairs.push(matchedPair);
        }
      }
  }
  return matchedPairs;
}


var matchedPairs = findSumPairs(intArray, sampleSum);
console.log(intArray);
console.log(matchedPairs);











//
