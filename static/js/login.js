var validemail = false
var validpass = false
$(document).ready(function(){
    $('#email').on('input', function(){
        var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
        if ($(this).val() != '') {
            if ($(this).val().match(pattern)) {
                $(this).removeClass('invalid');
                $(this).addClass('valid');
                $('#foremail').removeClass('invalid');
                $('#foremail').addClass('valid');
                validemail = true
            } else {
                $(this).removeClass('valid');               
                $(this).addClass('invalid');
                $('#foremail').removeClass('valid');
                $('#foremail').addClass('invalid');
            };
        };
    });
    $('#password').on('input', function(){
        if ($(this).val().length >= 8) {
            $(this).removeClass('invalid');
            $(this).addClass('valid');
            $('#forpassword').removeClass('invalid');
            $('#forpassword').addClass('valid');
            validpass = true
        }
         else {
            $(this).removeClass('valid');            
            $(this).addClass('invalid');
            $('#forpassword').removeClass('valid');
            $('#forpassword').addClass('invalid');
        };
    });
});

$('.login-btn').click(function(e){
    e.preventDefault()
    var email = $('#email').val()
    var password = $('#password').val()
    var csrf_token = $("input[name='csrfmiddlewaretoken']").val()
    const form_data = new FormData()
    form_data.append('csrfmiddlewaretoken', csrf_token)
    form_data.append('email', email)
    form_data.append('password', password)
    if (validemail == true && validpass == true) {
        $.ajax({
            type: 'POST',
            url: "",
            enctype: "form-data",
            data: form_data,
            success: function(argument) {
                window.location.href = "/";
            },
            cache: false,
            contentType: false,
            processData: false
        });
    }
})
