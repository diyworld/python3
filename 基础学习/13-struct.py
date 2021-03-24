
# 列表应用 - 栈
stack = [1,2,3]
print('1: ', stack)
stack.append(4)
stack.append(5)
print('1: ', stack)
print('1: ', stack.pop(-1))
print('1: ', stack)
print()

# 列表应用 - 队列
queue = [1,2,3]
print('2: ', queue)
queue.append(4)
queue.append(5)
print('2: ', queue)
print('2: ', queue.pop(0))
print('2: ', queue)
print()

# 列表推导式
vec = [1,2,3,4,5,6]
print('3: ', vec)
print('3: ', [3*x for x in vec])   # 列表用 []
print('3: ', [[2**x, x*x] for x in vec])
print('3: ', [[2**x, x*x] for x in vec if x>3])
print('3: ', {x:2**x for x in vec}) # key-value, 字典用{}
print()

# 字典遍历
a = {1:'one', 2:'two', 3:'three'}
for k, v in a.items():
    print('4: ', k, v)
print()

# 列表遍历
l = ['zero', 'one', 'two', 'three']
for i in range(len(l)):
    print(i, l[i])




