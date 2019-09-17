# -*- coding:utf-8 -*-
'''
添加数据库数据
'''
import pymysql

#连接数据库
db = pymysql.connect(host='localhost',
                     port = 3306 ,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset= 'utf8')
#获取游标  (操作数据库，执行sql语句，得到执行结果)
cur = db.cursor()

#执行语句
sql = 'insert into interest values (2,"Emma","sing","C",14800,"Good Gril");'
cur.execute(sql)    #执行语句

# 提交到数据库
db.commit()

#关闭游标
cur.close()

#关闭数据库
db.close()

