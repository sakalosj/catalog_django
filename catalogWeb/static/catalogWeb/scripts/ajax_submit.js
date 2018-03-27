$(document).ready(function() {
    $(".ajax_submit").click(function(event) {
       var link= $(this).attr('href');
       event.preventDefault();
       $.ajax({ data: $("#form1").serialize(),
                type: $("#form1").attr('method'),
                url: $("#form1").attr('action'),
                success: function(response) {
                     console.log(response);
                     if(response['success']) {
                        window.location = link;
                     }
                     if(response['error']) {
                         $("#form_data").html(response['form']);
                     }
                },
                error: function (request, status, error) {
                     console.log(request.responseText);
                }
       });
   });
})
