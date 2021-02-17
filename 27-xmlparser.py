"""
    使用 SAX解析xml文件
    SAX解析xml文档分为解析器和事件处理器两个部分
    C:\ccx\workplace\python3\tmp\movies.xml
"""

import xml.sax

# 定义SAX的事件处理器类
class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.ytpe = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""
    
    # 在元素开始时调用
    # 把标签记录在 CurrentData变量中
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title:", title)
    
    # 读取元素内容时调用
    # 把元素内容记录在对应的变量中
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content
    
    # 在元素结束时调用
    # 这时已经读取一个完整的元素标签，可以打印相应信息
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

# 如果本文件作为脚本被执行，则执行下面代码
# 如果本文件被其他python引用 import，则不会执行下面代码
if (__name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # 重写 ContexHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)
    #解析 movies.xml文件
    parser.parse(r"C:\ccx\workplace\python3\tmp\movies.xml")





