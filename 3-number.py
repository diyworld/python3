import math
import random

print("#### 数的基本计算函数 ####")
print(0x0a)
print(abs(-10))
print(math.ceil(4.2)) #向上取整
print(math.floor(4.2))#向下取整
print(math.exp(1)) #e的指数幂
print(math.fabs(-10)) #绝对值
print(math.log(math.e))
print(math.log(10))
print(math.log(100,10))
print(math.log10(100))
print(max(1,3,0))
print(min(1,3,0))
print(math.modf(3.14))
print(pow(2,3))
print(round(3.14159)) #四舍五入
print(round(3.14159, 2))
print(math.sqrt(64))

print("#### 随机数 ####")
print(random.choice(range(11,19))) #随机选择一个整数
print(random.choice(['ab', 'bcd', '123', 1, 123.3])) #随机选择一个元素
print(random.randrange(10, 100, 5))#按步长在范围内选择一个数
#随机排列
list0 = [1,2,3,'1','2','3'];
print(list0)
random.shuffle(list0)
print(list0)
print(random.uniform(1.1, 99.999))

#常量
print(math.pi)
print(math.e)

