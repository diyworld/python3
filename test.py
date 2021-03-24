
# lambda 匿名函数
IEEE1905_RSSI_TO_RCPI = lambda rssi: (2 * ((rssi) + 110))
IEEE1905_RCPI_TO_RSSI = lambda rcpi: (((rcpi) / 2) - 110)
print("rssi = -22  -> rcpi = ", IEEE1905_RSSI_TO_RCPI(-22))
print("rcpi = -176 -> rssi = ", IEEE1905_RCPI_TO_RSSI(176))

STRING_CMP = lambda str1, str2: True if (str1 == str2) else False
print(STRING_CMP("abcd", "abcd"))
print(STRING_CMP("abcd", "abcd1"))
print(STRING_CMP("abcd", "abce"))

# map 函数, 将给定对象里的每一个元素使用给定函数进行映射输出
# 返回一个矢代器对象, 使用 list 转换为列表
def square(x):
    return x * x
y = list(map(square, [1, 2, 3]))
print(*y[0:], sep=' ')

# filter 函数, 过滤不符合条件的元素
# 返回一个矢代器对象, 使用 list 转换为列表
def is_odd(n):
    return True if(n%2 == 0) else False
list0 = [1,2,3,4,5,6,7,8,9,0]
list1 = list(filter(is_odd, list0))
print(list1)

