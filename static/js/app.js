$('#contact_form').submit(function() {
  $.ajax({
    url: $(this).attr('action'),
    type: $(this).attr('method'),
    dataType: 'json',
    data: $(this).serialize(),
    success: function(data) {
      alert('We get your message!');
    }
  });
  return false;
});
