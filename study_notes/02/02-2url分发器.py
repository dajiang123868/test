#_*_coding:utf-8_*_
"""
URL中包含另外一个urls模块，抽离URL模块中的代码，解耦代码
通过include函数来实现
from django.urls import path,include
path('book/',include("book.urls"))
其中book为一个app，将book/这样的url都分发到book下的urls模块中
urls模块中：
urlpatterns = [
    path('list/',views.book_list),
    path('detail/<book_id>/',views.book_detail)
]

指定命名空间：
from django.urls import path,include
urlpatterns = [
    path('movie/',include('movie.urls',namespace='movie'))
]


后在movie/urls.py中指定应用命名空间。实例代码如下
app_name = 'movie'

"""


"""
re_path函数
    需要用到正则来匹配url的时候，使用的函数
     from django.urls import path, re_path
     urlpatterns = [
        path('articles/2003/', views.special_case_2003),
        re_path(r'articles/(?P<year>[0-9]{4})/', views.year_archive),
        re_path(r'articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.month_archive),
        re_path(r'articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-_]+)/', views.article_detail),
    ]

"""


"""
url参数
1>
    from django.urls import path
    path('book/<book_id>/',views.book_detail)  book_id为字符串

2>
    通过查询字符串传递
    path('book/detail/',views.book_detail)
    /book/detail/?id=1
    view视图中 book_id = request.GET.get("id") 可得到参数
    
3>
    定义传参类型,使用django自带url转换器或者自定义转换器
    urlpatterns = [
        path('articles/<int:year>/', views.special_case_2003),
        # 使用注册的转换器
        path('articles/<yyyy:year>/', views.year_archive),
        ...
    ]
    

"""


"""
url反转
    1>reverse("list") 对应url：/book/list/
    2>如果有应用命名空间或者有实例命名空间，那么应该在反转的时候加上命名空间。示例代码如下
        reverse('book:list')   /book/list/
    3>如果这个url中需要传递参数，那么可以通过kwargs来传递参数。示例代码如下：
        reverse("book:detail",kwargs={"book_id":1})  对应url:/book/detail/1
    4>反转的时候添加查询字符串的参数
    ogin_url = reverse('login') + "?next=/"

"""

"""
自定义url转换器
 # 1. 定义一个类
    class FourDigitYearConverter:
        # 2. 定义一个正则表达式
        regex = '[0-9]{4}'

        # 3. 定义to_python方法
        def to_python(self, value):
            return int(value)

        # 4. 定义to_url方法
        def to_url(self, value):
            return '%04d' % value     

    # 5. 注册到django中
    from django.urls import register_converter
    register_converter(converters.FourDigitYearConverter, 'yyyy')
    urlpatterns = [
        path('articles/2003/', views.special_case_2003),
        # 使用注册的转换器
        path('articles/<yyyy:year>/', views.year_archive),
        ...
    ]

"""