#!/usr/bin/node
/* 4. Prints the number of movies
where the character “Wedge Antilles” is present. */
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log('Request failed: ', error);
  } else if (response.statusCode !== 200) {
    console.log('Unexpected status code: ', error);
  } else {
    let data;
    try {
      data = JSON.parse(body).results;
      let count = 0;
      for (const movie in data) {
        for (const char of data[movie].characters) {
          if (char.search('/18/') > 0) {
            count++;
          }
        }
      }
      console.log(count);
    } catch (error) {
      console.log('Failed to parse response body: ', error);
    }
  }
});
