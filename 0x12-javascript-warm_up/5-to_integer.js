#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv.length === 1 && !isNaN(argv[0])) {
  console.log('My number: ' + parseInt(argv[0]));
} else {
  console.log('Not a number');
}
