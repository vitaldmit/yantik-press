;( function( $ ) {
  $('.swipebox').swipebox({
    hideBarsDelay : 0,
    loopAtEnd: true
  });
})( jQuery );

// Карусель для первого поста на главной
;$('.carousel').carousel({
  interval: 3000
});

// Подсветка меню
;$(document).ready(function(){
  var link = window.location.pathname;
  $('a[href="'+link+'"]').addClass('active');
  if(link.startsWith('/news/'))
    $('a[href="/news/"]').addClass('active');
});