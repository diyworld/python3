"""
    selenium 测试项
    1）使用 selenium 打开 Chrome 浏览器
    2）浏览器加载本地 html 文件
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
"""
import time
from selenium import webdriver

# 创建Chrome驱动器
driver = webdriver.Chrome()
# 打开网页
driver.get("https://www.douban.com/")
time.sleep(1)
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
# 退出
time.sleep(3)
driver.quit()

