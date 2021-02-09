"""
启动cgi, 在cmd命令下对应目录执行:
C:\ccx\workplace\python3\var\www>python -m http.server --cgi 808
"""

"""
# 一个简单的html
print ("Content-type:text/html")
print ()                             # 空行，告诉服务器结束头部
print ('<html>')
print ('<head>')
print ('<meta charset="utf-8">')
print ('<title>First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello Word! CGI Program is grate!</h2>')
print ('</body>')
print ('</html>')
"""

# 获取环境变量并发送给客户端
import os

print ("Content-type: text/html")
print ()
print ("<meta charset=\"utf-8\">")
print ("<b>Environment</b><br>")
print ("<ul>")
for key in os.environ.keys():
    print ("<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key]))
print ("</ul>")
