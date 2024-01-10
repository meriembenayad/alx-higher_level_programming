#!/usr/bin/node
/* global $ */
/* JavaScript script that toggles the class of the <header>
  when the user clicks on the tag DIV#toggle_header
 */
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red').addClass('green');
    } else {
      $('header').removeClass('green').addClass('red');
    }
  });
});
