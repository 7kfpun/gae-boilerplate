$('#contact_form').submit(function() {
  that = $(this);
  $.ajax({
    url: that.attr('action'),
    type: that.attr('method'),
    data: that.serialize(),
    success: function(data) {
      $('#contactModal').modal('show');
      that.find("input, textarea").val("");
    },
    error: function(data) {
      console.log('Fail!');
    }
  });
  _gaq.push(['_trackEvent', 'Contact', 'Send message', 'Contact Form',, false]);
  return false;
});

$('#nav li a').click(function() {
  $(this).tab('show');
})

setTimeout(function() {
  $('#promoModal').modal('show');
  _gaq.push(['_trackEvent', 'Contact', 'Popup contact form', 'Contact Form',, false]);
}, 1000 * 60 * 10);

$('#promoModaltoContact').click(function() {
  $('#promoModal').modal('hide');
  $('#contact_form input[name="name"]').focus();
  _gaq.push(['_trackEvent', 'Contact', 'Close contact form', 'Contact Form',, false]);
});
