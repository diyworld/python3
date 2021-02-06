
#菲薄垃圾序列
a, b = 0, 1
while b < 1000:
    print(b)
    a, b = b, (a + b)
