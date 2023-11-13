#!/usr/bin/node
// printing arguments

const numOfArgs = process.argv;

if (numOfArgs.length === 2) {
  console.log('No argument');
} else if (numOfArgs.length === 3) {
  console.log('Arguments found');
} else {
  console.log('Arguments found');
}
