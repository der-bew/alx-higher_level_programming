#!/usr/bin/node
// prints the title of a Star Wars movie where the episode num matches given int

const request = require('request');
request('http://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
