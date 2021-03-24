
# 矢代器
list0 = [1,2,3]
it = iter(list0)
print(next(it))
for x in it:
    print('>', x)

list1 = ['a', 'b', 'c']
it1 = iter(list1)
while True:
    try:
        print(next(it1), end = ' ')
    except StopIteration:
        break;
print('\n')

# 创建矢代器
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 3:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
 
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))

# 生成器
# 使用了 yield 的函数被称为生成器（generator）
import sys
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a # 每次调用 next()都在这里返回和开始
        a, b = b, a + b
        counter += 1

f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()



