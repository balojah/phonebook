$(function(){
    $(".modalbox").click(function () {
        $("#inline").fadeIn();
        return false;
    })
    $(".popup-close").click(function () {
        $(this).parents("#inline").fadeOut();
        return false;
    })
})
$(function () {
    $(".btn").click(function (event) {
        event.preventDefault();
        $.ajax({
            url: '',
            type: 'post',
            dataType: 'json',
            data: $('form#postform').serialize(),
            success: (function () {
                alert('Saved.');
                location.reload();
            }),
            error: (function (response) {
                const obj = JSON.parse(response.responseText);
                alert('Contact not saved! ' + obj.errors);
            })
            })
            })
        })