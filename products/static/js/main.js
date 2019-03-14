

function getCookie(name) {
    var cookieValue = null;

    if (document.cookies && document.cookie !== '') {
        var cookie = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);

            if (cookie.substring(0, name.length + 1 ) === (name + '=')) {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
 }

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$('button').on('click', function(event){
    event.preventDefault();
    var element = $(this);

    $.ajax({
        url: '/buy_product/',
        type: 'GET',
        data: { product_id: element.attr("data-id")},
        success: function(response){
                        element.html('Stack: ' + response);
                    }

        });
    });