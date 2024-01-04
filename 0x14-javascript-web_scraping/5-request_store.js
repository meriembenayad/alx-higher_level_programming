#!/usr/bin/node
/* 5. Gets content of webpage
and stores it in a file */
const request = require('request');
const fs = require('fs');
const urlPage = process.argv[2];
const filePath = process.argv[3];

request(urlPage, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(error);
  }
});
