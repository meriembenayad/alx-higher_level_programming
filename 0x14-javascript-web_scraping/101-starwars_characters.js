#!/usr/bin/node
/* 7. Prints all characters of Star Wars movie */
const request = require('request');
const movieId = process.argv[2];
const urlApi = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(urlApi, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body).characters;

    data.forEach(character => {
      request(character, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        } else {
          console.log(error);
        }
      });
    });
  } else {
    console.log(error);
  }
});
