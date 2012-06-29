$(document).ready(function() {
    $("ul ul").hide();
    $("ul li").click(function(e)
    {
        $(this).children("ul").toggle();
        e.stopPropagation();
    });
});
