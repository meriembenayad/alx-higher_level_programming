#!/usr/bin/node
/* 4. Prints the number of movies
where the character “Wedge Antilles” is present. */
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;

    for (const movie of data.results) {
      if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  }
});
