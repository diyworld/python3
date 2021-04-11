
"""
    debug日志打印接口
"""
import os
import sys
import time
import inspect
import threading

"""
文件同步操作
防止不同实例操作同一个目录下的文件
"""
g_thread_lock = threading.Lock()
def loadto_file(path, s):
    """ 将字符串写入文件 """
    ret = True
    filename = "debug-" + time.strftime("%Y-%m-%d", time.localtime()) + ".txt"
    fullpath = os.path.join(path, filename)
    g_thread_lock.acquire()
    try:
        fd = open(fullpath, "a")
        fd.write(s)
        fd.close()
    except:
        print("open and write failed")
        ret = False
    g_thread_lock.release()
    return ret

"""
日志打印类
"""
class debug:
    def __init__(self):
        # 打印模式 ['full', 'class', 'func']
        self.mode = "class"
        self.wflag = False
        # 打印标签列表
        self.tags = ['err', 'info', 'trace', 'tmp']
        # 日志存储标签
        self.storetags = ['err', 'info']
        self.path = ""
    def printlog(self, tag, *vartuple):
        """
        打印日志信息
        tag: 指定标签, 只有存在于 self.tags 的标签才会打印输出
        *vartuple: 可变参数, 每个参数以空格分割
        """
        if tag not in self.tags:
            return False
        s = '['
        if self.mode == 'full':
            # 模式 full, 打印全路径
            s = s + sys._getframe().f_code.co_filename
        elif self.mode == 'class':
            # 模式 class, 打印模块名
            s = s + getattr(sys.modules['__main__'], '__file__', None)
        elif self.mode == 'func':
            # 模式 func, 打印函数名
            s = s + inspect.stack()[1][3]
        s = s + '/'
        s = s + str(sys._getframe().f_back.f_lineno)
        s = s + '][' + tag + '] '
        # 输出到终端
        for ele in vartuple:
            #print(ele, end=' ')
            s = s + str(ele) + ' '
        s = s + '\n'
        print(s, end='')
        if self.wflag:
            # 存储到对应路径下
            if tag in self.storetags:
                if not loadto_file(self.path, s):
                    return False
        return True
    def addtags(self, tags):
        """ 新增标签, tags: 标签列表 """
        for tag in tags:
            if tag not in self.tags:
                self.tags.append(tag)
        return True
    def deltags(self, tags):
        """ 删除标签, tags: 标签列表 """
        for tag in tags:
            if tag in self.tags:
                self.tags.remove(tag)
        return True
    def showtags(self):
        """ 显示当前标签列表 """
        print("tags =", self.tags)
        print("storetags =", self.tags)
        return True
    def setpath(self, path):
        """ 设置日志存储路径 """
        if len(path) == 0:
            print("path is null")
            return False
        elif not os.path.exists(path):
            print("[setpath] path doesn't exist")
            return False
        elif os.path.isfile(path):
            print("param isn't a path but file")
            return False
        self.path = path
        self.wflag = True
        return True
    def clrpath(self):
        """ 清除日志存储路径 """
        self.wflag = False
        self.path = ""
        return True
    def addstoretags(self, storetags):
        """ 新增标签, storetags: 标签列表 """
        for tag in storetags:
            if tag not in self.storetags:
                self.storetags.append(tag)
        return True
    def delstoretags(self, storetags):
        """ 删除标签, storetags: 标签列表 """
        for tag in storetags:
            if tag in self.storetags:
                self.storetags.remove(tag)
        return True
        
# 应用举例
if (__name__ == "__main__"):
    # 普通打印测试
    dbg = debug()
    dbg.printlog("tmp", "hello", 1, (1, 2), {'one':1, 'tow':2})
    dbg.showtags()
    dbg.addtags(['debug-err', 'debug-tmp'])
    dbg.showtags()
    dbg.printlog("debug-err", "test")
    dbg.printlog("debug-info", "test")
    dbg.deltags(['debug-err', 'debug-trace'])
    dbg.showtags()
    # 日志存储测试
    dbg = debug.debug()
    dbg.printlog("info", "a good day")    # 为设置路径, 不会存储到文件
    dbg.setpath(r"C:\ccx\workplace\python3\tmp")
    dbg.printlog("info", "one two three") # 设置路径后, 会存储到文件
    dbg.printlog("trace", "1 2 3")        # trace标签, 默认不会存储到文件
