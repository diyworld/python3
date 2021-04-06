
var tag = document.getElementById("content").getElementsByClassName("title")[0];
var url = tag.childNodes[1].getAttribute("href");
window.location = url;

return "ok";