

# 创建一个类
# 类的方法必须带至少一个参数self, 代表类的实例
class MyClass:
    # 基本属性
    oob = 'hahaha'
    a = 0
    b = 0
    # 私有属性
    __pri = 0
    def __init__(self): # 构造函数
        self.a = 1
        self.b = 2
    def oobf(self): # 需要带入自身的实例索引
        print("oob = ", self.oob)
        print("a = ", self.a)
        print("b = ", self.b)
        print("__pri = ", self.__pri)
    def classparam(self):
        print("self = ", self)
        print("__class__ = ", self.__class__)

x = MyClass()
x.oobf()
x.classparam()
print(x.a, x.b)

# 继承
class people:
    name = ''
    age = 0
    __weight = 0 #私有属性
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.__weight = weight
    def speak(self):
        print(f"{self.name} 想: 我 {self.age} 岁，我会改变世界的。")
 
class student(people): #单继承示例
    grade = ''
    def __init__(self,name,age,weight,grade):
        #调用父类的构造函数
        people.__init__(self,name,age,weight)
        self.grade = grade
    def speak(self): #重写父类的方法
        print(f"{self.name} 说: 我曾经 {self.age} 岁，我在读 {self.grade} 年级")
 
 
p = people('mgd',31,140)
p.speak()

s = student('mgd',10,60,3)
s.speak()

