
/*
//在 python 端用 execjs.compile() 直接调用该函数情况下，环境不是浏览器的环境
function LoadUrlHandle(url) {
    var Sys = {};
    var userAgent = navigator.userAgent;
    //location.href = url;
    return "OK";
}
*/

//载入指定的地址
url = arguments[0];
location.href = url;

//返回给调用者
return "OK";

