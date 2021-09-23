$('#tab-posts').addClass('active-tab');
$('#section-friends').hide();
$('#tab-posts').click(function () {
    $('#tab-friends').removeClass('active-tab');
    $('#section-about').hide();
    $('#section-posts').show();
});
$('#tab-friends').click(function () {
    $(this).addClass('active-tab');
    $('#tab-posts').removeClass('active-tab');
    $('#section-posts').hide();
    $('#section-about').show();
});