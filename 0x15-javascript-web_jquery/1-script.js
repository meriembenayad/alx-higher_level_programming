#!/usr/bin/node
/* global $ */
/* JavaScript script that updates the text color of the <header> using JQuery */
$(document).ready(function () {
  const header = $('header');
  header.css('color', 'FF0000');
});
