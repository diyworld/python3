
"""
参考链接：https://www.cnblogs.com/richered/p/11707915.html
1）启动CGI服务器（系统命令）
2）启动CGI：python -m http.server 8081
3）打开浏览器，输入网址
http://localhost:8081/cgi-bin/hello_get.py
"""

import os

workpath = "D:\\workplace\\python3"
path = workpath + "\\var\\www"
print(path)
os.chdir(path)
os.system('python -m http.server 8081')
os.chdir(workpath)


