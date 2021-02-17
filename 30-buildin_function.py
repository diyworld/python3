"""
    Python3 内置函数
"""

# 绝对值 abs
print("<<<abs>>>")
x = abs(-1)
print("abs(-1) =", x)

# 元素完整性判断 all
print("<<<all>>>")
list1 = ['a', 'b', 'c', 'd']
list2 = ['a', 'b', '', 'd']
list3 = [0, 1, 2, 3]
print(all(list1))
print(all(list2))
print(all(list3))

# 元素存在性判断 any
print("<<<any>>>")
print(any(list1))
print(any(list2))
print(any(list3))

# bin
print("<<<bin>>>")
print(bin(10))

# bool
print("<<<bool>>>")
print(bool(0))
print(bool(9))
print(bool('a'))

# 检查一个对象是否可调用 callable
print("<<<callable>>>")
def add(a, b):
    return a + b
print(callable(0))
print(callable(add))

# chr 整数转换为字符
print("<<<chr>>>")
print(chr(0x30))
print(chr(97))

# compile() 函数
print("<<<compile>>>")
str = "for i in range(0,10): print(i, end='')"
c = compile(str,'','exec')
exec(c)
print()

# dict() 创建字典
print("<<<dict>>>")
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))
print(dict([('one', 1), ('two', 2), ('three', 3)]))

# dir() 获取当前模块属性
print("<<<dir>>>")
print(dir())

# eval() 执行一个表达式字符串
print("<<<eval>>>")
print(eval("3 * 7"))

# exec() 执行更复杂的代码
print("<<<exec>>>")
exec("""
for i in range(5):
    print(i, end='')
print()
""")

# format() 格式化函数
print("<<<format>>>")
print("{}-{}".format("hey", "July"))
print("{1}-{0}".format("hey", "July"))

# globals() 当前位置全部全局变量
print("<<<globals>>>")
print(globals())
# locals() 当前位置全部全局变量
print("<<<locals>>>")
print(locals())

# hash() 返回一个对象的hash值
print("<<<hash>>>")
print(hash("test"))

# hex() 整数转换为16进制数
print("<<<hex>>>")
print(hex(255))

# id() 获取对象内存地址
print("<<<id>>>")
a = 100
print(id(a))

# int() 字符串转整形数
print("<<<int>>>")
print(int('15'))
print(int('1010', 2))

# iter() 生成矢代器
print("<<<int>>>")
lst = [1, 2, 3]
for i in iter(lst):
    print(i, end='')
print()

# len() 返回对象长度
print("<<<len>>>")
print(len("abcdef"))

