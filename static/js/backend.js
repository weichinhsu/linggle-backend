$('#about').on('click', function () {
  $('main').load("{% include 'about.html' %}")
})