#_*_coding:utf-8_*_

"""
使用orm比原生slq的好处
1.代码的重复率高
2.维护不方便
3.sql注入，安全隐患
性能损耗比较低，可以忽略不计
"""



"""
创建ORM模型
ORM模型一般都是放在app的models.py文件中。
每个app都可以拥有自己的模型。
并且如果这个模型想要映射到数据库中，
那么这个app必须要放在settings.py的INSTALLED_APP中进行安装。
以下是写一个简单的书籍ORM模型。
示例代码如下：
from django.db import models
class Book(models.Model):
    name = models.CharField(max_length=20,null=False)
    author = models.CharField(max_length=20,null=False)
    pub_time = models.DateTimeField(default=datetime.now)
    price = models.FloatField(default=0)





映射模型到数据库中：
将ORM模型映射到数据库中，总结起来就是以下几步：
在settings.py中，配置好DATABASES，做好数据库相关的配置。
在app中的models.py中定义好模型，这个模型必须继承自django.db.models。
将这个app添加到settings.py的INSTALLED_APP中。
在命令行终端，进入到项目所在的路径，然后执行命令python manage.py makemigrations来生成迁移脚本文件。
同样在命令行中，执行命令python manage.py migrate来将迁移脚本文件映射到数据库中。



"""


"""
模型常用属性
常用字段：
AutoField：
映射到数据库中是int类型，可以有自动增长的特性。一般不需要使用这个类型，如果不指定主键，那么模型会自动的生成一个叫做id的自动增长的主键。如果你想指定一个其他名字的并且具有自动增长的主键，使用AutoField也是可以的。

BigAutoField：
64位的整形，类似于AutoField，只不过是产生的数据的范围是从1-9223372036854775807。

BooleanField：
在模型层面接收的是True/False。在数据库层面是tinyint类型。如果没有指定默认值，默认值是None。

CharField：
在数据库层面是varchar类型。
在Python层面就是普通的字符串。
这个类型在使用的时候必须要指定最大的长度，也即必须要传递max_length这个关键字参数进去。

DateField：
auto_now：在每次这个数据保存的时候，都使用当前的时间。比如作为一个记录修改日期的字段，可以将这个属性设置为True。
auto_now_add：在每次数据第一次被添加进去的时候，都使用当前的时间。比如作为一个记录第一次入库的字段，可以将这个属性设置为True。

DateTimeField：
日期时间类型，类似于DateField。不仅仅可以存储日期，还可以存储时间。映射到数据库中是datetime类型。这个Field也可以使用auto_now和auto_now_add两个属性。

TimeField：
时间类型。在数据库中是time类型。在Python中是datetime.time类型。

EmailField：
类似于CharField。在数据库底层也是一个varchar类型。最大长度是254个字符。

FileField：
用来存储文件的。这个请参考后面的文件上传章节部分。

ImageField：
用来存储图片文件的。这个请参考后面的图片上传章节部分。

FloatField：
浮点类型。映射到数据库中是float类型。

IntegerField：
整形。值的区间是-2147483648——2147483647。

BigIntegerField：
大整形。值的区间是-9223372036854775808——9223372036854775807。

PositiveIntegerField：
正整形。值的区间是0——2147483647。

SmallIntegerField：
小整形。值的区间是-32768——32767。


PositiveSmallIntegerField：
正小整形。值的区间是0——32767。

TextField：
大量的文本类型。映射到数据库中是longtext类型。


UUIDField：
只能存储uuid格式的字符串。uuid是一个32位的全球唯一的字符串，一般用来作为主键。

URLField：
类似于CharField，只不过只能用来存储url格式的字符串。并且默认的max_length是200。

"""

"""
Field的常用参数：
null：
如果设置为True，Django将会在映射表的时候指定是否为空。默认是为False。在使用字符串相关的Field（CharField/TextField）的时候，官方推荐尽量不要使用这个参数，也就是保持默认值False。因为Django在处理字符串相关的Field的时候，即使这个Field的null=False，如果你没有给这个Field传递任何值，那么Django也会使用一个空的字符串""来作为默认值存储进去。因此如果再使用null=True，Django会产生两种空值的情形（NULL或者空字符串）。如果想要在表单验证的时候允许这个字符串为空，那么建议使用blank=True。如果你的Field是BooleanField，那么对应的可空的字段则为NullBooleanField。


blank：
标识这个字段在表单验证的时候是否可以为空。默认是False。
这个和null是有区别的，null是一个纯数据库级别的。而blank是表单验证级别的。


db_column：
这个字段在数据库中的名字。如果没有设置这个参数，那么将会使用模型中属性的名字。

default：
默认值。可以为一个值，或者是一个函数，但是不支持lambda表达式。并且不支持列表/字典/集合等可变的数据结构。

primary_key：
是否为主键。默认是False。

unique：
在表中这个字段的值是否唯一。一般是设置手机号码/邮箱等。

"""

