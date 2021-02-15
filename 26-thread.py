"""
    线程简单实例
    使用_thread
"""
import _thread
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{threadName}: {time.ctime(time.time())}")

try:
    _thread.start_new_thread(print_time, ("Thread-1", 1))
except:
    print("Error: Start thread failed")

while True:
    pass #类似于执行空操作，什么也不发生，用于防止不允许空代码情况下发送错误