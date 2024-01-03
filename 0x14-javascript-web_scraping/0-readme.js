#!/usr/bin/node
/* 0. Readme */
const file = require('fs');
const filePath = process.argv[2];

file.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
