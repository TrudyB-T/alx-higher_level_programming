$.ajax({
    method: 'GET',
    url: 'https://swapi.co/api/people/5/?format=json',
    success: function (data) {
      $('DIV#character').text(data.name);
    }
  });
});
