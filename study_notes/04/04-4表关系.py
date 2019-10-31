#_*_coding:utf-8_*_
"""
一对多：
应用场景：比如文章和作者之间的关系。一个文章只能由一个作者编写，但是一个作者可以写多篇文章。文章和作者之间的关系就是典型的多对一的关系。
实现方式：一对多或者多对一，都是通过ForeignKey来实现的。还是以文章和作者的案例进行讲解。
lass User(models.Model):
     username = models.CharField(max_length=20)
     password = models.CharField(max_length=100)

 class Article(models.Model):
     title = models.CharField(max_length=100)
     content = models.TextField()
     author = models.ForeignKey("User",on_delete=models.CASCADE)


那么以后在给Article对象指定author，就可以使用以下代码来完成：

article = Article(title='abc',content='123')
author = User(username='zhiliao',password='111111')
# 要先保存到数据库中
author.save()
article.author = author
article.save()



并且以后如果想要获取某个用户下所有的文章，可以通过article_set来实现。示例代码如下：
user = User.objects.first()
# 获取第一个用户写的所有文章
articles = user.article_set.all()
for article in articles:
    print(article)






多对多：
1.应用场景：比如文章和标签的关系。
一篇文章可以有多个标签，一个标签可以被多个文章所引用。
因此标签和文章的关系是典型的多对多的关系

2.实现方式：Django为这种多对多的实现提供了专门的Field。
叫做ManyToManyField。还是拿文章和标签为例进行讲解。示例代码如下：

class Article(models.Model):
     title = models.CharField(max_length=100)
     content = models.TextField()
     tags = models.ManyToManyField("Tag",related_name="articles")

class Tag(models.Model):
     name = models.CharField(max_length=50)


related_name和related_query_name：
还是以User和Article为例来进行说明。
如果一个article想要访问对应的作者，那么可以通过author来进行访问。
但是如果有一个user对象，想要通过这个user对象获取所有的文章，
该如何做呢？这时候可以通过user.article_set来访问，
这个名字的规律是模型名字小写_set。示例代码如下：
user = User.objects.get(name='张三')
user.article_set.all()

如果不想使用默认查询的名字可以使用related_name，反向引用的时候就可以使用
user.article.all()进行查询
如果不像使用反向引用那么可以指定related_name='+'

related_query_name
查询的时候：
users = User.objects.filter(article_title="abc")  article为模型类的名字
如果设置了related_name为articles则查询为：
users = User.objects.filter(artiles_title="abc")
可以通过related_query_name将查询的反转名字修改成其他的名字。比如article，
related_query_name = 'article1'
反向过滤查询的是时候使用一下代码：
users = User.objects.filter(article1_title='abc')


"""