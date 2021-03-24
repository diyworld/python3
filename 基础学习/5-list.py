
# 列表基本性质
list0 = ['one', 2, 'thr', 4]
list1 = [1, 'hello', list0]
print('1: ', list1)
print('2: ', list1[0])
print('3: ', list1[1])
print('4: ', list1[0:2])
print('5: ', list0[1:])
print('\n')

#列表基本操作
list0 = ['zero', 'one', 'two', 'three']
list1 = [0, 2, 3]
list1[0] = 1
print('1: ', list1)
print('2: ', len(list1))
print('3: ', list0 + list1)
print('4: ', list1 * 4)

idx = 0
for x in list0:
    print(f"5:  list0[{idx}] = {x}")
    idx = idx + 1
print('\n')

#列表赋值是指针的传递
list1 = [0, 1, 2]
list2 = list1
list3 = list1.copy()
print('1: ', f"list1 = {list1}\n1:  list2 = {list2}\n1:  list3 = {list3}")
list2[0] = 3
list3[1] = 3
print('2: ', f"list1 = {list1}\n2:  list2 = {list2}\n2:  list3 = {list3}")
print('\n')

#函数
#注意不能是 list1.len()
list1 = [0, 2, 3, 5]
print('1: ', len(list1))
print('2: ', max(list1))
print('3: ', min(list1))
print('\n')

#方法
list0 = ['a', 'b', 'c']
list1 = [1,1,2,3]
list1.append(4)    #末尾添加对象
print('1: ', list1)
list1.count(1)     #统计对象出现次数
print('2: ', list1)
list1.extend(list0)#列表拼接
print('3: ', list1)
list1.pop(-1)      #移除最后一个值
print('4: ', list1)
list1.pop(0)       #移除第一个值
print('5: ', list1)
list1.remove(4)    #移除匹第一个配项  
print('6: ', list1)
print('\n')

list0 = [(2, 2), (3, 4), (4, 1), (1, 3)]
print('1: ', list0) #原始序列
list1 = list0.copy()
list1.sort()        #直接排序（默认第1个元素排序）
print('2: ', list1)
list2 = list0.copy()
list2.sort(reverse = True) #反序
print('3: ', list2)
def takeSecond(elem):
    return elem[0] # 获取列表的第二个元素
list3 = list0.copy()
list3.sort(key = takeSecond, reverse = False) #指定第2个元素排序
print('4: ', list3)
list0.clear() #清空列表
print('5: ', list0)
print('\n')

"""
list.append(obj)        在列表末尾添加新的对象
list.count(obj)         统计某个元素在列表中出现的次数
list.extend(seq)        在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)         从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj) 将对象插入列表
list.pop([index=-1])    移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)        移除列表中某个值的第一个匹配项
list.reverse()          反向列表中元素
list.sort( key=None, reverse=False) 对原列表进行排序
list.clear()            清空列表
list.copy()             复制列表
"""
