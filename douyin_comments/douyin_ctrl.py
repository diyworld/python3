import os
import _thread
import subprocess
import platform
import json
import threading

import debug
import common
import time

class AdbCtrl:
    def __init__(self):
        pass
    def adb_run(self, cmd):
        """ 运行adb命令, 有输出则返回输出, 没有则返回空字符串 """
        return ""
    def adb_ui_dump(self):
        """ 获取UI控件信息 """
        cmd = "uiautomator dump /sdcard/tmp/ui.xml"
        self.adb_run(cmd)
    def adb_click(self, x, y):
        """ 点击 """
        pass
    def adb_dy_start(self):
        """ 启动抖音软件 """
        pass
    def adb_dy_stop(self):
        """ 关闭抖音软件 """
        pass
    def adb_input(self, msg):
        """ 输入文件信息 """
        pass
    def adb_slide(self, x1, y1, x2, y2):
        """ 滑动 """
        pass

