#!/usr/bin/node
/* global $ */
/* JavaScript script that fetches the character name
  from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
 */
$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.getJSON(url, function (data) {
    $('#character').text(data.name);
  });
});
