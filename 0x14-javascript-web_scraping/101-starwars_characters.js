#!/usr/bin/node
/* 8. Prints all characters of Star Wars movie
in the same order of the list “characters” in the /films/ */
const request = require('request');
const movieId = process.argv[2];
const urlApi = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function printChar (characters, idx) {
  request(characters[idx], (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        printChar(characters, idx + 1);
      }
    }
  });
}

request(urlApi, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body).characters;
    printChar(data, 0);
  } else {
    console.log(error);
  }
});
