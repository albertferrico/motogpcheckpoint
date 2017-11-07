//document.querySelector(".site-menu-container").addEventListener("click",function(){
//	document.querySelector(".site-menu-container ul").classList.toggle("show")
//})
$(document).ready(function(){
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
