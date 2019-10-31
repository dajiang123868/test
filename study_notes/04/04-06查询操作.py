#_*_coding:utf-8_*_
"""
1.exact
article = Article.objects.get(id__exact=14)
article = Article.objects.get(id__exact=None)

对应擦查询翻译的sql为
select ... from article where id=14;
select ... from article where id IS NULL;

2.使用like进行查找  iexact
article = Article.objects.filter(title__iexact='hello world')
select ... from article where title like 'hello world';

3.contains
articles = Article.objects.filter(title__contains='hello')
select ... where title like binary '%hello%';  区分大小写的模糊查询

4.icontains
大小写不敏感的匹配查询。示例代码如下：
articles = Article.objects.filter(title__icontains='hello')
select ... where title like '%hello%';

5.in
articles = Article.objects.filter(id__in=[1,2,3])
select ... where id in (1,3,4)

也可以传递一个QuerySet对象进去，示例代码如下：
inner_qs = Article.objects.filter(title__contains='hello')
categories = Category.objects.filter(article__in=inner_qs)
select ...from category where article.id in (select id from article where title like '%hello%');

6.gt
查询某个field的值大于给定的值，
articles = Article.objects.filter(id__gt=4)
select ... where id > 4;

7.gte：
类似于gt，是大于等于。

8.lt
类似于gt是小于。

9.lte：
类似于lt，是小于等于。

10.startswith
articles = Article.objects.filter(title__startswith='hello')
select ... where title like 'hello%'

11.issatrtwith
类似于startswith，但是大小写是不敏感的。

12.endswith：
articles = Article.objects.filter(title__endswith='world')
select ... where title like '%world';

13.iendswith
类似于endswith，只不过大小写不敏感。

14.range：
from django.utils.timezone import make_aware
from datetime import datetime
start_date = make_aware(datetime(year=2018,month=1,day=1))
end_date = make_aware(datetime(year=2018,month=3,day=29,hour=16))
articles = Article.objects.filter(pub_date__range=(start_date,end_date))
select ... from article where pub_time between '2018-01-01' and '2018-12-12'。

不包含最后一个值
USE_TZ=True
TIME_ZONE='Asia/Shanghai'
make_aware会将指定的时间转换为TIME_ZONE中指定的时区的时间。

15.date
articles = Article.objects.filter(pub_date__date=date(2018,3,29))
select ... WHERE DATE(CONVERT_TZ(`front_article`.`pub_date`, 'UTC', 'Asia/Shanghai')) = 2018-03-29

16.year
articles = Article.objects.filter(pub_date__year=2018)
articles = Article.objects.filter(pub_date__year__gte=2017)

select ... where pub_date between '2018-01-01' and '2018-12-31';
select ... where pub_date >= '2017-01-01';

17.month，day，week_day,time
1表示星期天，7表示星期六，2-6代表的是星期一到星期五。
articles = Article.objects.filter(pub_date__time=datetime.time(12,12,12));

18.isnull
articles = Article.objects.filter(pub_date__isnull=False)
select ... where pub_date is not null;

19.regex和iregex：


"""

"""
根据关联查询
class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=100,null=True)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)



categories = Category.object.filter(article__title__contains("hello"))



"""


"""
聚合函数：
1.Avg
 from django.db.models import Avg
 result = Book.objects.aggregate(Avg('price'))
 print(result)
  {"price__avg":23.0}

其中price__avg的结构是根据field__avg规则构成的。如果想要修改默认的名字，那么可以将Avg赋值给一个关键字参数。示例代码如下：
 result = Book.objects.aggregate(my_avg=Avg('price'))
 print(result)
  {"my_avg":23}
  
  
  
2.
from django.db.models import Count
result = Book.objects.aggregate(book_num=Count('id'))
以上的result将返回Book表中总共有多少本图书。
Count类中，还有另外一个参数叫做distinct，默认是等于False，如果是等于True，那么将去掉那些重复的值。比如要获取作者表中所有的不重复的邮箱总共有多少个，那么可以通过以下代码来实现：

     from djang.db.models import Count
     result = Author.objects.aggregate(count=Count('email',distinct=True))

3.Max和Min：获取指定对象的最大值和最小值。比如想要获取Author表中，最大的年龄和最小的年龄分别是多少。那么可以通过以下代码来实现：

 from django.db.models import Max,Min
 result = Author.objects.aggregate(Max('age'),Min('age'))
如果最大的年龄是88,最小的年龄是18。那么以上的result将为：

 {"age__max":88,"age__min":18}
 
 
 4.Sum：求指定对象的总和。比如要求图书的销售总额。那么可以使用以下代码实现：

 from djang.db.models import Sum
 result = Book.objects.annotate(total=Sum("bookstore__price")).values("name","total")
     

"""

"""
aggregate和annotate的区别：
aggregate：返回使用聚合函数后的字段和值。

annotate：在原来模型字段的基础之上添加一个使用了聚合函数的字段，并且在使用聚合函数的时候，会使用当前这个模型的主键进行分组（group by）。
比如以上Sum的例子，如果使用的是annotate，那么将在每条图书的数据上都添加一个字段叫做total，计算这本书的销售总额。
而如果使用的是aggregate，那么将求所有图书的销售总额。


"""


"""
F表达式和Q表达式：



"""