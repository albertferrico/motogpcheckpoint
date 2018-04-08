//document.querySelector(".site-menu-container").addEventListener("click",function(){
//	document.querySelector(".site-menu-container ul").classList.toggle("show")
//})
$(document).ready(function(){
	$(window).bind('scroll', function () {
    		if ($(window).scrollTop() > 50) {
        		$('.navbar').addClass('navbar-fixed-top');
    		} else {
        		$('.navbar').removeClass('navbar-fixed-top');
    		}
	});
	$('.contenedor-carta').css('cursor', 'pointer').on('click', function() {
		document.location = $(this).attr('data-url');
	});

	$('site-menu-container').on('click', function(){
		$('.site-menu-container ul').toggle('show');
	});
	var amountScrolled = 300;

	$(window).scroll(function() {
    		if ( $(window).scrollTop() > amountScrolled ) {
        		$('a.scrollToTop').fadeIn('slow');
    		} else {
        		$('a.scrollToTop').fadeOut('slow');
    		}
	});
	
	$('a.scrollToTop').click(function() {
    		$('html, body').animate({
        		scrollTop: 0
    		}, 700);
    		return false;
	});
});
