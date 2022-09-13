#!/usr/bin/node
// Task 3
// Script prints the title of a Star Wars movie where the episode number matches a given int
// The first argument is the movie ID
// You must use the Star wars API with the endpoint
// You must use the module axios

const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request({ url: url, json: true }, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    console.log(res.body.title);
  }
});
