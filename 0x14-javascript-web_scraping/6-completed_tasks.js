#!/usr/bin/node
/* 6. Computes the number of tasks completed by user id. */
const request = require('request');
const urlApi = process.argv[2];

request(urlApi, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const completeTasks = {};

    for (const task of data) {
      if (task.completed) {
        if (completeTasks[task.userId]) {
          completeTasks[task.userId]++;
        } else {
          completeTasks[task.userId] = 1;
        }
      }
    }
    console.log(completeTasks);
  } else {
    console.log(error);
  }
});
