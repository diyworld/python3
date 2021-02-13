
import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9870
print(f"host = {host}, port = {port}")
serversocket.bind((host, port)) # 注意以元组的形似作为参数
serversocket.listen(5) # 最大监听数

while True:
    clientsocket, addr = serversocket.accept() # 阻塞监听
    print(f"接入地址: {str(addr)}")
    msg = 'welcome to my home' + '\r\n'
    clientsocket.send(msg.encode('utf-8')) # 发送数据
    clientsocket.close()
