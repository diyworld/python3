
#集合，自动去重
a = {'a', 'b', 'b'}
print('1: ', a)

#集合运算
a = set('abcd1')
b = set('1234a')
c = {x for x in a if x not in b}
print('2: ', 'a =   ', a)
print('2: ', 'b =   ', b)
print('2: ', 'a-b = ', a-b)
print('2: ', 'a|b = ', a|b)
print('2: ', 'a&b = ', a&b)
print('2: ', 'a^b = ', a^b)
print('2: ', 'c =   ', c)

#添加/删除元素, 集合不支持嵌套
a = {'abc', '123', 100}
print('3: ', a)
a.add(200)  #新增元素
print('3: ', a)
a.update({1,2,3}) #新增元素, 可以是多个元素
print('3: ', a)
a.remove(200) #删除元素, 不存在会报错
print('3: ', a)
a.discard(1) #删除元素, 不存在不会报错
print('3: ', a)
a.pop() #随机删除一个元素
print('3: ', a)

#集合元素
a = {'abc', '123', 100}
print('4: ', len(a)) #集合大小
print('4: ', 'abc' in a) #元素存在性
print('4: ', 'ab' in a)
a.clear() #清空集合
print('4: ', a)

#集合方法
"""
add()               为集合添加元素
clear()             移除集合中的所有元素
copy()              拷贝一个集合
difference()        返回多个集合的差集
difference_update() 移除集合中的元素，该元素在指定的集合也存在。
discard()           删除集合中指定的元素
intersection()      返回集合的交集
intersection_update() 返回集合的交集。
isdisjoint()        判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()          判断指定集合是否为该方法参数集合的子集。
issuperset()        判断该方法的参数集合是否为指定集合的子集
pop()               随机移除元素
remove()            移除指定元素
symmetric_difference() 返回两个集合中不重复的元素集合。
symmetric_difference_update() 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()             返回两个集合的并集
update()            给集合添加元素
"""

