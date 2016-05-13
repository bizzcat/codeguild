'use strict';


function getSetup() {
  return $('#joke-setup').val();
}

function getPunchline() {
  return $('#joke-punchline').val();
}

function getJokeSection(jokeSetup, jokePunchline) {
  var setupBlock = $('<blockquote></blockquote>');
  var punchlineBlock = $('<blockquote></blockquote>').attr("class", "hidden");
  var jokeSection = $('<section></section>').attr("class", "suspense");

  setupBlock.text(jokeSetup);
  punchlineBlock.text(jokePunchline);

  jokeSection.append(setupBlock);
  jokeSection.append(punchlineBlock);
  return jokeSection;
}

function appendJokeSection(jokeSection) {
  $('body').append(jokeSection);
}

function sectionClickEvent() {
  $("section").on("click", function(event) {
  event.preventDefault();
  $(this).attr("class", "sensation");
  $(this).children().attr("class", "");
  })
}

function submitJoke() {
  var jokeSetup = getSetup();
  var jokePunchline = getPunchline();
  var jokeSection = getJokeSection(jokeSetup, jokePunchline);
  appendJokeSection(jokeSection);
}

function submitEvent () {
  $("form").on("submit", function(event) {
    event.preventDefault();
    submitJoke();
    sectionClickEvent();
  })
}


submitEvent ();
