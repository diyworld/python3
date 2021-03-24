
import mysql.connector


# 直接连接数据库
print("连接打开数据库")
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1234567ba",
    database = "test_db")

# 创建一个游标对象
mycursor = mydb.cursor()
# 显示版本
mycursor.execute("select version()")
myresult = mycursor.fetchall()
print(f"MySql Version is {myresult[0][0]}")
print()

# 创建表 test_tbl0
mycursor.execute("create table test_tbl0 (id int auto_increment primary key, name varchar(255), url varchar(255))")
print("创建表 test_tbl0")
print()

# 显示本数据库所有表项
mycursor.execute("show tables")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print()

"""
# 插入数据
sql = "insert into test_tbl1(name, url) values (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql, val)
mydb.commit()    # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功。")

# 批量插入
sql1 = "insert into test_tbl1(name, url) VALUES (%s, %s)"
val1 = [
  ('Google', 'https://www.google.com'),
  ('Github', 'https://www.github.com'),
  ('Taobao', 'https://www.taobao.com'),
  ('stackoverflow', 'https://www.stackoverflow.com/')
]
mycursor.executemany(sql1, val1)
mydb.commit()
print(mycursor.rowcount, "记录插入成功。")

"""

# 查询所有记录
mycursor.execute("select * from test_tbl1")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print()
# 只输出 name和 url
mycursor.execute("select name, url from test_tbl1")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print()
# 只读取一条记录
mycursor.execute("select * from test_tbl1")
myresult = mycursor.fetchone()
print(myresult)
myresult = mycursor.fetchall() # toack 为啥一定要执行这个后, 后面的查询才有效??
print()
# 读取name==RUNOOB的记录
mycursor.execute("select * from test_tbl1 where name = 'RUNOOB'")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print()
# 限制查询数据量
mycursor.execute("select * from test_tbl1 where name = 'RUNOOB' limit 3")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print()

# 删除记录
mycursor.execute("delete from test_tbl1 where name = 'RUNOOB'")
mydb.commit()
print(mycursor.rowcount, " 条记录删除")
print()

# 更新表数据
mycursor.execute("update test_tbl1 set name = 'Zhihu' where name = 'Taobao'")
mydb.commit()
print(mycursor.rowcount, " 条记录被修改")
print()

# 如果 test_tbl0存在, 则删除数据表 test_tbl0
mycursor.execute("drop table if exists test_tbl0")
print("删除表 test_tbl0")
print()

# 关闭数据库
mydb.close()
print("关闭数据库")