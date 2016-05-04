"use strict";


var totalTaxes = function(amount) {
  var bracketOneWindow = 3350;
  var bracketOneTaxed = (bracketOneWindow * .05);
  var bracketTwoWindow = 8400 - 3351;
  var bracketTwoTaxed = bracketOneTaxed + (bracketTwoWindow * .07);
  var bracketThreeWindow = 125000 - 8401;
  var bracketThreeTaxed = bracketTwoTaxed + (bracketThreeWindow * .09);
  var tax;

  if (amount < 3351) {
    tax = (amount * .05);
  }

  else if (amount < 8401) {
    tax = bracketOneTaxed + ((amount - 3351) * .07);
  }

  else if (amount < 125001) {
    tax = bracketTwoTaxed + ((amount - 8401) * .09);
  }

  else {
    tax = bracketThreeTaxed + ((amount - 125001) * .099);
  }

  return Math.ceil(tax)

}

console.log(totalTaxes(50000))
