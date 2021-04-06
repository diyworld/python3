"""
    使用 SAX解析xml文件
    SAX解析xml文档分为解析器和事件处理器两个部分
    C:\ccx\workplace\python3\tmp\movies.xml
"""

import xml.sax



# 定义SAX的事件处理器类
class bounders_handler(xml.sax.ContentHandler):
    def __init__(self):
        self.comment_bounder = "" #评论坐标
    
    # 在元素开始时调用
    # 把标签记录在 CurrentData变量中
    def startElement(self, tag, attributes):
        if tag == "node":
            tagid = None
            content = None
            bounds = None
            if 'resource-id' in attributes:
                tagid = attributes['resource-id']
            if 'content-desc' in attributes:
                content = attributes['content-desc']
            if 'bounds' in attributes:
                bounds = attributes['bounds']
            if tagid and content and bounds:
                print("id, text, dounds =", tagid, content, bounds)
            if bounds and tagid == "com.ss.android.ugc.aweme:id/b98":
                print("bounds =", bounds)
    # 读取元素内容时调用
    # 把元素内容记录在对应的变量中
    def characters(self, content):
        pass
    
    # 在元素结束时调用
    # 这时已经读取一个完整的元素标签，可以打印相应信息
    def endElement(self, tag):
        pass

# 如果本文件作为脚本被执行，则执行下面代码
# 如果本文件被其他python引用 import，则不会执行下面代码
if (__name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # 重写 ContexHandler
    parser.setContentHandler(bounders_handler())
    #解析 movies.xml文件
    parser.parse(r"C:\ccx\workplace\python3\tmp\ui0.xml")

