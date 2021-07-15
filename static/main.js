$(document).ready(function () {
    $("#reviews-box").html("");
    showReview();
});

function ajaxPost() {
    $.ajax({
        type: "POST",
        url: "/review",
        data: {sample_give: '샘플데이터'},
        success: function (response) {
            alert(response["msg"]);
            window.location.reload();
        }
    })
}

function ajaxGet() {
    $.ajax({
        type: "GET",
        url: "/review?sample_give=샘플데이터",
        data: {},
        success: function (response) {
            alert(response["msg"]);
        }
    })
}