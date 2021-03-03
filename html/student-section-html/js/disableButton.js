$(document).ready(function() {
  //when you upload file, disabled equals false
  $('#file').change(function() {
    $('#submit').attr('disabled',false);
  });
});
