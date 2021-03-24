"""
    使用 DOM解析xml文件
    一个 DOM 的解析器在解析一个 XML 文档时，一次性读取整个文档，
    把文档中所有元素保存在内存中的一个树结构里，之后你可以利用DOM
    提供的不同的函数来读取或修改文档的内容和结构，也可以把修改过的
    内容写入xml文件
    C:\ccx\workplace\python3\tmp\movies.xml
"""

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用 minidom解析器打开 XML文档
DOMTree = xml.dom.minidom.parse(r"C:\ccx\workplace\python3\tmp\movies.xml")
# 获取XML文档内部所有元素
collection = DOMTree.documentElement
# 检查文档是否存在 shelf标签
if collection.hasAttribute("shelf"):
    print(f"Root element: {collection.getAttribute('shelf')}")

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影详细信息
for movie in movies:
    print("*****Movie*****")
    if movie.hasAttribute("title"):
        print(f"Title: {movie.getAttribute('title')}")
    type0 = movie.getElementsByTagName('type')[0]
    format0 = movie.getElementsByTagName('format')[0]
    rating0 = movie.getElementsByTagName('rating')[0]
    description0 = movie.getElementsByTagName('description')[0]
    print(f"Type: {type0.childNodes[0].data}")
    print(f"Format: {format0.childNodes[0].data}")
    print(f"Rating: {rating0.childNodes[0].data}")
    print(f"Description: {description0.childNodes[0].data}")

print(type(type0))
print(type(type0.childNodes))
print(type(type0.childNodes[0].data))

