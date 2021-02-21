import urllib.request
import json
import gzip
import io
from lxml import etree
from bs4 import BeautifulSoup

from http.cookiejar import FileCookieJar
from http.cookiejar import MozillaCookieJar
from http.cookiejar import LWPCookieJar

# 创建与libwww-perl Set-Cookie3文件兼容的FileCookieJar实例
cookie_file = r"C:\ccx\workplace\python3\tmp\cookie.txt"
cookie = LWPCookieJar(cookie_file)
cookie.load(cookie_file, ignore_discard=True, ignore_expires=True)
# 创建cookie处理器
cookie_handle = urllib.request.HTTPCookieProcessor(cookie)
# 构建opener
opener = urllib.request.build_opener(cookie_handle)

# 构建http请求
#url = "http://www.baidu.com/"
url = "https://accounts.douban.com/j/mobile/login/basic"  #登入链接
forms = {'name': '15060121576', 'password': '12345678'}           #http表单数据
postdata = urllib.parse.urlencode(forms).encode()                 #编码http表单数据
headers = {                                                       #http头
        "Accept": "text/html,application/xml",
        "Accept-Encoding": "gzip",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "accounts.douban.com",
        "Origin": "https://accounts.douban.com",
        "Referer": "https://accounts.douban.com/passport/login_popup?login_source=anony",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
request = urllib.request.Request(url, postdata, headers)  #组装成一个http请求实体

# 抓取首页 html
try:
    # 使用opener打开请求，这样可以自动保存cookie内容到 cookie变量
    response = opener.open(request)
    responsedata = response.read()
    # 打印响应http数据
    if response.code == 200:
        print("headers:", response.headers)
        print("url:", response.url)
        print("code:", response.code)
        print("msg:", response.msg)
        print("Content-Encoding:", response.info().get('Content-Encoding'))
        print("Content-Type:", response.info().get('Content-Type'))
        print(f"Response data: {len(responsedata)} bytes, type is {type(responsedata)}")

    # 解压数据，只支持gzip
    #f = gzip.GzipFile(fileobj=io.StringIO(responsedata))
    f = gzip.GzipFile(fileobj=io.BytesIO(responsedata))
    f_dat = str(f.read(), 'utf-8')
    print("Response data:", f_dat)
    # 转换为字典
    dict0 = json.loads(f_dat)
    print("status:", dict0['status'])
    print("touch_cap_url:", dict0['payload']['touch_cap_url'])
    # 保存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)
    # 第一步完成
    print("Step1 Ok")
except urllib.error.URLError as e:
    print("URLError reason:", e.reason)
except urllib.error.HTTPError as e:
    print("HTTPError reason:", e.reason)
    print("HTTPError code:", e.code)
    print("HTTPError headers:", e.headers)
    
# 保存文件
#file = open(r"C:\ccx\workplace\python3\tmp\douban.html", 'w')
#file.write(htmldata.decode('gbk', 'ignore'))
#file.close()

# 提取登入地址
#soup = BeautifulSoup(htmldata, features='html.parser')
# 直接获取 iframe的tag下的src属性，tag属性操作和字典相同
#login_url = soup.iframe['src']
#print(login_url)

