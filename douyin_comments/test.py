import os
import _thread
import subprocess
import platform
import json
import threading

import debug
import common
import time

# 为线程定义一个函数
def print_time( threadName, delay):
   dbg = debug.debug()
   dbg.setpath(r"C:\ccx\workplace\python3\tmp")
   count = 0
   while count < 100:
       dbg.printlog("info", threadName + "haahhahahahhaha")
       count += 1

# 创建两个线程
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")


