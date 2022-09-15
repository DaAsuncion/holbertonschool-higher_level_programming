#!/usr/bin/node
// Script that computes the number of tasks completed by user id
// The first argument is the API URL
// Only print users with completed task
// You must use the module axios

const request = require('request');
const url = process.argv[2];
const dictList = {};
request(url, { json: true }, (err, res) => {
  const list = res.body;
  if (err) {
    console.log(err);
  } else {
    for (let i = 0; i < list.length; i++) {
      const key = list[i].userId;
      if (list[i].completed === true) {
        if (!dictList[key]) {
          dictList[key] = 1;
        } else {
          dictList[key] += 1;
        }
      }
    }
    console.log(dictList);
  }
});
