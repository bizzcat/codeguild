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
sampleSum = 12;

function findSumPairs(intArray, sampleSum) {
  var totalPairs = [];
  var matchedPairs = [];

  for (var i = 0; i < intArray.length; i++) {
    var intTarget = sampleSum - intArray[i];
    if (totalPairs.indexOf(intTarget) === -1 ) {
      totalPairs.push(intArray[i])
    }

    else {
      matchedPairs.push([Math.min(intArray[i], intTarget), Math.max(intArray[i], intTarget)])
    }
  }
  return matchedPairs
}


var matchedPairs = findSumPairs(intArray, sampleSum)
console.log(matchedPairs)











//
