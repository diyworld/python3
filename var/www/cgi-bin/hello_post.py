# CGI处理模块
import cgi, cgitb 

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
site_name = form.getvalue('name')
site_url  = form.getvalue('url')

if not site_name:
    site_name = "default-name"
if not site_url:
    site_url = "http://localhost:8081/cgi-bin/hello_post.py"
# http://localhost:8081/cgi-bin/hello_post.py?name=localhost&url=http://localhost:8081/cgi-bin/xxx
print ("Content-type:text/html")
print ()
print ("""<html>
<head>
<title>菜鸟教程 CGI 测试实例</title>
</head>
<body>
<h2>%s官网：%s</h2>
<p>POST方法表单发送数据测试: 
    <a href="http://localhost:8081/html/hello_post.html">
        点我进入测试连接
    </a>
</p>
</body>
</html>
""" % (site_name, site_url))

