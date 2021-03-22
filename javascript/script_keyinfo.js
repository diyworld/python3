
var kinfo = "";

//获取热映列表数组
var hotMoviesNodeList = document.getElementById("anony-movie").getElementsByClassName("main")[0].getElementsByClassName("movie-list list")[0].getElementsByTagName("li");
//遍历提取数据
for (i = 0, tlen = hotMoviesNodeList.length; i < tlen; i++) {
    var cnode = hotMoviesNodeList[i];
    var title = cnode.getElementsByClassName("title")[0].innerText;
    var tlink = cnode.getElementsByClassName("title")[0].childNodes[1];
    kinfo = kinfo + "    " + title + "," + tlink + ';\n';
}
return kinfo;
