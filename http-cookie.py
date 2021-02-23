import urllib.request
import os
import re

### Cookie实例 ###
if True:
    import urllib
    from http.cookiejar import FileCookieJar
    from http.cookiejar import MozillaCookieJar
    from http.cookiejar import LWPCookieJar
    cookie_file = r"C:\Ruijie\workplace\python3\tmp\urllib_cookie.txt"
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