"""
    基于 threading创建子类 myThread
"""
import threading
import time

# 创建线程类，继承threading.Thread
class myThread(threading.Thread):
    # 定义构造函数
    def __init__(self, threadID, name, sleepSec):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.sleepSec = sleepSec
    # 定义一个运行方法run
    def run(self):
        print("开始线程: " + self.name)
        cnt = 5
        while cnt > 0:
            time.sleep(self.sleepSec)
            print(f"{self.name}: {time.ctime(time.time())}")
            cnt -= 1
        print("退出线程: " + self.name)

# 创建两个线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 启动线程
thread1.start()
thread2.start()

# 使用join方法等待线程结束
thread1.join()
thread2.join()

print("退出主线程")
