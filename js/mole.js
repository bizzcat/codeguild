'use strict';

//  set interval
//  generate random value
//  apply random value to switch picture
//  set action upon click event for cute-mole class

function generateRandomNum() {
  return Math.ceil(Math.random() * 20);
}

function generateRandomImgID(randomNum) {
  return "#img-" + randomNum;
}

function assignNewImage(randomImgID) {
  $(randomImgID).attr("src", "cutemole.jpg");
}

function revertToOriginalImage(randomImgID) {
  setTimeout( function () {
    var currentScore = parseInt($("#score-ticker").text());
    if (currentScore === 0) { }
    else {
      var newScore = parseInt($("#score-ticker").text()) - 4;
      $("#score-ticker").text(newScore);
    }
    $(randomImgID).attr("src", "emptymole.jpg"); }, 1800 );
}

function generation() {
  var randomNum = generateRandomNum();
  var randomImgID = generateRandomImgID(randomNum);
  assignNewImage(randomImgID);
  revertToOriginalImage(randomImgID);
}

var theInterval;

function generateOnInterval() {
  theInterval = setInterval(generation, 1000);
}

function assignClickEventsToAllImages(lives) {
  $("img").each(function () {
    var lives = 3;
    var score = 0;

    $(this).on("click", function(event) {
      if ($(this).attr("class") === "clicked") {
        $(this).attr("class", "");
      }
      else if ($(this).attr("src") === "emptymole.jpg") {
        $(this).attr("class", "clicked");
        if ($("#life-ticker").text() === '0') {
          endGame();
        }
        else {
          $("#life-ticker").text( $("#life-ticker").text() - 1 );
        }
      }
      else {
        $(this).attr("src", "emptymole.jpg").attr("class", "");
        var newScore = parseInt($("#score-ticker").text()) + 14;
        $("#score-ticker").text(newScore);
      }
      }
    )
  })
}

function endGame() {
  $("img").attr("src", "evilrat.png");
  clearInterval(theInterval);
}

var lives = 3;
var score = 0;
$("#life-ticker").text(lives);
$("#score-ticker").text(score);
assignClickEventsToAllImages(lives);
generateOnInterval();
