#!/usr/bin/node
/* 6. Computes the number of tasks completed by user id. */
const request = require('resquest');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let data = JSON.parse(body);
    let results = {};
    for (let i = 0; i < data.length; i++) {
      if (data[i]['completed'] == true) {
        if (results[data[i]['userId'].toString()]) {
          results[data[i]['userId'].toString()]++;
        } else {
          results[data[i]['userId'].toString()] = 1;
        }
      }
    }
    console.log(results);
  }
});
