 
         
          $(document).ready(function() {
            
            $('#LoginRegister').validate({
              rules: {
              username: {
                  required: true,
                  minlength: 4,
                  maxlength: 20,
                // remote: 
                //     url: 'username_exists', // The URL to check if the username already exists
                //     type: 'post',
                //     data: {
                //       username: function() {
                //         return $('#id_username').val();
                //       }
                //     }
                //    }  
                  
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
                
              },
              messages: {
                username: {
                  required: 'Please enter a username.',
                  minlength: 'Username must be at least 4 characters long.',
                  maxlength: 'Username must be at most 20 characters long.',
                //   {% comment %} remote: 'Username already exists. Please choose a different username.', // The message to display if the username already exists  {% endcomment %}
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
                
              },
              
              submitHandler: function(form) {
                $.ajax({
                  type: 'post', // Get the form's method attribute
                  url: 'UserAddView', // Get the form's action attribute
                  data: $(form).serialize(), // Serialize the form data
                  success: function(response) {
                    // Handle the server's response here
                    alert('Form submitted successfully!');
                    $('#exampleModal').modal('hide');
                   
               
                  },
                  error: function(xhr, status, error) {
                    // Handle errors here
                    alert('An error occurred while submitting the form.');
                    console.error(xhr.responseText);
                  }
                });
              }
            });
          
            
          });

            
     