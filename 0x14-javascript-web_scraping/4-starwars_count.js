#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
const characterId = 18;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movieData = JSON.parse(body);
    const moviesWithWedge = movieData.results.filter(movie => {
      return movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
    });
    console.log(`${moviesWithWedge.length}`);
  }
});
