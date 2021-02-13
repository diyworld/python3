
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9870
print(f"host = {host}, port = {port}")
s.connect((host, port))
msg = s.recv(1024) # 阻塞接收
s.close()
print(msg.decode('utf-8'))