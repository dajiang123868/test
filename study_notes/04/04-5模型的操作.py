#_*_coding:utf-8_*_
"""
1.添加一个模型到数据库中(插入一组数据)：
class Book(models.Model):
    name = models.CharField(max_length=20,null=False)
    desc = models.CharField(max_length=100,name='description',db_column="description1")
    pub_date = models.DateTimeField(auto_now_add=True)

book = Book(name='三国演义',desc='三国英雄！')
book.save()

2.查找所有数据：
books = Book.objects.all()

3.数据过滤
objects的filter
books = Book.objects.filter(name='三国演义')
多个条件
books = Book.objects.filter(name='三国演义',desc='test')
没有找到满足条件的数据时候返回一个空列表

4.获取单个对象
使用filter返回的是所有满足条件的结果集，如果只需要返回第一个满足的条件对象。可以使用get方法
book = Book.objects.get(name='三国演义')
如果没有找到满足的条件对象。就会抛出异常’

5.数据排序
books = Book.objects.order_by('pub_date')
会按照pub——date从小到大排序
如果进行倒序排序：
books = Book.objects.order_by("-pub_date")

6.修改数据：
修改对象的某个属性即可
from datetime import datetime
book = Book.objects.get(name='三国演义')
book.pub_date = datetime.now()
book.save()

7.删除数据
book = Book.objects.get(name='三国演义')
book.delete()






"""