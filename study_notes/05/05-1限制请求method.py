#_*_coding:utf-8_*_
"""
限制请求装饰器
django.http.decorators.http.require_http_methods：
这个装饰器需要传递一个允许访问的方法的列表。
比如只能通过GET的方式访问。那么示例代码如下：
from django.views.decorators.http import require_http_methods
 @require_http_methods(["GET"])
 def my_view(request):
     pass

django.views.decorators.http.require_GET：这个装饰器相当于是require_http_methods(['GET'])的简写形式，只允许使用GET的method来访问视图。示例代码如下：
 from django.views.decorators.http import require_GET
 @require_GET
 def my_view(request):
     pass


django.views.decorators.http.require_POST：这个装饰器相当于是require_http_methods(['POST'])的简写形式，只允许使用POST的method来访问视图。示例代码如下：
 from django.views.decorators.http import require_POST
 @require_POST
 def my_view(request):
     pass

django.views.decorators.http.require_safe：这个装饰器相当于是require_http_methods(['GET','HEAD'])的简写形式，只允许使用相对安全的方式来访问视图。因为GET和HEAD不会对服务器产生增删改的行为。因此是一种相对安全的请求方式。示例代码如下：
 from django.views.decorators.http import require_safe
 @require_safe
 def my_view(request):
     pass

"""



"""
重定向

永久性重定向：http的状态码是301，多用于旧网址被废弃了要转到一个新的网址确保用户的访问，最经典的就是京东网站，你输入www.jingdong.com的时候，会被重定向到www.jd.com，因为jingdong.com这个网址已经被废弃了，被改成jd.com，所以这种情况下应该用永久重定向。

暂时性重定向：http的状态码是302，表示页面的暂时性跳转。比如访问一个需要权限的网址，如果当前用户没有登录，应该重定向到登录页面，这种情况下，应该用暂时性重定向。



在Django中，重定向是使用redirect(to, *args, permanent=False, **kwargs)来实现的。to是一个url，permanent代表的是这个重定向是否是一个永久的重定向，默认是False。关于重定向的使用。请看以下例子：
from django.shortcuts import reverse,redirect
def profile(request):
    if request.GET.get("username"):
        return HttpResponse("%s，欢迎来到个人中心页面！")
    else:
        return redirect(reverse("user:login"))

"""