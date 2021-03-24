
# 函数
def myadd(a, b):
    return a + b

print(myadd(1,2))

# 引用参数
def changeme(mylist):
    mylist.append([1,2,3,4])
    print ("函数内取值: ", mylist)
mylist = [10,20,30]
print ("原始列表取值: ", mylist)
changeme( mylist )
print ("函数外取值: ", mylist)

# 关键字参数
def myfunc(nm, ag):
    print(f"nm = {nm}", end = ', ')
    print(f"ag = {ag}")
myfunc('mgd', 31)
myfunc(ag = 31, nm = 'mgd')

# 不定长参数
# 以元组的形似传入
def printinfo(arg1, *vartuple):
    print (arg1, end = ' ')
    for var in vartuple:
        print(var, end = ' ')
    print()
printinfo(10)
printinfo(10, 60, 50)

# 不定长参数
# 以字典的形似传入
def printinfo1(fmt, **dict0):
    print(fmt)
    print(dict0)
    #for k in dict0:
    #    print(f"{k}:{dict0[k]},", end = ' ')
    #print()
a0 = {0, 'zero'}
a = {1:'one'}
b = {1:'one', 2:'two', 3:'three'}

#printinfo1(a) ??
#printinfo1(b) ??

# 匿名函数
ssum = lambda a, b: a+b
NAMESIZE = lambda: 64
print(ssum('a', 'b'))
print(ssum(2, 1))
print(NAMESIZE())
