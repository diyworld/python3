"""
    selenium 测试项
    1）使用 selenium 打开 Chrome 浏览器
    2）浏览器加载本地 test4.html 文件
    3）调用执行一段外部的 JavaScript 程序 show_browser_info.js
    3.1）show_browser_info.js：搜集浏览器环境信息，cookie信息等显示在当前浏览器页面
    4）调用执行 load_url.js，传入豆瓣主页
    4.1）load_url.js：接收 url 参数，浏览器加载该 url 页面
    5）调用执行 script_keyinfo.js
    5.1）script_keyinfo.js：抓取主页热点信息，打印到 python 控制台
    6）调用执行 script_login.js
    6.1）script_login.js：设置用户名和密码，提交表单进行登录操作
    6.2）打印登录结果：成功或失败
    7）获取登录后的部分用户信息，打印到 python 控制台
    8）指定打开一部电影，进行自动评论提交
    9）手动验证是否提交成功
    10）退出浏览器
"""
import time
from selenium import webdriver

HTML_TEST4      = r"C:\ccx\workplace\python3\html\test4.html"
JS_BROWSER_INFO = r"C:\ccx\workplace\python3\javascript\show_browser_info.js"
PARAM_URL       = "https://www.douban.com/"
#PARAM_URL       = "https://www.baidu.com/"
JS_LOAD_URL     = r"C:\ccx\workplace\python3\javascript\load_url.js"
JS_GRUB_KINFO   = r"C:\ccx\workplace\python3\javascript\script_keyinfo.js"
JS_LOGIN_DOUBAN = r"C:\ccx\workplace\python3\javascript\script_login.js"
JS_OPRATE = r"C:\ccx\workplace\python3\javascript\script_oprate.js"

# 获取js文件内容
def get_js(js_path):
    f = open(js_path, 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


# 1）创建Chrome驱动器
driver = webdriver.Chrome()
# 2）打开本地文件
driver.get(HTML_TEST4)

# 3）执行js获取浏览器信息
operate_js = get_js(JS_BROWSER_INFO)
driver.execute_script(operate_js)

# 4）加载该豆瓣主页面
# 注: 不能使用 execjs 模块调用 js 文件的方法，这样调用的环境就没了
#import execjs
#status = execjs.compile(open(JS_LOAD_URL, encoding='utf-8').read()).call('LoadUrlHandle', PARAM_URL)
#print("Open url<" + PARAM_URL + "> status: " + status)
operate_js = get_js(JS_LOAD_URL)
#driver.get("缓存所在的url")
status = driver.execute_script(operate_js, PARAM_URL)
print("Open url<" + PARAM_URL + "> status: " + status)

# 5）抓取主页热点信息，打印到 python 控制台
operate_js = get_js(JS_GRUB_KINFO)
kinfo = driver.execute_script(operate_js)
print("Grub key info:\n" + kinfo)

# 6）登录
operate_js = get_js(JS_LOGIN_DOUBAN)
ifr_src = driver.execute_script(operate_js)
print("Login the douban: " + ifr_src + '\n')

# 等待登录完成
cmd = input("cmd: ")
while cmd != 'ok':
    cmd = input("cmd: ")
print("Login ok")

# 登录后操作
operate_js = get_js(JS_OPRATE)
opdata = driver.execute_script(operate_js)
print("opdata: " + opdata)
"""
# 定位到电影，点击提交
# 先定位到 id='anony-movie' and class='section'的 div数据块，然后逐级找到对应的链接标签
anony_movie = driver.find_element_by_xpath("//div[@id='anony-movie' and @class='section']")
movie = anony_movie.find_element_by_xpath("./div/div/h2/a")
movie.click()
time.sleep(3)
# 搜索正在热映的影片，并打印
screening_bd = driver.find_element_by_xpath("//div[@class='screening-bd']")
movie_li = screening_bd.find_element_by_xpath("./ul//li")
movie = movie_li
title = movie.get_attribute("data-title")
print(title)
#for movie in enumerate(movie_li):
#    title = movie.get_attribute("data-title")
#    print(title)
"""
# 退出
time.sleep(3)
cmd = input("cmd: ")
while cmd != 'exit':
    cmd = input("cmd: ")
print("Exit")
driver.quit()

