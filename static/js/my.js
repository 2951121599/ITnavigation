function getFocus($obj) {
    //找到所有添加了focus样别的元素
    $(".focus").each(function (i, e) {
        //将e转换成jq对象
        $(e).removeClass('focus');
    });
    //添加需要获取焦点的样式
    $obj.addClass("focus");
}