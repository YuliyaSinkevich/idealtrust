$(document).ready(function () {
    $("#main-top-navbar").on("click", "a", function (event) {
        event.preventDefault();
        var id = $(this).attr('href'),
            top = $(id).offset().top;
        $('body,html').animate({scrollTop: top}, 500);
    });


window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        document.getElementById("main-top-navbar").style.borderTop = "0";
        } else {
        document.getElementById("main-top-navbar").style.borderTop = "50px solid #3d4f9b";
    }
}


var switcherButton = document.getElementById("switcherBut");
switcherButton.addEventListener("click", toggle, false);

function toggle() {
var switcher = document.getElementById("switcher");
var yandexMap = document.getElementById('yandexMap');

    if(switcherButton.style.cssText !== "float: right;") {
        yandexMap.style.cssText = "display: block;";
        switcherButton.style.cssText = "float: right;";
        switcher.style.cssText = "background-color: #cf6f27";
    } else {
        yandexMap.style.cssText = "display: none;";
        switcherButton.style.cssText = "float: left;";
        switcher.style.cssText = "background-color: #3d4f9b;";
    }
}

});





