#!/usr/bin/node
/* global $ */
/* JavaScript script that fetches and lists the title for all movies
  by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
  */
$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.getJSON(url, function (data) {
    const movies = data.results;
    $.each(movies, function (idx, movie) {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    });
  });
});
