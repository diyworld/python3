
import mysql.connector

print("连接打开数据库")
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1234567ba",
    database = "test_db")

# 创建一个游标对象
cursor = mydb.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("drop table if exists employee")

# 创建表
cmd = """create table employee(
            first_name char(20) not null,
            last_name char(20),
            age int,
            sex char(1),
            income float)"""
cursor.execute(cmd)
print("创建表 employee")
print()

# 插入数据
cmd = """ insert into employee(first_name,
            last_name, age, sex, income)
            values ('Mac', 'Mohan', 22, 'M', 2000)"""
try:
    cursor.execute(cmd)
    mydb.commit()
except:
    print("发生错误，进行回滚")
    mydb.rollback()
print("插入1条数据")
print()

# 批量插入数据
cmd1 = "insert into employee(first_name, last_name, age, sex, income) values (%s,%s,%d,%s,%d)" # 这里用%d不行
cmd2 = "insert into employee(first_name, last_name, age, sex, income) values (%s,%s,%s,%s,%s)"
val1 = [('Ali', 'si', 32, 'G', 5000),
        ('Uzi', 'ez', 29, 'M', 1000),
        ('Lili', 'chen', 22, 'G', 3000),
        ('Kan', 'kan', 25, 'M', 1500)]
val2 = [('li', 'si', 16, 'F', 1000),
       ('Bruse', 'Jerry', 30, 'F', 3000),
       ('Lee', 'Tomcat', 40, 'M', 4000),
       ('zhang', 'san', 18, 'M', 1500)]
try:
    cursor.executemany(cmd2, val1)
    mydb.commit()
    print(f"插入{cursor.rowcount}条数据")
except:
    print("插入多条数据发生错误，进行回滚")
    mydb.rollback()
print()

# 查询
cmd = "select * from employee where income > %s" % (1000)
try:
   # 执行SQL语句
   cursor.execute(cmd)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
       # 打印结果
      print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fetch data")
print()

# 更新
cmd = "update employee set age = age + 1 where sex = '%c'" % ('M')
try:
    cursor.execute(cmd)
    mydb.commit()
except:
    mydb.rollback()
print(cursor.rowcount, " 条记录被修改")
print("更新数据库完毕")
print()

# 删除表项
cmd = "delete from employee where age > %s" % (30)
try:
    cursor.execute(cmd)
    mydb.commit()
except:
    mydb.rollback()
print("更新数据库完毕")
print()

# 关闭数据库
cursor.close()
mydb.close()
print("关闭数据库连接")


