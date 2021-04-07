import os
import subprocess
import platform
import json
import debug

# 公共模块
class common:
    def __init__(self):
        self.dbg = debug.debug()
        self.dbg.printlog("info", platform.system() + ',', "version:" + platform.python_version())
    """ 读取文件内容 """
    def readfile(self, path, mode):
        # 按 json 格式读取, 返回字典
        if mode == 'json':
            try:
                fo = open(path, 'r')
                info = json.load(fo)
                fo.close()
                return info
            except:
                self.dbg.printlog("err", "read file {} in {} failed".format(path, mode))
                return {}
        # 按行格式读取, 返回列表
        elif mode == 'line':
            lines = []
            try:
                fo = open(path, 'r')
                for line in fo.readlines():
                    line = line.strip()
                    lines.append(line)
                fo.close()
                return lines
            except:
                self.dbg.printlog("err", "read file {} in {} failed".format(path, mode))
                return []
        # 一次性读取所有内容, 返回字符串
        elif mode == 'all':
            try:
                fo = open(path, 'r')
                info = fo.read()
                fo.close()
                return info
            except:
                self.dbg.printlog("err", "read file {} in {} failed".format(path, mode))
                return {}
    """ 写数据到文件 """
    def writefile(self, path, data):
        pass
    
    
    
    