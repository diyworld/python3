import os
import json
import threading
import random
import debug
import time

class AdbDyCtrl:
    def __init__(self):
        self.dbg = debug.Debug()
        self.adb_fullpath = r"C:\ccx\workplace\ADB\Minimal ADB and Fastboot\adb.exe"
        self.uixml = "/tmp/ui.xml"
        self.rand_xmax = 10
        self.rand_ymax = 10
        self.dy_packet = "com.ss.android.ugc.aweme"
        self.dy_activity = ".splash.SplashActivity"
    def adb_run(self, adb_cmd):
        """ 运行adb命令, 有输出则返回输出, 没有则返回空字符串 """
        cmd = self.adb_fullpath + " " + adb_cmd
        ret = os.popen(cmd)
        return ret.read()
    def adb_ui_dump(self):
        """ 获取UI控件信息 """
        cmd = "uiautomator dump " + self.uixml
        self.dbg.printlog("trace", cmd)
        self.adb_run(cmd)
    def adb_click(self, x, y):
        """ 点击 """
        xx = x + random.randint(x, x + self.rand_xmax)
        yy = y + random.randint(y, y + self.rand_xmax)
        cmd = "adb tap " + str(xx) + " " + str(yy)
        self.dbg.printlog("trace", cmd)
        self.adb_run(cmd)
    def adb_dy_start(self):
        """ 启动抖音软件 """
        cmd = "am start -n %s/%s" % (self.dy_packet, self.dy_activity)
        self.dbg.printlog("trace", cmd)
        self.adb_run(cmd)
    def adb_dy_stop(self):
        """ 关闭抖音软件 """
        cmd = "am force-stop %s" % (self.dy_packet)
        self.dbg.printlog("trace", cmd)
        self.adb_run(cmd)
    def adb_input(self, msg):
        """ 输入文件信息 """
        cmd = "input text %s" % (msg)
        self.dbg.printlog("trace", cmd)
        self.adb_run(cmd)
        pass
    def adb_slide(self, x1, y1, x2, y2):
        """ 滑动 """
        pass

adbpath = r"C:\ccx\workplace\ADB\Minimal ADB and Fastboot\adb.exe"


