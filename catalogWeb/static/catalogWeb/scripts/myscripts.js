// $(document).ready(function () { //tabs handling - tab effect is that in data-store is poinintg to
//     $('ul.tabs li').click(function () {
//         $('ul.tabs li').removeClass('current_tab'); //current_tab class is poinitng to active tab
//         $(this).addClass('current_tab');
//         get_table();
//     });
// });
//
// /****************************
//  *** db queries
//  ***
//  *** todo: add queries to datastructure (array)
//  *****************************/
// var dbscript = ""; //used to store db phpp based on form id
// var columns = {};
// var output = "";
//
// $(function () {// onready shorthand
//     //Listener for navbar list entries and subelemnts clicks
//     $("navbar_left ul li").click(functionParser);
//
//     //Listener for submit event in popup form
//     $(document).on('submit', '.popupform', ajaxCall);       //listener for pupforms submit type button
//
//     //Listener for button type button in popop form - rework to be more specific, it is for popup closing
//     //$(document).on('click keypress','.popupform *[type="button"]',disablePopup);
//     $(document).on('click', '.popupform *[type="button"]', disablePopup);
//     /*$(document).on('keyup','.popupform',function(event){
//      var KEYCODE_ESC = 27;
//      if (event.keyCode == KEYCODE_ESC){
//      disablePopup();
//      }
//      });*/
//
//     //Listener for table rows - header excluded
//     $(document).on('click', '#db_table tr:not(#head)', (function () {
//         var id = $(this).find('td:first').text();
//         //alert('You clicked ' + id);
//         show_popup(id);
//     }));
//
//     //Initial table load after html is ready
//     get_table();
// });
//
//
// function functionParser(e) { //choosing right function and preparing info for next function call
//     if (e.target == e.currentTarget) {
//         e.stopPropagation();
//     }
//     var button_id = this.id;  //id of pressed button in left nav menu
//     dbscript = "scripts/" + $(".current_tab").attr('data-tab') + "_" + button_id.replace(/_nav_but_form/i, ".php"); // taking id from target event (clicked button) and building script string for ajax calll
//
//     if (button_id.search("nav_but_form") > -1) { //cheking type of button pressed nav -location in navbar_left, but - button, form - popou form / ref - refresh
//         var popup_form_id = "#" + $(".current_tab").attr('data-tab') + "_" + button_id.replace(/nav_but_form/i, "form");
//         loadPopup(popup_form_id);
//     }
//
//     if (button_id.search("nav_but_ref") > -1) {
//         get_table();
//     }
// }
//
// function get_table() { //ajax call to list table - rework to jquery
//     var s = "scripts/" + $(".current_tab").attr('data-tab') + "_list.php"; // building script path based on current_tab
//
//     var xmlhttp = new XMLHttpRequest();
//     xmlhttp.onreadystatechange = function () {
//         if (this.readyState == 4 && this.status == 200) {
//             document.getElementById("db_table_container").innerHTML = this.responseText;
//         }
//         ;
//
//     }
//     xmlhttp.open("GET", s, true);
//     xmlhttp.send();
//
// }
// //http://stackoverflow.com/questions/5004233/jquery-ajax-post-example-with-php
// //http://stackoverflow.com/questions/2019608/pass-entire-form-as-data-in-jquery-ajax-function
// function ajaxCall(e) {
//     var request;
//     console.log(e);
//     e.preventDefault();
//
//     if (request) {
//         request.abort();
//     }
//
//     var $form = $(this);
//     var $inputs = $form.find("input, select, button, textarea");
//     var serializedData = $form.serialize();
//     //console.log(serializedData);
//
//     // Let's disable the inputs for the duration of the Ajax request.
//     // Note: we disable elements AFTER the form data has been serialized.
//     // Disabled form elements will not be serialized.
//     $inputs.prop("disabled", true);
//     //console.log(dbscript);
//     // Fire off the request to /form.php
//     request = $.ajax({
//         url: dbscript,
//         type: "post",
//         data: serializedData
//     });
//
//     // Callback handler that will be called on success
//     request.done(function (response, textStatus, jqXHR) {
//         // Log a message to the//console
//         //console.log("Hooray, it worked!");
//     });
//
//     // Callback handler that will be called on failure
//     request.fail(function (jqXHR, textStatus, errorThrown) {
//         // Log the error to the//console
//         console.error(
//                 "The following error occurred: " +
//                 textStatus, errorThrown
//                 );
//     });
//
//     // Callback handler that will be called regardless
//     // if the request failed or succeeded
//     request.always(function () {
//         // Reenable the inputs
//         $inputs.prop("disabled", false);
//         $('.active_popup *[type="button"]').trigger("click");  //triggers click event on active form cancel button
//         get_table();
//     });
// }
// ;
//
// /*
//  /****************************
//  *** popup scripts
//  ***
//  *** todo:
//  *****************************/
//
//
//
// //loading popup with jQuery magic!
// function loadPopup(element_id, e) {
//     //console.log("loadpopup"+e);
//     //console.log(e);
//
//     //form = "#"+$(".current_tab").attr('data-tab')+"_"+e.target.id.replace(/nav_but_form/i, "form");
//     //var popup_form_id =  "#"+$(".current_tab").attr('data-tab')+"_"+button_id.replace(/nav_but_form/i, "form");
//     //console.log(form);
//     //loads popup only if it is disabled
//
//     $("#popupdiv").css({
//         "display": "flex"
//     });
//     $(element_id).css({
//         "display": "block"
//     });
//     $("#popupdiv").fadeIn("fast");
//     $(element_id).fadeIn("fast");
//     $(element_id).addClass('active_popup');
//
// }
//
// function disablePopup(event) {
//     var element_id = "#" + this.parentElement.id;
//
//     alert(event.type);
//     //if
//     $("#popupdiv").fadeOut("slow");
//     $(".active_popup").fadeOut("slow");
//     $("#popupdiv").css({
//         "display": "none"
//     });
//     $(".active_popup").css({
//         "display": "none"
//     });
//     $(element_id).removeClass('active_popup');
//
// }
//
//
// /***********************
//  **** Dynamic POPUP FORMS functions
//  ***********************/
// var $popup_stack = [];
//
//
//     $(document).keydown(function(e) {
//      if (e.keyCode == 27) { // escape key maps to keycode `27`
//         //alert(event.type);
//         destroy_popup();
//     }
// });
//
// function show_popup(id) {
//     $popup_stack.push(id); // if db fail it will be not removed
//     get_db_data(create_popup2);
// }
//
// function get_db_data(callback) { //ajax call to field names of table
//
//     //set vars - script and current table = current tab
//     var table = $(".current_tab").attr('data-tab');
//
//     request = $.ajax({
//         type: "POST",
//         url: "scripts/db_get.php",
//         data: "table=" + table,
//     });
//     request.done(function (response) {
//         callback(response);
//         columns = JSON.parse(response);
//         output = JSON.parse(response);
//         //console.log(response);
//         //return (response);
//     });
// }
//
//
//
//
//
//
//
// function create_popup2(json_data) {
//     console.log(json_data);
//     console.log(JSON.parse(json_data));
//     var $response = JSON.parse(json_data);
//     var c = $response.table_data;
//
//     $("#popup_template").append("<h2>" + $(".current_tab").attr('data-tab') + "</h2>");
//     for (var $category in $response) {
//         if ( $category === "table_data"){
//             for (var $entry in $response[$category]) {
//                 $("#popup_template").append("<h3>" + $entry + ":</h3>" + $response[$category][$entry]);
//             }
//         }
//         if ( $category === "picture"){
//             for (var $id in $response[$category]) {
//                 //$img_element = "<img src=\"$response[$category][$id][\"path\"]>";
//                 $img_element = "<img src="+$response[$category][$id]["path"]+">";
//                 $("#popup_template").append($img_element);
//             }
//         }
//
//     }
//
//     //<img src="smiley.gif" alt="Smiley face" height="42" width="42">
//
//
//     load_popup2("#popup_container");
// }
//
// function load_popup2(element_id, e) {
//
//
//     $("#popup_container").css({
//         "display": "flex"
//     });
//     $("#popup_template").css({
//         "display": "block"
//     });
//     $("#popup_container").fadeIn("fast");
//     $("#popup_template").fadeIn("fast");
//     $("#popup_template").addClass('active_popup');
// }
//
// function destroy_popup() {
//     $popup_stack.pop(); //remove current
//     $previous_popup = $popup_stack.pop();
//      if ($previous_popup !== undefined){
//          loadPopup2($previous_popup);
//      }
//     //var element_id = "#" + this.parentElement.id;
//
//     //alert(event.type);
//     //if
//     $("#popup_container").fadeOut("slow");
//     $(".active_popup").fadeOut("slow");
//     $("#popup_container").css({
//         "display": "none"
//     });
//     $(".active_popup").css({
//         "display": "none"
//     });
//     //$(element_id).removeClass('active_popup');
//     $(".active_popup").removeClass('active_popup');
//     $("#popup_template").empty();
// }
//
//
// /*****************************
//  ***   TRANSLATION MATRIX   ***
//  ******************************/
// tran = {first_name: {
//         sk: "Meno"},
//     last_name: {
//         sk: "Priezvisko"},
//     id: {
//         sk: "ID"}
// }

