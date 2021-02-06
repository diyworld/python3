
# if 结构

a = 1
b = 2

if a < b:
    print('a<b')
elif a > b:
    print('a>b')
else:
    print('a==b')

# while 循环
a = 1
while a < 1000:
    print(a, end = ' ')
    a *= 2

var = 0
while var != 0:
    var = int(input("输入一个数字: "))
    print(var)
else:
    print(f"var == {var}, and exit")

# for 循环
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    if x == 'C':
        print(f"I master the \"{x}\"")
    else:
        print(f"I don't master the \"{x}\"")
else:
    print("End")

for i in range(0, 100, 7):
    print(i, end = ' ')
print("\n")

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(f"a[{i}] = {a[i]}")

a = 1
while True:
    a *= 2
    if a > 100:
        break;
    if a % 8 != 0:
        continue
    print(a, end = ' ')
else:
    print("xxxxxx\n")

