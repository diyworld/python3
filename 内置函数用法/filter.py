# filter 函数, 过滤不符合条件的元素
# 返回一个矢代器对象, 使用 list 转换为列表
def is_odd(n):
    return True if(n%2 == 1) else False
# 过滤掉偶数
list0 = [1,2,3,4,5,6,7,8,9,0]
list1 = list(filter(is_odd, list0))
print(list1)