#!/usr/bin/node

const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    this.print(c);
  }
}

module.exports = Square;
