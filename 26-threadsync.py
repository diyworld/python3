"""
    线程数据访问同步锁机制与优先级队列
    queue.Queue(...)
    queueLock.acquire()
    queueLock.release()
    
"""
import queue
import threading
import time

gExitFlag = False # 退出标志位
queueLock = threading.Lock()
workQueue = queue.Queue(10)

class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("开启线程: " + self.name)
        while not gExitFlag:
            queueLock.acquire() #获取锁
            if not workQueue.empty():
                data = self.q.get()
                queueLock.release() #释放锁
                print(f"{self.name} processing {data}")
            else:
                queueLock.release() #释放锁
            time.sleep(1)
        print("退出线程: " + self.name)

nameList = ["Thread-1", "Thread-2", "Thread-3"] #线程名
dataList = ["One", "Two", "Three", "Four", "Five"] #数据列表
threads = [] #记录线程的列表
threadID = 1

# 创建线程
for tName in nameList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 队列填充数据
queueLock.acquire()
for word in dataList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程退出
gExitFlag = True

# 等待线程退出
for t in threads:
    t.join()
print("退出主线程")
