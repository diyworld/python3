
str0 = "hello python3!"
print(str0)
print(str0[3:6]) #左闭右开

#字符串拼接
str1 = str0 + " I like this script."
print(str1)

#字符串运算
a = 'a'
b = 'abc'
print(a+b)
print(a*5)
print(a in b)
print(b in a)
print('abc\n123\txyz')
print(r'abc\n123\txyz') #输出原始字符串，不转义
#多行字符输出
print("""hello world
this is beautiful world.""")
errHtml = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(errHtml)


#字面量格式化字符串 f-string
name = 'python3'
print(f'hello {name}')
print(f'hello name')
print(f'{1+2}')


#字符串函数
str0 = "abc\t123"
a = 'hello'
print(str.capitalize("hello")) #首字母转大写
print(a.capitalize())
print(len(a)) #字符长度
print(str0.expandtabs(1))
print(str0)
print(str0.find('123'))
print(str0.find('xyz'))

#合并字符串
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))

#字符替换
str1 = "hello world 123123 kkk zzz"
print(str1.replace('123', 'abc'))

#字符串切片
str2 = "this is string example....wow!!!"
print (str2.split(' '))       # 以空格为分隔符
print (str2.split('w'))     # 以 w 为分隔符

#格式化数字
str3 = "123.4"
print(str3.rjust(7, ' '))
print(str3.rjust(7, '0'))
print(str3.ljust(7, ' '))
print(str3.ljust(7, '0'))

"""
capitalize()                将字符串的第一个字符转换为大写
center(width, fillchar)     返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
count(str, beg= 0,end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
bytes.decode(encoding="utf-8", errors="strict") Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
encode(encoding='UTF-8',errors='strict') 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
endswith(suffix, beg=0, end=len(string)) 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
expandtabs(tabsize=8)       把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
find(str, beg=0, end=len(string)) 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
index(str, beg=0, end=len(string)) 跟find()方法一样，只不过如果str不在字符串中会报一个异常。
isalnum()                   如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False
isalpha()                   如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
isdigit()                   如果字符串只包含数字则返回 True 否则返回 False..
islower()                   如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
isnumeric()                 如果字符串中只包含数字字符，则返回 True，否则返回 False
isspace()                   如果字符串中只包含空白，则返回 True，否则返回 False.
istitle()                   如果字符串是标题化的(见 title())则返回 True，否则返回 False
isupper()                   如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
join(seq)                   以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
len(string)                 返回字符串长度
ljust(width[, fillchar])    返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
lower()                     转换字符串中所有大写字符为小写.
lstrip()                    截掉字符串左边的空格或指定字符。
maketrans() 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
max(str)                    返回字符串 str 中最大的字母。
min(str)                    返回字符串 str 中最小的字母。
replace(old, new [, max])   把将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。
rfind(str, beg=0,end=len(string)) 类似于 find()函数，不过是从右边开始查找.
rindex( str, beg=0, end=len(string)) 类似于 index()，不过是从右边开始.
rjust(width,[, fillchar])   返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
rstrip()                    删除字符串字符串末尾的空格.
split(str="", num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
splitlines([keepends])      按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
startswith(substr, beg=0,end=len(string)) 检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
strip([chars])              在字符串上执行 lstrip()和 rstrip() 35   swapcase() 将字符串中大写转换为小写，小写转换为大写
title()                     返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle()) 37 translate(table, deletechars="") 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
upper()                     转换字符串中的小写字母为大写
zfill (width)               返回长度为 width 的字符串，原字符串右对齐，前面填充0
isdecimal()                 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
"""
