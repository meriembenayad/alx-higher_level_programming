#!/usr/bin/node
const args = process.argv.slice(2);
const argOne = parseInt(args[0]);
const argTwo = parseInt(args[1]);
function add (a, b) {
  return a + b;
}

if (isNaN(argOne) || isNaN(argTwo)) {
  console.log('NaN');
} else {
  console.log(add(argOne, argTwo));
}
