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
  if(link.startsWith('/press/'))
    $('a[href="/press/"]').addClass('active');
  if(link.startsWith('/about/'))
    $('a[href="/about/"]').addClass('active');
});

// ;$(document).ready(function(){
//   let video = document.getElementsByTagName('video')[0];
//   video.setAttribute("muted", "true")
// });
