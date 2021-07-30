const slideContents = document.querySelectorAll('.movie-rank_list'); // each slide dom
const slideLen = slideContents.length; // slide length
const slideWidth = 1575; // slide width
const slideSpeed = 300;// slide speed

// Box Office
const boxOfficeList = document.getElementById('jsBoxOfficeList'); // Slide parent dom
let boxOfficeCurIndex = 0; // current slide index (except copied slide)
const boxOfficePrevBtn = document.getElementById('jsBoxOfficePrevBtn'); // next button
const boxOfficeNextBtn = document.getElementById('jsBoxOfficeNextBtn'); // prev button


// Watcha
const watchaList = document.getElementById('jsWatchaList');
let watchaCurIndex = 0;
const watchaPrevBtn = document.getElementById('jsWatchaPrevBtn'); // next button
const watchaNextBtn = document.getElementById('jsWatchaNextBtn'); // prev button


// Netflix
const netflixList = document.getElementById('jsNetflixList');
let netflixCurIndex = 0;
const netflixPrevBtn = document.getElementById('jsNetflixPrevBtn'); // next button
const netflixNextBtn = document.getElementById('jsNetflixNextBtn'); // prev button



function boxOfficeNextBtnClick() {

    if (boxOfficeCurIndex == 0) {
        boxOfficeList.style.width = slideWidth * (slideLen) + "px";
        boxOfficeList.style.transition = slideSpeed + "ms";
        boxOfficeList.style.transform = "translate3d(-" + (slideWidth * (boxOfficeCurIndex + 1)) + "px, 0px, 0px)";
    }
    boxOfficeCurIndex = 1;
}

function boxOfficePrevBtnClick() {
    boxOfficeList.style.transform = "translate3d(0px, 0px, 0px)";
    boxOfficeCurIndex = 0;
}


function watchaNextBtnClick() {

    if (watchaCurIndex == 0) {
        watchaList.style.width = slideWidth * (slideLen) + "px";
        watchaList.style.transition = slideSpeed + "ms";
        watchaList.style.transform = "translate3d(-" + (slideWidth * (watchaCurIndex + 1)) + "px, 0px, 0px)";
    }
    watchaCurIndex = 1;
}

function watchaPrevBtnClick() {
    watchaList.style.transform = "translate3d(0px, 0px, 0px)";
    watchaCurIndex = 0;
}


function netflixNextBtnClick() {

    if (netflixCurIndex == 0) {
        netflixList.style.width = slideWidth * (slideLen) + "px";
        netflixList.style.transition = slideSpeed + "ms";
        netflixList.style.transform = "translate3d(-" + (slideWidth * (netflixCurIndex + 1)) + "px, 0px, 0px)";
    }
    netflixCurIndex = 1;
}

function netflixPrevBtnClick() {
    netflixList.style.transform = "translate3d(0px, 0px, 0px)";
    netflixCurIndex = 0;
}

function init() {
    boxOfficeNextBtn.addEventListener('click', boxOfficeNextBtnClick);
    boxOfficePrevBtn.addEventListener('click', boxOfficePrevBtnClick);

    watchaNextBtn.addEventListener('click', watchaNextBtnClick);
    watchaPrevBtn.addEventListener('click', watchaPrevBtnClick);

    netflixNextBtn.addEventListener('click', netflixNextBtnClick);
    netflixPrevBtn.addEventListener('click', netflixPrevBtnClick);
}

if (boxOfficeList) {
    init();
}
