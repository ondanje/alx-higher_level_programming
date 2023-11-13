#!/usr/bin/node
// printing I love c 'x times'

const x = process.argv[2];
const parsedInteger = parseInt(x);

if (!isNaN(parsedInteger)) {
  for (let i = 0; i <= parsedInteger; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
