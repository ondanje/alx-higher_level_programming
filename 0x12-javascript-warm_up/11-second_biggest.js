#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(arg => parseInt(arg));
  const sortedNumbers = numbers.sort((a, b) => b - a);

  console.log(sortedNumbers[1]);
}
