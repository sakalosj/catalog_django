$(document).ready(function()
{
    $("#show_hide_form").click(function (e) {
        // {#alert('working')#}
        e.preventDefault()
        $(".filter_form").slideToggle(toggle_filter_text)

    })

    // $( ".filter_form" ).change(function() {
    //     alert( "Handler for .change() called." );
    // });
})

function toggle_filter_text() {

    var toggle_filter_text = ''
    if ($(".filter_form").is(":visible")){
        toggle_filter_text = "Hide filter"
    } else {

        toggle_filter_text = "Show filter"
    }
    $("#show_hide_form").html(toggle_filter_text)

}
