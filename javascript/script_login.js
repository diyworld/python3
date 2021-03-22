/**
 * 方案一：定位到登录的标签，把用户名和密码更新到标签的 value 域，然后提交
 *         定位方法1：window.frames[0].document.getElementById("username")
 *         定位方法2：window.location = document.getElementsByTagName("iframe")[0].src;
 * 方案二：搜集页面信息和相关加密信息，返回给外部 python ，然后在外部构造http报文直接提交
 * 方案三：创建一个 form 提交
 */

var user_name = '15060121576';
var pass_word = '1234567ba';

//定位到 iframe 页面
var ifr_src = document.getElementsByTagName("iframe")[0].src;
window.location = ifr_src;
//填充数据，注：需要等待页面加载完成运行
//document.getElementById("username").value = user_name;
//document.getElementById("password").value = pass_word;

return ifr_src
/*
//获取 iframe 相关属性
var ifr_name = document.getElementsByTagName("iframe")[0].name;
var ifr_src = document.getElementsByTagName("iframe")[0].src;
//获取 iframe 子页面 id=username 的元素
var ifr_id_username = window.frames[0].document.getElementById("username");
*/