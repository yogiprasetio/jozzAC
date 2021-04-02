//event pada saat di klik

$('.nav-link , .navbar-brand').click(function(v) {
    //ambil isi href
    var href = $(this).attr('href');

    //tangkap element
    var elementHref = $(href);
    //var mina = elementHref.offset().top;
    //console.log($('body').scrollTop());

    //pindahkan scroll
    $('html, body').animate({ scrollTop: elementHref.offset().top - 50 }, 1500);

    v.preventDefault();
});