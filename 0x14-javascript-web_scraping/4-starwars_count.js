#!/usr/bin/node
// Task 4
// Script that prints the number of movies where the character appears
// The first argument is the API URL of the Star wars API
// Wedge Antilles is character ID 18 - your script must use this ID
// You must use the module axios

const request = require('request');
const url = process.argv[2];
request({ url: url, json: true }, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    const films = res.body.results;
    let count = 0;
    for (let f = 0; f < films.length; f++) {
      for (let c = 0; c < films[f].characters.length; c++) {
        if (films[f].characters[c].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
