
#字典
dict0 = {1:'one', 2:'two', 3:'three'}
print('1: ', dict0)
print('\n')

#修改字典
dict0[1] = 'oneone'
dict0['0']= 'zero'
dict0[0] = 'zero'
print('2: ', dict0)
print('\n')

#删除字典
dict1 = dict0.copy()
print('2: ', dict1)
del dict1['0']
print('2: ', dict1)
dict1.clear()
print('2: ', dict1)
del dict1

#内置函数
dict2 = dict0.copy()
print('3: ', len(dict2))
print('3: ', str(dict2))
print('3: ', type(dict2))

#内置方法
#浅复制与删除
dict1 = dict0.copy()
print('4: ', dict1)
dict1.clear()
print('4: ', dict1)

#创建字典
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq, 'None')
print ('5: ', f"新的字典为: {dict}")

#获取或设置指定键的值，如果不存在则返回或填充指定的默认值
dict1 = {1:'one', 2:'two', 3:'three'}
print('6: ', dict1.get(1, 'None'))
print('6: ', dict1.get(0, 'None'))
dict1.setdefault(1, 'onee')
dict1.setdefault(0, 'zero')
print('6: ', dict1)

#分解字典为: 列表 + 元组
dict1 = {1:'one', 2:'two', 3:'three'}
print('7: ', dict1)
print('7: ', dict1.items())

#字典更新
dict1 = {1:'one', 2:'two', 3:'three'}
dict2 = {1:'onee', 2:'twoo', 0:'zeroo'}
print('8: ', dict1)
dict1.update(dict2)
print('8: ', dict1)

#获取字典里的所有值
dict1 = {1:'one', 2:'two', 3:'three'}
print('9: ', list(dict1.values()))

#删除指定健值对
dict1 = {1:'one', 2:'two', 3:'three'}
print('10: ', dict1)
dict1.pop(1)
print('10: ', dict1)

"""
radiansdict.clear()     删除字典内所有元素
radiansdict.copy()      返回一个字典的浅复制
radiansdict.fromkeys()  创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
radiansdict.get(key, default=None) 返回指定键的值，如果键不在字典中返回 default 设置的默认值
key in dict             如果键在字典dict里返回true，否则返回false
radiansdict.items()     以列表返回可遍历的(键, 值) 元组数组
radiansdict.keys()      返回一个迭代器，可以使用 list() 来转换为列表
radiansdict.setdefault(key, default=None) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
radiansdict.update(dict2) 把字典dict2的键/值对更新到dict里
radiansdict.values()    返回一个迭代器，可以使用 list() 来转换为列表
pop(key[,default])      删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
popitem()               随机返回并删除字典中的最后一对键和值。
"""
