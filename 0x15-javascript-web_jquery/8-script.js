// Script that fetches and lists the title for all movies by using this URL
// All movie titles must be list in the HTML tag UL#list_movies
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let index in data.results) {
    $('UL#list_movies').append('<li>' + data.results[index].title + '</li>');
  }
});
