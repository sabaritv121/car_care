$(document).ready(function() {

  if($('#result1') != null){
    Read();
}

$('#ScheduleAdd').submit(function(event) {
  // Validate the form before submitting

    event.preventDefault(); // Prevent the form from submitting normally
    


    $.ajax({
      type: 'post', // Get the form's method attribute
      url: 'ScheduleAddView', // Get the form's action attribute
      data: $(this).serialize(), // Serialize the form data
      success: function(response) {
        if (response !== 'True') {
          alert('Form validation failed: invalid date or time');
        } else {
          alert('Form submitted successfully!');
          
          Read();
          $('#example').modal('hide');
         
        }
      }
       
    });
  
});


});


function Read(){
$.ajax({
    async : 'true',
    url: 'read',
    type: 'POST',

    data:{
        res: 1,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    },
    success: function(response){
        $('#result1').html(response);
    }
});
}

$(document).ready(function() {
$(document).on("click",".toggle-active-btn",function() {
var category_id = $(this).data('category-id');
var csrf_token = $(this).data('csrf-token');

$.ajax({
  url: '/category/' + category_id + '/toggle-active/',
  method: 'POST',
  data: {
    'csrfmiddlewaretoken': csrf_token
  },
  success: function(response) {
    if (response.status === 'success') {
      $('.toggle-active-btn[data-category-id=' + category_id + ']').text(response.is_active ? 'Disable' : 'Enable');
    } else {
      alert(response.message);
    }
  },
  error: function(xhr, status, error) {
    console.log('Error:', error);
  }
});
});
});
