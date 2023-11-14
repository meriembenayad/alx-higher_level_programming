#!/usr/bin/node
const list = require('./100-data').list;

let newList = [];
newList = list.map((idx, value) => value * idx);

console.log(list);
console.log(newList);
