
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
<<<<<<< HEAD
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

