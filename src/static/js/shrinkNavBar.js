function scrollFunction() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {

        topWrap.style.display = "flex";
        topWrap.style.justifyContent = "center";
        navBar.style.height = "11vh";
        logoImg.style.width = "9vw";

    } else {
        navBar.style.height = "19.5vh";
        topWrap.style.display = "block";
        logoImg.style.width = "11vw";
    }
}

function init() {
    // When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
    window.onscroll = function() {scrollFunction()};

    topWrap = document.getElementById("jsTopWrap");
    navBar = document.getElementById("jsNavBar");
    logoImg = document.getElementById("jsLogoImg");
}

init()