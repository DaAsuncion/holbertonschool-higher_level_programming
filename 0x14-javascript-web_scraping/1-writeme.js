#!/usr/bin/node
// Task 1
// Write a script that writes a string to a file
// The first argument is the file path
// The second argument is the string to write
// The content of the file must be written in utf-8
// If an error occurred during while writing,print the error obj

const fs = require('fs');
const filepath = process.argv[2];
const contents = process.argv[3];
fs.writeFile(filepath, contents, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
