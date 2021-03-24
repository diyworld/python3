# map 函数, 将给定对象里的每一个元素使用给定函数进行映射输出
# 返回一个矢代器对象, 使用 list 转换为列表

# 将给定序列里的元素平方
def square(x):
    return x * x
y = list(map(square, [1, 2, 3]))
print(*y[0:], sep=' ')