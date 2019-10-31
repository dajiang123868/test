#_*_coding:utf-8_*_
"""
渲染模板的方式：
    1>render_to_string：
    找到模板，然后将模板编译后渲染成Python的字符串格式。
    最后再通过HttpResponse类包装成一个HttpResponse对象返回回去。
    示例代码如下：
     from django.template.loader import render_to_string
     from django.http import HttpResponse
     html = render_to_string("detail.html")
     return HttpResponse(html)

    2>render:
    直接将模板渲染成字符串和包装成HttpResponse对象一步到位完成。
    示例代码如下：
    from django.shortcuts import render
    def book_list(request):
     return render(request,'list.html')


"""

"""
模板查找路径配置:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


DIRS：这是一个列表，在这个列表中可以存放所有的模板路径，以后在视图中使用render或者render_to_string渲染模板的时候，会在这个列表的路径中查找模板。
APP_DIRS：默认为True，这个设置为True后，会在INSTALLED_APPS的安装了的APP下的templates文件加中查找模板。
查找顺序：比如代码render('list.html')。
    1>先会在DIRS这个列表中依次查找路径下有没有这个模板，如果有，就返回。
    2>如果DIRS列表中所有的路径都没有找到，那么会先检查当前这个视图所处的app是否已经安装，如果已经安装了，那么就先在当前这个app下的templates文件夹中查找模板，如果没有找到，那么会在其他已经安装了的app中查找。
    3>如果所有路径下都没有找到，那么会抛出一个TemplateDoesNotExist的异常。


"""