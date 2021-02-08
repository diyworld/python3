# ref: https://www.jianshu.com/p/cfbdacbeac6e
import urllib.request
import os
import re

g_url = 'http://www.baidu.com'
g_workpath = os.getcwd()
g_tmppath = g_workpath + '\\tmp\\'
htmlfile = g_tmppath + 'test.html'

# 抓取的数据
'''
htmldata = ''
for line in urllib.request.urlopen(g_url):
    line = line.decode('utf-8')
    htmldata += line
'''

# 抓取 html数据
request = urllib.request.Request(g_url)
response = urllib.request.urlopen(request)
htmldata = response.read().decode('utf-8')
print("Having get the html-data.")

# 写入文件
'''
file = open(htmlfile, 'w')
file.write(htmldata)
file.close()
print(f"Saving the html-data to file \"{htmlfile}\"")
'''

# 正则解析出所有匹配的 url
# http: 匹配字符<http>
# [\w/.?-]: 匹配一个字符，可以是字母或数字或特殊字符</.?->
# +: 匹配前面一个字符1次或多次
# *: 匹配前面一个字符0次或多次，这里<s*>表示至少匹配1次s
url_pattern = re.compile(r'https*://[\w/.?-]+')
find_url = url_pattern.findall(htmldata)
for i in range(len(find_url)):
    print(find_url[i])
print(len(find_url))
'''
from urllib.parse import urlparse
result = urlparse(g_url)
print(result)
'''
