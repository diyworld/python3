
#元组
"""
元组与列表类似，不同之处在于元组的元素不能修改，理解为枚举值。
元组使用小括号 ( )，列表使用方括号 [ ]。
"""

tup1 = (1,2,3,4,5)
print('1: ', tup1)
print('1: ', type(tup1))

tup2 = ('a', 'b')
tup3 = tup1 + tup2
print('2: ', tup3)
print('3: ', id(tup3)) #查看内存地址
del tup3
#print('3: ', tup3) #NameError: name 'tup3' is not defined
for x in (1,2,3):
    print('4: ', x)

