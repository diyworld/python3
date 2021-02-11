import cgi, cgitb
import sys

# 获取浏览器通过url传递过来的参数
# http://localhost:8081/cgi-bin/hello_get.py?name=localhost&url=http://localhost:8081/cgi-bin/xxx
form = cgi.FieldStorage() 
site_name = form.getvalue('name')
site_url  = form.getvalue('url')

if not site_name:
    site_name = "default-name"
if not site_url:
    site_url = "http://localhost:8081/cgi-bin/hello_get.py"

htmldata = """
Content-type:text/html

<html>
<head>
<!--注释掉charset, 否则浏览器显示中文会乱码-->
<!--<meta charset="utf-8">-->
<title>菜鸟教程 CGI 测试实例</title>
</head>
<body>
<h2>%s本机CGI地址：%s</h2>
<p>GET方法表单发送数据测试: 
    <a href="http://localhost:8081/html/hello_get.html">
        点我进入测试连接
    </a>
</p>
</body>
</html>
""" % (site_name, site_url)

print(htmldata)
"""
# 写入到html文件
htmlfile = "D:\\workplace\\python3\\var\\www\html\\hello_get_s1.html"
file = open(htmlfile, 'w')
file.write(htmldata)
file.close()
"""
