
from socket import *
import time

COD = 'utf-8'
HOST = gethostname()
PORT = 9870
ADDR = (HOST, PORT)
CONNCNT = 10
BUFSIZ = 1024

s = socket(AF_INET, SOCK_STREAM)
# SO_REUSEADDR 重用端口号，表示socket被关闭或服务进程终止后协议栈马上释放该端口
# 正常情况下操作系统会保留几分钟该端口号
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(CONNCNT)
while True:
    print("Start the server and listen client to connect ...")
    conn, addr = s.accept() # 阻塞监听
    print("Comming client:", addr)
    while True:
        try:
            data = conn.recv(BUFSIZ)
        except Exception:
            # 连接断开
            print("The client break down:", addr)
            break
        if not data:
            break
        print("Recv from clent:", data.decode(COD))
        # 获取时间数据
        timedat = time.strftime("%Y-%m-%d %X")
        sendmsg = "[%s]:%s" % (timedat, data.decode(COD))
        conn.send(sendmsg.encode(COD))
    conn.close()
s.closel()

