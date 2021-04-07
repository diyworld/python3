
"""
    debug日志打印接口
"""
import inspect
import sys

# 日志打印类
class debug:
    def __init__(self):
        # 打印模式 ['full', 'class', 'func']
        self.mode = "class"
        # 打印标签列表
        self.tags = ['err', 'info', 'trace', 'tmp']
    # 打印日志信息
    # tag: 指定标签, 只有存在于 self.tags 的标签才会打印输出
    # *vartuple: 可变参数, 每个参数以空格分割
    def printlog(self, tag, *vartuple):
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
        print(s, end='')
        for ele in vartuple:
            print(ele, end=' ')
        print()
        return True
    # 新增标签, tags - 标签列表
    def addtags(self, tags):
        for tag in tags:
            if tag not in self.tags:
                self.tags.append(tag)
        return True
    # 删除标签, tags - 标签列表
    def deltags(self, tags):
        for tag in tags:
            if tag in self.tags:
                self.tags.remove(tag)
        return True
    # 显示当前标签列表
    def showtags(self):
        print("tags =", self.tags)
        return True

# 应用举例
if (__name__ == "__main__"):
    dbg = debug()
    dbg.printlog("tmp", "hello", 1, (1, 2), {'one':1, 'tow':2})
    dbg.showtags()
    dbg.addtags(['debug-err', 'debug-tmp'])
    dbg.showtags()
    dbg.printlog("debug-err", "test")
    dbg.printlog("debug-info", "test")
    dbg.deltags(['debug-err', 'debug-trace'])
    dbg.showtags()
