from lxml import etree
from bs4 import BeautifulSoup

filepath = r"C:\ccx\workplace\python3\tmp\xpath_ex.html"

# 打开文件，使用html.parser解析器解析
soup = BeautifulSoup(open(filepath, 'r', encoding='utf-8'), features='html.parser')
print(soup.title) # 抽取标题
print(soup.a) # 抽取链接a元素
print(soup.p) # 抽取标签p元素
print(soup.div['class'])
print(soup.div.attrs)
print()
print(soup.head.contents) # 抽取标签head的子节点，列表形式输出
print()
# 抽取子节点并打印
for child in soup.head.children:
    print(child, end='')
print()

# 全文搜索
print("<<<find_all>>>")
print(soup.find_all(text = 'hahaha'))
# 选择器
print("<<<select>>>")
print(soup.select("title")) # 通过标记名title查找元素
print(soup.select(".hahaha")) # 通过标签的class属性查找



