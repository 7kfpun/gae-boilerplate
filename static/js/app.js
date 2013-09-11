$('#contact_form').submit(function() {
  that = $(this);
  $.ajax({
    url: that.attr('action'),
    type: that.attr('method'),
    data: that.serialize(),
    success: function(data) {
      $('#contactModal').modal('show');
      that.find("input[type=text], input[type=email], textarea").val("");
    },
    error: function(data) {
      console.log('Fail!');
    }
  });
  return false;
});

$('#nav li a').click(function() {
  $(this).tab('show');
})
