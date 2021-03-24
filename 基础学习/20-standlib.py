
import os
# 当前工作目录
workpath = os.getcwd()
print(workpath)
# 修改当前工作目录
os.chdir(workpath + '\\tmp')
print(os.getcwd())
# 执行系统命令
os.system('cd ..')
os.chdir(workpath)
print(os.getcwd())
print()

# 文件的拷贝和移动
import shutil
#shutil.copyfile('xxx', 'yyy')
#shutil.move('xxx', 'yyy')

# 文件通配符
import glob
print(glob.glob('*.py'))
print()

# 正则匹配
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
print()

# 数学运算
import math
print(math.cos(math.pi / 4))
print(math.log(1024, 2))
print()

# 随机数
import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random()) # 0~1的随机数
print(random.randrange(6))

# 访问互联网
import urllib.request
# 打印互联网抓取的数据
for line in urllib.request.urlopen('https://www.baidu.com'):
    line = line.decode('utf-8')
    #if 'baidu' in line:
    print(line, end='')
print()
print()

# 日期和时间
import datetime
print(datetime.date.today())
print(datetime.date.today().strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
#print(time.time())
print()

# 数据压缩
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t1 = zlib.compress(s)
print(len(t1))
t2 = zlib.decompress(t1)
print(len(t2))

