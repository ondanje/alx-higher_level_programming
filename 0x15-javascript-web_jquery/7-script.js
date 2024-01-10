// JavaScript script that fetches the character name from this
// URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character
$(function () {
  $.ajax({
    method: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (data) {
      $('#character').text(data.name);
    },
    error: function () {
      console.error('Failed to fetch');
    }
  });
});
