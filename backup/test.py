# coding=utf-8
import pymysql

# 打开数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', database='testdb')

# 使用cursor方法创建一个游标对象
cursor = conn.cursor()

# 使用execute方法执行sql查询
# cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

# 使用预处理语句创建表
# sql1 = """CREATE TABLE `employee` (
# `first_name` varchar(255) DEFAULT NULL COMMENT '姓',
# `last_name` varchar(255) DEFAULT NULL COMMENT '名',
# `age` int(11) DEFAULT NULL COMMENT '年龄',
# `sex` varchar(255) DEFAULT NULL COMMENT '性别',
# `income` varchar(255) DEFAULT NULL COMMENT '收入'
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
# """
sql = "select * from employee"
#向数据表中插入数据
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
# LAST_NAME, AGE, SEX, INCOME)
# VALUES ('Mac','Gglanw',20, 'M', 10000)"""

# #使用fetchone方法获取单条数据
# data = cursor.fetchone()

#执行sql
cursor.execute(sql)
# conn.commit()  #提交到数据库执行

results = cursor.fetchall()
# 遍历列表
for row in results:
    # print(row)
    first_name = row[0]
    last_name = row[1]
    age = row[2]
    sex = row[3]
    income = row[4]
    print(first_name, last_name, age, sex, income)


cursor.close()
conn.close()
