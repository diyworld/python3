
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
            values ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    cursor.execute(cmd)
    mydb.commit()
except:
    print("发生错误，进行回滚")
    mydb.rollback()
print("插入1条数据")
print()

# 关闭数据库
mydb.close()
print("关闭数据库")