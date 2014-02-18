function submit_contact_form() {
  console.log("Click");
  that = $("#contact_form");
  $.ajax({
    url: that.attr('action'),
    type: that.attr('method'),
    data: that.serialize(),
    success: function(data) {
      that.find("#success").html('Your mail has been sent. We will contact you soon.');
      setTimeout(function() {
        $('#simple-menu').die().click();
        that.find("input[type=text], input[type=email], input[type=tel], textarea").val("");
        that.find("#success").html('');
      }, 3000)
    },
    error: function(jqXHR, textStatus, errorThrown) {
      console.log(jqXHR, textStatus, errorThrown);
      if (jqXHR.status == 403) {
        that.html(jqXHR.responseText);
      } else {
        that.find("#error").html('Something wrong! Please send us directly to <a href="mailto:mia@getmewrite.com">mia@getmewrite.com</a>');
      }
    }
  });
  return false;
};

function cancel_contact_form() {
  $('#simple-menu').die().click();
  $("#contact_form").find("input[type=text], input[type=email], textarea").val("");
};

$(document).ready(function() {
  $('#simple-menu').sidr();
});
