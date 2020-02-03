(function($) {var $window = $(window),
    $body = $('body');
    breakpoints({
        wide: [ '1281px', '1680px' ],
        normal: [ '1081px', '1280px' ],
        narrow: [ '961px', '1080px' ],
        narrower: [ '737px', '960px' ],
        mobile: [ null, '736px' ]});
    $window.on('load', function() {window.setTimeout(function() 
        {$body.removeClass('is-preload');}, 100);});
        $('#nav > ul').dropotron({offsetY: -14,noOpenerFade: true});
        $('<div id="titleBar">' +'<a href="#navPanel" class="toggle"></a>' +'</div>').appendTo($body);
        $('<div id="navPanel">' +'<nav>' +$('#nav')
        .navList() +'</nav>' +'</div>')
        .appendTo($body)
        .panel({
            delay: 500,
            hideOnClick: true,
            hideOnSwipe: true,
            resetScroll: true,
            resetForms: true,
            side: 'left',
            target: $body,
            visibleClass: 'navPanel-visible'});
        })
        (jQuery);


//Get the button
var mybutton = document.getElementById("scroll-to-top");

// When the user scrolls down 350px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 450 || document.documentElement.scrollTop > 450) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

