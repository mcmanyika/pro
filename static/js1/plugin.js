$(document).ready(function(){
  var $addData = $('.my-ajax-form');
  $addData.submit(function(event){
    event.preventDefault();
    var $formData = $addData.serialize();
    var $thisURL = $addData.attr('data-url') || window.location.href;
    $.ajax({
      method:'POST',
      url: $thisURL,
      data: $formData,
      success: handleSuccess,
      error: handleError,
    });
    function handleSuccess(data){
      console.log(data.message);
      $addData[0].reset()
    }
    function handleError(ThrowError){
      console.log(ThrowError);
    }
  });
});

