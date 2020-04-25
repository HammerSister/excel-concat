$("#file").on("change",function (e) {

    var e = e || window.event;  //获取 文件 个数 取消的时候使用
    var files = e.target.files;

    $("#names").empty()
    $("#choose").html("重新选择")
    $("input[type='submit']").css("display","block");

    if(files.length > 0){

        for (let i = 0; i < files.length; i++){
            var $input = $("<input type='text' id='file" + i + "' value='" + files[i].name + "' readonly>")
            $("#names").append($input)
        }

    }
});