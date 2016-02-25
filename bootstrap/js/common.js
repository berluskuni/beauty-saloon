$(document).ready(function () {
    $('#login').submit(function(e){
        e.preventDefault();
        var data = $(this).serialize();
        $.ajax({
            type: "POST",
            url: "/auth/login/",
            data: data,
            dataType: "html",
            cache: false,
            statusCode: {
                200: function(){
                    location.replace("http://firstexperience.ru/");
                },
                401: function(){
                    $('#error-login').html('Authentication error');
                },
                405: function(){
                    $('#error-login').html('Method not allowed');
                }
            }
       });
    });
    $('#register').submit(function(e){
        e.preventDefault();
        var data = $(this).serialize();
        $.ajax({
            type: "POST",
            url: "/auth/register/",
            data: data,
            dataType: "html",
            cashe: false,
            statusCode: {
                200: function(){
                    location.replace("http://firstexperience.ru/");
                },
                405: function(){
                    $('#error-login').html('Method not allowed');
                }
            }
        });
    });
});