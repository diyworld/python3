"""
    基于 selenium.webdriver 操控Chrome浏览器搜索信息，并提取第一个标题信息
    注1：需要安装 selenium: pip install selenium
    注2：需要下载 chromedriver.exe（版本要与实际浏览器一致），放置到 python3安装根目录下
    注3：谷歌浏览器安装目录添加到环境变量 Path
    注4：selenium的性质是一个web测试工具，用于模拟人操作浏览器用的
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

