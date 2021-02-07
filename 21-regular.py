import re

# 匹配查找: re.search
line = "abcd,test@runoob.com 1234"
# <re.M>多行匹配, <re.I>忽略大小写
m1 = re.search(r'com', line, re.M|re.I)
if m1: print('1:', m1.group())
m2 = re.match(r'.*(com)', line, re.M|re.I)
if m2: print('1:', m2.group(1))
# 邮箱匹配
# <\b>匹配单词边界
# <[\w.%+-]>匹配字符和数字，以及特殊字符 .%+-，也可以写成[a-zA-Z0-9.%+-]
# <+>表示前面的表达式至少匹配一个字符
# <@>匹配字符 @
# <a-zA-Z>匹配大小写字母
m3 = re.search(r'\b[\w.%+-]+@[\w.-]+[a-zA-Z]\b', line, 0)
if m3: print ('2:', m3.group())
print()

# 定义一个模式: re.compile 
email_pattern = re.compile(r'\b[\w.%+-]+@[\w.-]+[a-zA-Z]\b')
m4 = email_pattern.search(line)
print('3:', m4)         # 匹配到的参数对象
print('3:', m4.group()) # 匹配的字符串
print('3:', m4.span())  # 匹配字符串索引
print()

# 替换: re.sub
phone = "2004-959-559 # 这是一个99999电话号码"
# 移除非数字的内容
# <#.*>匹配#后面的所有字符
# <[^0-9]>匹配非数字字符
# <|>先匹配第一个项并进行替换操作, 然后在匹配第二个项并进行替换操作
num = re.sub(r'#.*|[^0-9]', "", phone)
print ("电话号码 : ", num)
print()

# 找出匹配项: re.findall
str0 = 'run88oob 123google 456'
r1 = re.findall(r'[0-9]+', str0)
pttrn = re.compile(r'[0-9]+')
r2 = pttrn.match(str0)
r3 = pttrn.search(str0)
r4 = pttrn.findall(str0)
print('4:', r1)
print('4:', r2)
print('4:', r3)
print('4:', r4)
print()

# 返回矢代器: re.finditer
str0 = 'run88oob 123google 456'
it = re.finditer(r'[0-9]+', str0)
for s in it: print('5:', s.group())
print()

# 分割字符串: re.split
str0 = 'I say hello world'
r1 = re.split(' ', str0)
print('6:', r1)

"""
<<<re模块函数的标志位说明>>>
re.I: 大小写不敏感
re.L: 本地化识别???
re.M: 多行匹配, 影响 ^和 $
re.S: 使点<.>匹配包括换行在内的所有字符

<<<正则表达式实例>>>
python     匹配 "python".
[Pp]ython  匹配 "Python" 或 "python"
[rou.!@#]  匹配中括号内的任意一个字符
[0-9]      匹配任何数字。类似于 [0123456789]
[a-z]      匹配任何小写字母
[A-Z]      匹配任何大写字母
[a-zA-Z0-9]匹配任何字母及数字
[^aeiou]   除了aeiou字母以外的所有字符
[^0-9]     匹配除了数字外的字符

<<<特殊字符>>>
.      匹配除 "\n" 之外的任何单个字符，'[.\n]'匹配所有字符。
\d     匹配一个数字字符。等价于 [0-9]。
\D     匹配一个非数字字符。等价于 [^0-9]。
\s     匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
\S     匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
\w     匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
\W     匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。

<<<元字符>>>
\      转义字符, 将下一个字符转义为特殊字符
^      匹配输入字符串的开始位置
$      匹配输入字符串的结束位置
*      匹配前面表达式n次，n >= 0
+      匹配前面表达式n次，n >= 1
?      匹配前面表达式n次，0<= n <=1
.      匹配除\r\n之外的任何字符
|      或的关系，x|y，匹配x或y，但注意会先处理x
"""
