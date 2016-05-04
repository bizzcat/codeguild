"use strict";

// Write function that gets the input you want from the user / input boxes/ existing elemtns
// write transformaton funcitons that select exciting elements or make new ones to perform the changes you want
// Link those two things together
// Wire it up using event handler and callbacks

// Give the user a text box that they can enter image URLs into.
// When the user clicks "submit", that image will be added and displayed in an album below.
// Each album image will appear in it's own "tile".
// Each album tile will have a 300 pixels by 300 pixels instance of the image and underneath will be a link to the original image URL and a button to delete the image from the album.
// Layout the tiles in a grid.
// Have a header above the album that displays the total number of images saved.




function getURL() {
  console.log($('#pictureURL').val());
  return $('#pictureURL').val();
}

function getImageFromURL(url) {
  var imageFromURL = $("<img></img>").attr("src", url).attr("height", 300).attr("width", 300);
  // var imageFromURL = $("<img></img>").attr("href", url).attr("height", 300).attr("width", 300);
  return imageFromURL;
}

function putImageInArticle(image) {
  var articleWithImage = $("<article></article>").attr("width", 300);
  return articleWithImage.append(image);
}

function putURLIntoArticle(articleWithImage, url) {
  var linkToURL = $("<a>Link to this image</a>").attr("href", url);
  var articleBox = $("<article></article>");
  articleBox = articleBox.append(linkToURL);
  var articleWithImageAndLink = articleWithImage.append(articleBox);
  return articleWithImageAndLink
}

function createButton(articleWithImageAndLink) {
  var ourButton = $("<button>").text("Delete").attr("href", "");
  ourButton.on("click", function (event) {
    event.preventDefault();
    articleWithImageAndLink.remove();
  })
  return ourButton;
}

function putButtonIntoArticle(articleWithImageAndLink, button) {
  var articleWithImageAndLinkAndButton = articleWithImageAndLink.append(button);
  return articleWithImageAndLinkAndButton;
}


function putArticleInDiv(articleWithImageAndLinkAndButton) {
  $("div").append(articleWithImageAndLinkAndButton);
}


function getSubmission() {
  var ourURL = getURL();
  var ourImage = getImageFromURL(ourURL);
  var articleWithImage = putImageInArticle(ourImage);
  var articleWithImageAndLink = putURLIntoArticle(articleWithImage, ourURL);
  var ourButton = createButton(articleWithImageAndLink);
  var articleWithImageAndLinkAndButton = putButtonIntoArticle(articleWithImageAndLink, ourButton);
  putArticleInDiv(articleWithImageAndLinkAndButton);
}

function registerEverything() {
  $("form").on("submit", function(event) {
    event.preventDefault();
    getSubmission();
  })
}

$(document).ready( function() {
  registerEverything();
});




//
// function getReminderString() {
//     return $("#reminder-input").val();
// }
//
// function createDelLink(reminderElement) {
//     var delLink = $("<a></a>").text("X").attr("href", "");
//     delLink.on("click", function (event) {
//         event.preventDefault();
//         reminderElement.toggleClass("done");
//     });
//     return delLink;
// }
//
// function createReminderElement(reminderString) {
//     var reminderElement = $("<li></li>").text(reminderString);
//     var delLink = createDelLink();
//     return reminderElement.append(delLink);
// }
//
// function addReminderElementToList(reminderElement) {
//     $("#reminder-list").append(reminderElement);
// }
//
// function getReminderStringAndAddElementToList() {
//     var reminderString = getReminderString();
//     var reminderElement = createReminderElement(reminderString);
//     addReminderElementToList(reminderElement);
// }
//
// function registerGlobalEventHandlers() {
//     $("form").on("submit", function (event) {
//         event.preventDefault();
//         getItemStringAndAddElement();
//     });
// }
//
// $(document).ready(function () {
//     registerGlobalEventHandlers();
// });

//
