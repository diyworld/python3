# ref: https://www.jianshu.com/p/cfbdacbeac6e
import urllib.request
import os
import re

if False:
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

### 基本请求实例 ###
if False:
    import urllib
    # 指定url, 
    url = "http://httpbin.org/post"
    # 构造请求头部, 
    headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
            'Host': 'httpbin.org'
    }
    # 构造post表单数据, 
    forms = {'word': 'hello'}
    postdata = urllib.parse.urlencode(forms).encode()
    # 构造请求实例
    req = urllib.request.Request(url, postdata, headers)
    # 发送请求
    try:
        response = urllib.request.urlopen(req, timeout = 5)
        print("Receive data:", response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Failed reason:", e.reason)

### Cookie实例 ###
if True:
    import urllib
    from http.cookiejar import FileCookieJar
    from http.cookiejar import MozillaCookieJar
    from http.cookiejar import LWPCookieJar
    cookie_file = r"C:\ccx\workplace\python3\tmp\urllib_cookie.txt"
    # 构造cookie实例
    # 创建FileCookieJar实例，检索cookie信息并将信息存储到文件中
    #cookie = FileCookieJar(cookie_file)
    # 创建与Mozilla cookies.txt文件兼容的FileCookieJar实例
    #cookie = MozillaCookieJar(cookie_file)
    # 创建与libwww-perl Set-Cookie3文件兼容的FileCookieJar实例
    cookie = LWPCookieJar(cookie_file)
    cookie.load(cookie_file, ignore_discard=True, ignore_expires=True)
    # 创建cookie处理器
    cookie_handle = urllib.request.HTTPCookieProcessor(cookie)
    # 构建opener
    opener = urllib.request.build_opener(cookie_handle)

    # 指定url
    url = "https://www.baidu.com/"
    # 构造请求头部
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Host': 'baidu.com'
    }
    # 构造post表单数据
    forms = {'word': 'hello'}
    postdata = urllib.parse.urlencode(forms).encode()
    # 构造请求实例
    req = urllib.request.Request(url, postdata, headers)
    # 发送请求
    try:
        response = opener.open(req, timeout = 5)
        cookie.save(ignore_discard=True, ignore_expires=True)
        if response.code == 200:
            print("headers:", response.headers)
            print("url:", response.url)
            print("msg:", response.msg)
            print("Receive data: %d bytes" % len(response.read().decode('utf-8')))
    except urllib.error.URLError as e:
        print("URLError reason:", e.reason)
    except urllib.error.HTTPError as e:
        print("HTTPError reason:", e.reason)
        print("HTTPError code:", e.code)
        print("HTTPError headers:", e.headers)
