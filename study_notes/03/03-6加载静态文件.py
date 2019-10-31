#_*_coding:utf-8_*_
"""
使用static标签来加载静态文件。
要使用static标签，首先需要{% load static %}
加载静态文件的步骤如下：
1.首先确保django.contrib.staticfiles已经添加到settings.INSTALLED_APPS中。
2.确保在settings.py中设置了STATIC_URL。
3.在已经安装了的app下创建一个文件夹叫做static，然后再在这个static文件夹下创建一个当前app的名字的文件夹，再把静态文件放到这个文件夹下。
4.如果有一些静态文件是不和任何app挂钩的。那么可以在settings.py中添加STATICFILES_DIRS，以后DTL就会在这个列表的路径中查找静态文件。比如可以设置为:
 STATICFILES_DIRS = [
     os.path.join(BASE_DIR,"static")
 ]
5.在模版中使用load标签加载static标签。比如要加载在项目的static文件夹下的style.css的文件。
那么示例代码如下：
{% load static %}
 <link rel="stylesheet" href="{% static 'style.css' %}">

6.如果不想每次在模版中加载静态文件都使用load加载static标签，
那么可以在settings.py中的TEMPLATES/OPTIONS添加
'builtins':['django.templatetags.static']，
这样以后在模版中就可以直接使用static标签，而不用手动的load了。

7.如果没有在settings.INSTALLED_APPS中添加django.contrib.staticfiles。
那么我们就需要手动的将请求静态文件的url与静态文件的路径进行映射了。
示例代码如下：
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 其他的url映射
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""