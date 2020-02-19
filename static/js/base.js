;( function( $ ) {
  $('.swipebox').swipebox({
    hideBarsDelay : 0,
    loopAtEnd: true
  });
})( jQuery );

;$('.carousel').carousel({
  interval: 3000
});

;$(document).ready(function(){
  var link = window.location.pathname;
  $('a[href="'+link+'"]').addClass('active');
});