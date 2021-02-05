
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
print(len('hello')) #字符长度
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

str3 = "123.4"
print(str3.rjust(7, ' '))
print(str3.rjust(7, '0'))
print(str3.ljust(7, ' '))
print(str3.ljust(7, '0'))
