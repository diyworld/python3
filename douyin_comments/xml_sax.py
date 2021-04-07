"""
    使用 SAX解析xml文件
    输入：元素唯一属性标识字典，需要的属性列表
    输出：返回找到的属性字典，找不到返回空字典
"""

import xml.sax

#print("[%s@%s]" % (__file__, sys._getframe().f_lineno) )

g_tag = ""
g_attrs = {}
g_finds = {}
# 设置输入属性和输出属性
def set_attrs(tag, attrs, finds):
    global g_tag, g_attrs, g_finds
    g_tag = tag
    g_attrs = attrs.copy()
    g_finds = finds.copy()
# 获取输出属性
def get_finds():
    global g_tag, g_attrs, g_finds
    return g_finds

#获取变量类型
def typeof(variate):
    type=None
    if isinstance(variate,int):
        type = "int"
    elif isinstance(variate,str):
        type = "str"
    elif isinstance(variate,float):
        type = "float"
    elif isinstance(variate,list):
        type = "list"
    elif isinstance(variate,tuple):
        type = "tuple"
    elif isinstance(variate,dict):
        type = "dict"
    elif isinstance(variate,set):
        type = "set"
    return type

# 定义SAX的事件处理器类
class xml_sax_handler(xml.sax.ContentHandler):
    def __init__(self):
        pass
    # 在元素开始时调用
    def startElement(self, tag, attrs):
        global g_tag, g_attrs, g_finds
        is_match = True
        # 匹配标签值
        if tag != g_tag:
            return
        # 匹配属性列表
        for k, v in g_attrs.items():
            if k not in attrs:
                is_match = False
                break
            if v != attrs[k]:
                is_match = False
                break
        # 不匹配退出
        if is_match != True:
            return
        # 搜集目标属性值
        for k, v in g_finds.items():
            if k in attrs:
                g_finds[k] = attrs[k]
    # 读取元素内容时调用
    def characters(self, content):
        pass
    # 在元素结束时调用
    def endElement(self, tag):
        pass

# 查找属性值
class xml_attrs_finder():
    def __init__(self):
        self.parser = xml.sax.make_parser() # 创建一个 XMLReader
        self.parser.setFeature(xml.sax.handler.feature_namespaces, 0) # 关闭命名空间
        self.parser.setContentHandler(xml_sax_handler()) # 重写 ContexHandler
    # xml_file_path: 文件路径
    # tag  : 标签名称, 为空表示不关心
    # attrs: 输入的标签属性, 字典
    # finds: 要查找的属性, 列表
    def find_attrs(self, xml_file_path, tag, attrs, finds):
        if typeof(attrs) != 'dict' or typeof(finds) != 'dict':
            print("param is not dict")
            return {}
        elif len(attrs) == 0 or len(finds) == 0:
            print("param is null")
            return {}
        set_attrs(tag, attrs, finds)
        self.parser.parse(xml_file_path)
        return get_finds()

# 如果本文件作为脚本被执行，则执行下面代码
# 如果本文件被其他python引用 import，则不会执行下面代码
if (__name__ == "__main__"):
    xaf = xml_attrs_finder()
    tag = "movie"
    attrs = {'title':'Trigun'}
    finds = {'bounds':''}
    file = r"C:\Ruijie\workplace\python3\tmp\movies.xml"
    set_attrs(tag, attrs, finds)
    print(xaf.find_attrs(file, tag, attrs, finds))

