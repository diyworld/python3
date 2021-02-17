"""
    基于 perf_counter进度条实例
"""
import time

scale = 100

# center() 控制输出居中
# 宽度为 scale//2 = 25
# 字符居中，两边填充 '-'
line1 = "Start"
print(line1.center(scale//2, "-"))

# 获取一个初始时间点
start = time.perf_counter()

#
for k in range(scale+1):
    # k个'*'字符
    a = '*' * k
    # (scale-k)个'.'字符
    b = '.' * (scale-k)
    # 当前进度百分比
    percent = (k/scale) * 100
    # 用时时间
    dur = time.perf_counter() - start
    # 打印输出进度条
    # \r 光标回到行首
    # {:^3.0f} 居中输出，占3位，小数点后0位，浮点数，对应输出变量为percent
    # 后面两个{}分别对应 a和 b字符串
    # {:.2f}s 输出有两位小数的浮点数，单位s
    formatbar = "\r{:^3.0f}%[{}->{}]{:.2f}s"
    print(formatbar.format(percent, a, b, dur), end='')
    # 延迟0.1s
    time.sleep(0.03)

line2 = "\r" + "100 %" + "[" + "*" * k + "]"
print(line2)
line3 = "End"
print(line3.center(scale//2, '-'))
