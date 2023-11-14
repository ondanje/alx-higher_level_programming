#!/usr/bin/node
// function that prints the number of arguments already printed and the new argument value

exports.logMe = function logMe (item) {
  // Check if the counter property exists on the 'logMe' function
  if (!logMe.counter) {
    logMe.counter = 0;
  }
  console.log(logMe.counter + ': ' + item);
  logMe.counter++;
};
