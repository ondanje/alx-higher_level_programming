#!/usr/bin/node

const numOfArgs = process.argv;

if (numOfArgs[2] === undefined) {
  console.log('No argument');
} else {
  console.log(numOfArgs[2], 'is', numOfArgs[3]);
}
