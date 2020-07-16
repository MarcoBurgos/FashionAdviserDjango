$(function() {
  "use strict";



  // //------- Sticky Header -------//
  // $(".sticky-header").sticky();

  // //------- video popup -------//
  // $(".hero-banner__video, .video-play-button").magnificPopup({
  //   disableOn: 700,
  //   type: "iframe",
  //   mainClass: "mfp-fade",
  //   removalDelay: 160,
  //   preloader: false,
  //   fixedContentPos: false
  // });

  // //------- mailchimp --------//
	// function mailChimp() {
	// 	$('#mc_embed_signup').find('form').ajaxChimp();
  // }
  // mailChimp();

  var nav_offset_top = $('header').height() + 50;
    /*-------------------------------------------------------------------------------
	  Navbar
	-------------------------------------------------------------------------------*/

	//* Navbar Fixed
    function navbarFixed(){
        if ( $('.header_area').length ){
            $(window).scroll(function() {
                var scroll = $(window).scrollTop();
                if (scroll >= nav_offset_top ) {
                    $(".header_area").addClass("navbar_fixed");
                } else {
                    $(".header_area").removeClass("navbar_fixed");
                }
            });
        };
    };
    navbarFixed();


  if ($('.blog-slider').length) {
    $('.blog-slider').owlCarousel({
        loop: true,
        margin: 30,
        items: 1,
        nav: true,
        autoplay: 2500,
        smartSpeed: 1500,
        dots: false,
        responsiveClass: true,
        navText : ["<div class='blog-slider__leftArrow'><img src='static/images/left-arrow.png'></div>","<div class='blog-slider__rightArrow'><img src='static/images/right-arrow.png'></div>"],
        responsive:{
          0:{
              items:1
          },
          600:{
              items:2
          },
          1000:{
              items:3
          }
      }
    })
  }

  //------- mailchimp --------//
	// function mailChimp() {
	// 	$('#mc_embed_signup').find('form').ajaxChimp();
	// }
  // mailChimp();

});

$(document).ready(function() {
  $("#target").submit(function( event ) {
    var emailFormForm = $("#email").val();
    

      $.ajax({
        type:"GET",
        url: '/callback/forms/ajax_call/',
        data: {
         'email': emailFormForm
       },
       success: function(data) {
         if (data.is_there) {
           swal("Ya estás dentro", "El correo que ingresaste ya está en nuestra base de datos", "info");

         }
         else {
           swal("Bienvenida/o", "Tu correo quedó registrado para recibir nuestro boletín", "success");
         }
       },

      dataType: 'json',
      });


    event.preventDefault();
  });
});
