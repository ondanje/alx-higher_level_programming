#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
