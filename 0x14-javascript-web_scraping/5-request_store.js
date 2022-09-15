#!/usr/bin/node
// Task 5
// Script that gets the contents of a web and stores it in a file
// The first argument is the URL to request
// The second argument the file path to store the body response
// The file must be UTF-8 encoded
// You must use the module axios

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filepath, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
