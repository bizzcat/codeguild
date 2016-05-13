'use strict';


$(".suspense").on("click", function(event) {
  event.preventDefault();
  $(this).attr("class", "sensation");
  $(this).children().attr("class", "");
})
