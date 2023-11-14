#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const Element of list) {
    if (Element === searchElement) {
      count++;
    }
  }
  return count;
};
