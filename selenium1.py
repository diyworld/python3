"""
    基于 selenium.webdriver 操控Chrome浏览器搜索信息，并提取第一个标题信息
    注1：需要安装 selenium: pip install selenium
    注2：需要下载 chromedriver.exe（版本要与实际浏览器一致），放置到 python3安装根目录下
    注3：selenium的性质是一个web测试工具，用于模拟人操作浏览器用的
"""
import time
from selenium import webdriver

keys = "lifeeeee"
# 创建Chrome驱动器
driver = webdriver.Chrome()
# 打开网页
driver.get("https://www.baidu.com/")
time.sleep(1)
# 定位到搜索栏，并在搜索栏输入关键字
inputElement = driver.find_element_by_name("wd")
inputElement.send_keys(keys)
# 定位到提交按钮，点击提交
su_find = driver.find_element_by_id('su')
su_find.click()
time.sleep(3)
# 搜索name为 description的标签
re_title = driver.find_element_by_name('')
print(re_title.get_attribute("content"))
# 退出
time.sleep(3)
driver.quit()

