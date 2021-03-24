
WORKTMPPATH = "C:\\ccx\\workplace\\python3\\tmp"
tfile = WORKTMPPATH + "\\14-test.txt"

# 写文件
print('1: ', tfile)
f = open(tfile, 'w')
f.write("This is a test content!\n")
f.write("abc\n")
f.write("123\n")
f.close()

# 读文件
f = open(tfile, 'r')
str0 = f.read()
print('2: ', f"str0 = <{str0}>")
f.close()

# 按行读取文件
f = open(tfile, 'r')
for line in f:
    print(line, end='')
print('3: ', "end")
f.close()

# pickle模块 - 保存对象到文件
import pickle
data1file = WORKTMPPATH + "\\data1.pkl"
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
data2 = [1,3,5,7,9]
print('4: ', data1)
print('4: ', data2)
outfile = open(data1file, 'wb')
pickle.dump(data1, outfile)
pickle.dump(data2, outfile)
outfile.close()

# pickle模块 - 从文件读取对象信息
infile = open(data1file, 'rb')
obj1 = pickle.load(infile)
obj2 = pickle.load(infile)
infile.close()
print('4: ', obj1)
print('4: ', obj2)


