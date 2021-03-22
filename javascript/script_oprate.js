
var str;
var info = "";

str = document.cookie;
info = info + "\ncookie: ";
info = info + str;

str = document.getElementById('db-global-nav').innerHTML;
info = info + "\ndb-global-nav: "
info = info + str;

return info