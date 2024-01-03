#!/usr/bin/node
// script that writes a string to a file.

const fs = require('fs');
const filepath = process.argv[2];
const stringtowrite = process.argv[3];

fs.writeFile(filepath, stringtowrite, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
