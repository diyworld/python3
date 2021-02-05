# 变量类型
print("#####变量类型#####")
a, b, c, d = 20, 5.5, True, 4+3j
x, y = "hello", True
print(type(a), type(b), type(c), type(d))
print(type(x), type(y))

# 除法
print("#####除法#####")
a = 12.3
b = 3
print(a/b)
print(a//b)

# 字符串
print("#####字符串#####")
str1 = "hello python3"
print(str1)
print(str1[0:3])

# 列表
print("##### 列表: 有序的对象集合 #####")
list1 = ['k', 999]
list2 = ['a', 'b', 'abc', 1, 123.3, list1]
print(list1)
print(list2)
list2[5][1] = 1000
print(list2)
print(list2[0:5:2])

print("##### 字符串转列表 #####")
str0 = "hello python3 and I love you!"
list0 = str0.split(" ") # 以空格分割字符串形成列表
print(list0)

print("##### 元组Tuple: 与列表类似 #####")
tuple0 = ('abc',)
tuple1 = (1, 2.0, 'abc', tuple0)
print(tuple0)
print(tuple1)
print(tuple1[1:100])

print("##### 集合: 事物或对象的集合 #####")
site1 = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
a = set('1abc')
b = set('a123')
print(site1)   # 输出集合，重复的元素被自动去掉
print(a)
print(b)

print(a - b) # 差集
print(a | b) # 并集
print(a & b) # 交集
print(a ^ b) # 非交集

print("##### 字典: 无序的对象集合, key:value形式 #####")
a = {'abc':'123'}
a['one'] = 1
a[2] = 'two'
print(a)
print(a.keys())
print(a.values())

print("##### 数据类型转换 #####")
print(int(12.3))
print(float(10))
print(complex(1,2))
print({'one':1, 2:'two'}) # 将对象转换为适合阅读的字符串
print(repr({'one':1, 2:'two'})) #将对象转化为供解释器读取的形式
print(list('abc123'))
print(dict(a='a', b='b', t='t'))
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))
print(dict([('one', 1), ('two', 2), ('three', 3)]))
print(chr(98))
print(ord('a'))
print(hex(15))

