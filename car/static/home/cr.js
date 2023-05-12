$(document).ready(function() {
    if ($('#emplist') != null) {
      Read();
    }
    $('#EmployeeRegister').validate({
      rules: {
        username: {
          required: true,
          minlength: 4,
          maxlength: 20,
        // remote: {
        //     url: 'username_exists', // The URL to check if the username already exists
        //     type: 'post',
        //     data: {
        //       username: function() {
        //         return  $('#id_username').val();
        //       }
        //     }
         
        }, 
        password1: {
          required: true,
          minlength: 8,
        },
        password2: {
          required: true,
          equalTo: '#id_password1',
        },
        phone_number: {
          required: true,
          minlength: 10,
          maxlength: 10,
          digits: true,
        },
        emp_id: {
          required: true,
          minlength: 6,
          maxlength: 6,
          digits: true,
        },
      },
      messages: {
        username: {
          required: 'Please enter a username.',
          minlength: 'Username must be at least 4 characters long.',
          maxlength: 'Username must be at most 20 characters long.',
          // {% comment %} remote: 'Username already exists. Please choose a different username.', // The message to display if the username already exists {% endcomment %}
        },
        password1: {
          required: 'Please enter a password.',
          minlength: 'Password must be at least 8 characters long.',
        },
        password2: {
          required: 'Please confirm your password.',
          equalTo: 'Passwords do not match.',
        },
        phone_number: {
          required: 'Please enter a phone number.',
          minlength: 'Phone number must be 10 digits long.',
          maxlength: 'Phone number must be 10 digits long.',
          digits: 'Please enter a valid phone number.',
        },
        emp_id: {
          required: 'Please enter an employee ID.',
          minlength: 'Employee ID must be 6 digits long.',
          maxlength: 'Employee ID must be 6 digits long.',
          digits: 'Please enter a valid employee ID.',
        },
      },
      
      submitHandler: function(form) {
        $.ajax({
          type: 'post', // Get the form's method attribute
          url: 'employeeadd', // Get the form's action attribute
          data: $(form).serialize(), // Serialize the form data
          success: function(response) {
            // Handle the server's response here
            alert('Form submitted successfully!');
            Read();
          },
          error: function(xhr, status, error) {
            // Handle errors here
            alert('An error occurred while submitting the form.');
            console.error(xhr.responseText);
          }
        });
      }
    });
  

      $(document).on('click', '.delete', function(){
          $id = $(this).attr('name');
        if(confirm("Are you sure you want to delete this item?")) {
          $.ajax({
              url: 'delete-wm' +"/"+ $id+"/",
              type: 'POST',
              data: {
                  csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
              },
              success: function(){
                  Read();
                 
              }
         
             });
          }
      });
      
 
  
    function Read() {
      $.ajax({
        async: true,
        url: 'EmployeeList',
        type: 'post',
        data: {
          res: 1,
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response) {
          $('#emplist').html(response);
        }
      });
    }
  });