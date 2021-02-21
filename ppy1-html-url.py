'''
    利用正则表达式，抓取指定域名的html数据，保存到文件，提取出里面所有的url
'''
import urllib.request
import os
import re

g_url = 'http://www.baidu.com'
g_workpath = os.getcwd()
g_tmppath = g_workpath + '\\tmp\\'
# 文件路径, 文件名提取:主域名第一个主要字符串-baidu
# <(\w+)>匹配数字字符串，等价于([a-zA-Z0-9]+)
# <\.(\w+)\.>匹配第一个匹配到的两个.之间的字符串
htmlfile = g_tmppath + (re.findall(r'\.(\w+)\.', g_url))[0] + '.txt'

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

# 正则解析出所有匹配的 url
# http: 匹配字符<http>
# [\w/.?-]: 匹配一个字符，可以是字母或数字或特殊字符</.?->
# +: 匹配前面一个字符1次或多次
# *: 匹配前面一个字符0次或多次，这里<s*>表示至少匹配1次s
url_pattern = re.compile(r'https*://[\w/.?-]+')
find_url = url_pattern.findall(htmldata)

# 正则找出所有<a href>xxx</a>的url和关键字xxx
# <(https*://[\w/.?-]+)>匹配url
# [^>]+> 匹配非>字符直到碰到字符>
# ([^<]+)<+ 匹配<...>xxx<...>中间的xxx中文字符串
url2_pattern = re.compile(r"<a href=\"(https*://[\w/.?-]+)\" +[^>]+>([^<]+)<+")
find_url2 = url2_pattern.findall(htmldata)
print(find_url2)

'''
from urllib.parse import urlparse
result = urlparse(g_url)
print(result)
'''
# 写入文件
file = open(htmlfile, 'w')
file.write(htmldata) #写html数据
file.write('\n\n')
for i in range(len(find_url)):#追加url数据到文件尾部
    #print(find_url[i])
    file.write(find_url[i])
    file.write('\n')
file.write('\n\n')
for i in range(len(find_url2)):#追加url数据到文件尾部
    #print(find_url[i])
    file.write(find_url2[i][1])
    file.write(' ')
    file.write(find_url2[i][0])
    file.write('\n')
print(len(find_url))
file.close()
print(f"Saving the html-data to file \"{htmlfile}\"")