//
// /*****************************
//  ***   django   ***
//  ******************************/
//
// function set_variable(variable,value) {
//     alert('ide!!!!!')
//     $("#db_table_container").empty;
//     posting = $.post("/ddd", {
//             variable: variable,
//             value: value,
//             csrfmiddlewaretoken: csrftoken
//         }
//     );
//     posting.done(function (data) {
//             var content = $(data).find("#content");
//             $("#db_table_container").html(data);
//
//         }
//     )
// }
//
// $("#send-my-url-to-django-button").click(function() {
//             $.ajax({
//                 url: "/process_url_from_client",
//                 type: "POST",
//                 dataType: "json",
//                 data: {
//                     url: url,
//                     csrfmiddlewaretoken: '{{ csrf_token }}'
//                     },
//                 success : function(json) {
//                     alert("Successfully sent the URL to Django");
//                 },
//                 error : function(xhr,errmsg,err) {
//                     alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
//                 }
//             });
//         });
//
//
// function get_table_django() { //ajax call to list table - rework to jquery
//     var s = "scripts/" + $(".current_tab").attr('data-tab') + "_list.php"; // building script path based on current_tab
//
//     var xmlhttp = new XMLHttpRequest();
//     xmlhttp.onreadystatechange = function () {
//         if (this.readyState == 4 && this.status == 200) {
//             document.getElementById("db_table_container").innerHTML = this.responseText;
//         }
//         ;
//
//     }
//     xmlhttp.open("GET", s, true);
//     xmlhttp.send();
//
// }

$(document).ready(function () { //tabs handling - tab effect is that in data-store is poinintg to
    $('ul.nav li').click(function () {
        $('ul.nav li.active').removeClass('active'); //current_tab class is poinitng to active tab
        $(this).addClass('active');
    });
});