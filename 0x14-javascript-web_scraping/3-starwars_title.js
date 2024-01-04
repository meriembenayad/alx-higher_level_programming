#!/usr/bin/node
/* 3. Print the title of Star Wars movie
where the episode number matches a given integer */
const request = require('request');
const episode = process.argv[2];

const endPoint = `https://swapi-api.alx-tools.com/api/films/${episode}`;

request(endPoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