"""
模型中Meta配置：

对于一些模型级别的配置。我们可以在模型中定义一个类，叫做Meta。然后在这个类中添加一些类属性来控制模型的作用。比如我们想要在数据库映射的时候使用自己指定的表名，而不是使用模型的名称。那么我们可以在Meta类中添加一个db_table的属性。示例代码如下：

class Book(models.Model):
    name = models.CharField(max_length=20,null=False)
    desc = models.CharField(max_length=100,name='description',db_column="description1")
    class Meta:
        db_table = 'book_model'







Meta类中的一些常用配置:

db_table:
模型映射到数据库中的表名。如果没有就是默认表名
ordering:
查找数据的排序，比如查询数据的时候按照添加的时间排序，


class Book(models.Model):
    name = models.CharField(max_length=20,null=False)
    desc = models.CharField(max_length=100,name='description',db_column="description1")
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'book_model'
        ordering = ['pub_date']

更多配置：
https://docs.djangoproject.com/en/2.0/ref/models/options/

"""

"""
外键和表的关系：
外键：
在MySQL中，表有两种引擎，一种是InnoDB，另外一种是myisam。如果使用的是InnoDB引擎，是支持外键约束的。外键的存在使得ORM框架在处理表关系的时候异常的强大。因此这里我们首先来介绍下外键在Django中的使用。


比如有一个User和一个Article两个模型。
一个User可以发表多篇文章，一个Article只能有一个Author，
并且通过外键进行引用。
那么相关的示例代码如下
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("User",on_delete=models.CASCADE)


定义为class ForeignKey(to,on_delete,**options)
第一个参数是引用的是哪个模型，
第二个参数是在使用外键引用的模型数据被删除了，
这个字段该如何处理，比如有CASCADE、SET_NULL等。



以上使用ForeignKey来定义模型之间的关系。即在article的实例中可以通过author属性来操作对应的User模型。这样使用起来非常的方便。示例代码如下：

article = Article(title='abc',content='123')
author = User(username='张三',password='111111')
article.author = author
article.save()

# 修改article.author上的值
article.author.username = '李四'
article.save()




如果模型的外键引用的是本身自己这个模型，那么to参数可以为'self'，或者是这个模型的名字。在论坛开发中，一般评论都可以进行二级评论，即可以针对另外一个评论进行评论，那么在定义模型的时候就需要使用外键来引用自身。示例代码如下：

class Comment(models.Model):
    content = models.TextField()
    origin_comment = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    # 或者
    # origin_comment = models.ForeignKey('Comment',on_delete=models.CASCADE,null=True)

"""

"""
外键删除操作：
如果一个模型使用了外键。那么在对方那个模型被删掉后，该进行什么样的操作。可以通过on_delete来指定。
可以指定的类型如下：
1.CASCADE：级联操作。如果外键对应的那条数据被删除了，那么这条数据也会被删除。
2.PROTECT：受保护。即只要这条数据引用了外键的那条数据，那么就不能删除外键的那条数据。
3.SET_NULL：设置为空。如果外键的那条数据被删除了，那么在本条数据上就将这个字段设置为空。如果设置这个选项，前提是要指定这个字段可以为空。
4.SET_DEFAULT：设置默认值。如果外键的那条数据被删除了，那么本条数据上就将这个字段设置为默认值。如果设置这个选项，前提是要指定这个字段一个默认值
5.SET()：如果外键的那条数据被删除了。那么将会获取SET函数中的值来作为这个外键的值。SET函数可以接收一个可以调用的对象（比如函数或者方法），如果是可以调用的对象，那么会将这个对象调用后的结果作为值返回回去。
6.DO_NOTHING：不采取任何行为。一切全看数据库级别的约束。
"""



