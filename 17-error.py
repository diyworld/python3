import sys
# try/except

# ValueError 异常
try:
    # 利用int()转换为整数, 如果不可转换, 则表示输入的不是数字
    x = int(input("Input a number: "))
    print(x*x)
except ValueError: # 值错误
    print("You input is not a number")

# OSError 异常
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

# ZeroDivisionError 异常
def thisfails():
    x = 1/0
try:
    thisfails()
except ZeroDivisionError as err:
    print("error: ",(err))

# 抛出异常 raise
x = 5
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

# 清理行为 finally
try:
    raise KeyboardInterrupt
finally:
    print("无论是否发生异常，最终都会执行这里，用于进行善后工作")



