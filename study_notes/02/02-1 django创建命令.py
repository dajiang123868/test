#_*_coding:utf-8_*_
"""
创建：
用命令行的方式：
创建项目：打开终端，使用命令：django-admin startproject [项目名称]即可创建。
比如：django-admin startproject first_project。
创建应用（app）：一个项目类似于是一个架子，但是真正起作用的还是app。
在终端进入到项目所在的路径，然后执行python manage.py startapp [app名称]创建一个app。

"""

"""
运行：
运行Django项目：
通过命令行的方式：python manage.py runserver。这样可以在本地访问你的网站，默认端口号是8000，这样就可以在浏览器中通过http://127.0.0.1:8000/来访问你的网站啦。如果想要修改端口号，那么在运行的时候可以指定端口号，python manage.py runserver 9000这样就可以通过9000端口来访问啦。另外，这样运行的项目只能在本机上能访问，如果想要在其他电脑上也能访问本网站，那么需要指定ip地址为0.0.0.0。示例为：python manage.py runserver 0.0.0.0:8000。
通过pycharm运行。直接点击右上角的绿色箭头按钮即可运行。

"""

"""
项目结构介绍：
    1>manage.py：以后和项目交互基本上都是基于这个文件。一般都是在终端输入python manage.py [子命令]。
    可以输入python manage.py help看下能做什么事情。除非你知道你自己在做什么，一般情况下不应该编辑这个文件。
    2>settings.py：本项目的设置项，以后所有和项目相关的配置都是放在这个里面。
    3>urls.py：这个文件是用来配置URL路由的。比如访问http://127.0.0.1/news/是访问新闻列表页，这些东西就需要在这个文件中完成。
    4>wsgi.py：项目与WSGI协议兼容的web服务器入口，部署的时候需要用到的，一般情况下也是不需要修改的。

"""

"""
project和app的关系：
app是django项目的组成部分。一个app代表项目中的一个模块，
所有URL请求的响应都是由app来处理。比如豆瓣，里面有图书，
电影，音乐，同城等许许多多的模块，如果站在django的角度来看，
图书，电影这些模块就是app，图书，电影这些app共同组成豆瓣这个项目。
因此这里要有一个概念，django项目由许多app组成，一个app可以被用到其他项目，django也能拥有不同的app。
"""