# mysql-connector是Mysql官方提供的驱动器

import mysql.connector


# 创建数据库连接
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword"
)

print(mydb)

# 创建数据库
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE runoob_db")

# 输出数据库列表
mycursor.execute("SHOW DATABASE")
for x in mycursor:
    print(x)

# 创建数据表
mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")

# 查看表
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

# 添加主键
mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")

# 插入数据
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql,val)
mydb.commit()  # 数据表内容有更新，必须使用该语句
print(mycursor.rowcount, "记录插入成功。")

# 批量插入
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "记录插入成功")

print("1条记录已插入，ID：", mycursor.lastrowid)  # 获取最后插入记录所在行的ID

# 查询数据
mycursor.execute("SELECT * FROM sites")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# 只读取一条数据
mycursor.execute("SELECT * FROM sites")
oneresult = mycursor.fetchone()


#
# PyMySQL是在Python3中用于连接MYSQL服务器的一个库，遵循Python数据库API v2.0规范
#
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

# 使用cursor（）方法创建一个游标对象
cursor = db.cursor()

# 使用execute（）方法执行SQL查询
cursor.execute("SELECT VERSION()")

# 使用fetchone（）方法执行SQL查询
data = cursor.fetchone()
print("Database version: %s" % data)

# 关闭数据库连接
db.close()

# 创建数据库表
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE(
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT)"""
cursor.execute(sql)

# 插入数据
sql = """INSERT INTO EMPLOYEE (FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('MAC', 'Mohan', 20, 'M', 2000)"""

sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%s', '%s', '%s')" % \
       ('MAC', 'Mohan', 20, 'M', 2000)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()

# 查询数据
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %s" % (1000)
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s, lname=%s, age=%s, sex=%s, income=%s" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

# 更新数据库表
sql = "UPDATE EMPLOYEE SET AGE = AGE+1 WHERE SEX = '%c'" % ('M')
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# Python DB API2.0的事务提供了两个方法commit或rollback
# 对于支持事务的数据库，当游标建立之时，就自动开始了一个隐形的数据库事务
sql = "DELETE FROM EMPLOYEE WHERE AGE> %s" % (20)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()


