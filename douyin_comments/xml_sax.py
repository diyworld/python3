"""
    使用 SAX解析xml文件
    输入：元素唯一属性标识字典，需要的属性列表
    输出：返回找到的属性字典，找不到返回空字典
"""
import re
import xml.sax
import debug
import sys

#print("[%s@%s]" % (__file__, sys._getframe().f_lineno) )

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
        self.tag = ""
        self.attrs = {}
        self.keys = [] #要查找的key列表
        self.result = []
    # 在元素开始时调用
    def startElement(self, tag, attrs):
        is_match = True
        # 匹配标签值
        if tag != self.tag:
            return
        # 匹配属性列表
        for k, v in self.attrs.items():
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
        find = {}
        for k in self.keys:
            if k in attrs:
                find.update({k:attrs[k]})
        if find:
            self.result.append(find)
    # 读取元素内容时调用
    def characters(self, content):
        pass
    # 在元素结束时调用
    def endElement(self, tag):
        pass

# 查找属性值
class xml_attrs_finder:
    def __init__(self):
        self.dbg = debug.Debug()
        self.parser = xml.sax.make_parser() # 创建一个 XMLReader
        self.parser.setFeature(xml.sax.handler.feature_namespaces, 0) # 关闭命名空间
        self.xmlsax = xml_sax_handler()
        self.parser.setContentHandler(self.xmlsax) # 重写 ContexHandler
    # 设置输入属性和输出属性
    def set_attrs(self, tag, attrs, keys):
        #self.dbg.printlog("tmp", "tag,attrs,keys =", tag, attrs, keys)
        self.xmlsax.tag = tag
        self.xmlsax.attrs = attrs.copy()
        self.xmlsax.keys = keys.copy()
        self.xmlsax.result = []
        #self.dbg.printlog("tmp", "tag,attrs,keys =", self.xmlsax.tag, self.xmlsax.attrs, self.xmlsax.keys)
    # 获取输出属性
    def get_finds(self):
        return self.xmlsax.result
    def find_attrs(self, xml_file_path, tag, attrs, keys):
        # xml_file_path: 文件路径
        # tag  : 标签名称, 为空表示不关心
        # attrs: 输入的标签属性, 字典
        # keys: 要查找的属性, 列表
        # return: [{k1:v1,k2:v2,...},{k3:v3},...]
        #         列表里的每个元素{}都是满足条件的行的目标键值对
        #         比如要找 k1, k2, k3的键值对，则会遍历每行，对满足条件的行，
        #         取出k1,k2,k3对应的键和值，组成一个字典，添加到列表里
        #self.dbg.printlog("tmp", "tag,attrs,keys =", tag, attrs, keys)
        if typeof(attrs) != 'dict' or typeof(keys) != 'list':
            print("param err")
            return []
        elif len(attrs) == 0 or len(keys) == 0:
            print("param is null")
            return []
        self.set_attrs(tag, attrs, keys)
        self.parser.parse(xml_file_path)
        return self.get_finds()
    def get_axis(self, xmlpath, tag_name, attrs):
        """
        根据参数获取页面对应点的坐标
        xmlpath: 文件路径
        tag_name: 标签名称
        attrs: 要匹配属性列表
        return: [[0,0,0,0], [0,0,2,2]] (result = [{'bounds':"[0,0][0,0]"}, {'bounds':"[0,0][2,2]"}])
        """
        keys = ["bounds"] #要查找的属性列表 
        result = self.find_attrs(xmlpath, tag_name, attrs, keys)
        axis_list = []
        for ele in result:
            axis = []
            try:
                tt = re.match("\[([0-9]+),([0-9]+)\]\[([0-9]+),([0-9]+)\]", ele["bounds"])
                axis.append(int(tt.group(1)))
                axis.append(int(tt.group(2)))
                axis.append(int(tt.group(3)))
                axis.append(int(tt.group(4)))
                axis_list.append(axis)
            except:
                self.dbg.printlog("warnning", "Add to bounds false")
        self.dbg.printlog("trace", axis_list)
        return axis_list

# 如果本文件作为脚本被执行，则执行下面代码
# 如果本文件被其他python引用 import，则不会执行下面代码
if (__name__ == "__main__"):
    xaf = xml_attrs_finder()
    tag = "node"
    attrs = {'resource-id':'com.ss.android.ugc.aweme:id/btw', 'index':'2'}
    xmlpath = r"C:\ccx\workplace\python3\douyin_comments\tmp\ui_xx.xml"
    result = xaf.get_axis(xmlpath, tag, attrs)
    print(result) #[[0, 0, 900, 1600], [1, 2, 900, 1600]]

