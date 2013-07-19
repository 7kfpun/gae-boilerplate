$('#contact_form').submit(function() {
  $.ajax({
    url: 'some-url',
    type: 'post',
    dataType: 'json',
    data: $(this).serialize(),
    success: function(data) {
    }
  });
  return false;
});
