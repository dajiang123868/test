#_*_coding:utf-8_*_
"""
第一种使用原生的sql

使用django封装好的connection对象，会自动读取settings.py中数据库的配置信息
from django.db import connection
# 获取游标对象
cursor = connection.cursor()
# 拿到游标对象后执行sql语句
cursor.execute("select * from book")
# 获取所有的数据
rows = cursor.fetchall()
# 遍历查询到的数据
for row in rows:
    print(row)
https://www.python.org/dev/peps/pep-0249/。
"""


"""
Python DB API下规范下cursor对象常用接口：
1.description：如果cursor执行了查询的sql代码。那么读取cursor.description属性的时候，将返回一个列表，这个列表中装的是元组，元组中装的分别是(name,type_code,display_size,internal_size,precision,scale,null_ok)，其中name代表的是查找出来的数据的字段名称，其他参数暂时用处不大。
2.rowcount：代表的是在执行了sql语句后受影响的行数。
3.close：关闭游标。关闭游标以后就再也不能使用了，否则会抛出异常。
4.execute(sql[,parameters])：执行某个sql语句。如果在执行sql语句的时候还需要传递参数，那么可以传给parameters参数。
示例代码如下：
cursor.execute("select * from article where id=%s",(1,))
5.fetchone：在执行了查询操作以后，获取第一条数据。
6.fetchmany(size)：在执行查询操作以后，获取多条数据。具体是多少条要看传的size参数。如果不传size参数，那么默认是获取第一条数据。
7.fetchall：获取所有满足sql语句的数据。

"""