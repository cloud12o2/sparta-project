$(document).ready(function () {
    $("#reviews-box").html("");
    ajaxPost();
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
        url: "http://spartacodingclub.shop/post",
        data: {},
        success: function (response) {
            console.log(response);
            alert(response["msg"]);
        }
    })
}