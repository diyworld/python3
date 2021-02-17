"""
    ref: https://www.runoob.com/python3/python3-json.html
    json.dumps(): 对数据进行编码
    json.loads(): 对数据进行解码
"""

import json

# Python 里的字典
dat = {
    'no': 1,
    'name': 'qingliu',
    'url': 'http://localhost:8081'
}

# 将字典数据转换为JSON字符串
jsonstr = json.dumps(dat)
print("Python字典数据:", repr(dat)) # repr()返回对象的string格式
print("转换为JSON对象:", jsonstr)

# 将JSON字符转换为字典
dat2 = json.loads(jsonstr)
print("type(dat2)=", type(dat2))
print("Python字典数据", repr(dat2))

# 将对象以JSON格式写入文件
with open(r"C:\ccx\workplace\python3\tmp\test-dat.json", "w") as f:
    json.dump(dat, f)

# 读取json存储格式的文件
with open(r"C:\ccx\workplace\python3\tmp\test-dat.json", "r") as f:
    dat3 = json.load(f)
    print("type(dat3)=", type(dat3))
    print("读文件JSON数据:", repr(dat3))
