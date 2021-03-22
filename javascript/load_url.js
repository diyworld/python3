
/*
在 python 端用 execjs.compile() 直接调用该函数情况下，环境不是浏览器的环境;
所以必须将url参数传递到该脚本下, 使用 xxx.execute_script(...)指令直接执行
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

