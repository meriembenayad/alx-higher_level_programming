#!/usr/bin/node
/* 1. Write a string to a file */
const fs = require('fs');
const filePath = process.argv[2];
const string = process.argv[3];

fs.writeFile(filePath, string, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
