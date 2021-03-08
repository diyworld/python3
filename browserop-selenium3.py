
"""
    基于 selenium.webdriver 操控Chrome浏览器搜索信息，并提取第一个标题信息
    注1：需要安装 selenium: pip install selenium
    注2：需要下载 chromedriver.exe（版本要与实际浏览器一致），放置到 python3安装根目录下
    注3：selenium的性质是一个web测试工具，用于模拟人操作浏览器用的
"""
import time
from selenium import webdriver

# 创建Chrome驱动器
driver = webdriver.Chrome()
# 打开网页
driver.get("https://www.douban.com/")
time.sleep(1)
# 定位到用户名标签，填写用户名
#username_tag = driver.find_element_by_xpath("//div[@id='anony-movie' and @class='section']")
iframe_tag = driver.find_element_by_xpath("//iframe[contains(@src,'//accounts.douban.com/passport/login_popup?login_source=anony')]")
print("iframe_tag, style = ", iframe_tag.get_attribute("style"))
driver.switch_to.frame(iframe_tag) #切换到iframe
'''
script_tag = driver.find_element_by_xpath("//script[@id='tmpl_account']")
print("script_tag, id = ", script_tag.get_attribute("id"))
username_tag = driver.find_element_by_xpath("//div[@class='account-form-raw'][2]/div/input")
'''
operate_js = "document.getElementById('tmpl_phone').innerHTML;"
operate_js_content = driver.execute_script(operate_js)
print('operate_js_content = ', operate_js_content)
#username_tag = driver.find_element_by_xpath("//input[@id='username' and @name='username']")
#username_tag = driver.find_elements_by_xpath("//script[@id='tmpl_account']")
#username_tag = driver.find_elements_by_xpath("//div[@class='account-tabcon-start']")
#print("username_tag, id = ", username_tag.get_attribute("id"))
#username_tag.send_keys("15060121576")
# 定位到密码标签，填写密码
'''
password_tag = driver.find_element_by_xpath("//script[@id='tmpl_account']/div[3]/div/input")
print("password = " + password_tag.get_attribute("password"))
password_tag.send_keys("1234567ba")
# 定位到提到标签，点击提交
submit_tag = driver.find_element_by_xpath("//script[@id='tmpl_account']/div[4]/a")
print("click = " + password_tag.get_attribute("href"))
submit_tag.click()
# 切换回主文档
driver.switch_to.default_content()
time.sleep(10)
'''
time.sleep(3)
driver.quit()

