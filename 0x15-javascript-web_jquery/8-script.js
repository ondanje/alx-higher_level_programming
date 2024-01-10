// script that fetches and lists the title for all movies by using this
// URL: https://swapi-api.alx-tools.com/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies
$(function () {
  $.ajax({
    method: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      data.results.forEach(function (movie) {
        $('#list_movies').append('<li>' + movie.title + '</li');
      });
    },
    error: function () {
      console.error('Failed to fetch');
    }
  });
});
