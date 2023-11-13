#!/usr/bin/node
// converting ti integer

const firstArgument = process.argv[2];
const parsedInteger = parseInt(firstArgument);

if (!isNaN(parsedInteger)) {
  console.log(`My number: ${parsedInteger}`);
} else {
  console.log('Not a number');
}
