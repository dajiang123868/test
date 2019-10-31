#_*_coding:utf-8_*_
from django.urls import path,re_path
from . import views
app_name = 'book'
from django.urls import converters,register_converter

class CategoryConverter(object):
    regex = r'\w+|(\w+\+\w+)+'

    def to_python(self,value):
        """
        返回视图函数
        :param value:
        :return:
        """
        # python+django+flask
        # ['python','django','flask']
        result = value.split("+")
        return result

    def to_url(self,value):
        """
        返回反转
        :param value:
        :return:
        """
        # value：['python','django','flask']
        # python+django+flask
        if isinstance(value,list):
            result = "+".join(value)
            return result
        else:
            raise RuntimeError("转换url的时候，分类参数必须为列表！")
register_converter(CategoryConverter,'cate')

urlpatterns = [
    path('', views.index),
    path('list/',views.book_list),
    path('detail/<book_id>/',views.book_detail),
    path('page/', views.books),
    path('page/<int:page>/',views.books),
    re_path(r'list/(?P<categories>\w+|(\w+\+\w+)+)/',views.article_list),
    path("list/<cate:categories>/", views.article_list, name='list'),

]
