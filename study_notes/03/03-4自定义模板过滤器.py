#_*_coding:utf-8_*_
"""
在创建了存储过滤器的文件后，接下来就是在这个文件中写过滤器了。
过滤器实际上就是python中的一个函数，只不过是把这个函数注册到模板库中，以后在模板中就可以使用这个函数了。
但是这个函数的参数有限制，第一个参数必须是这个过滤器需要处理的值，第二个参数可有可无，
如果有，那么就意味着在模板中可以传递参数。
并且过滤器的函数最多只能有两个参数。在写完过滤器后，
再使用django.template.Library对象注册进去。
示例代码如下：
    from django import template
    # 创建模板库对象
    register = template.Library()
    # 过滤器函数
    def mycut(value,mystr):
        return value.replace(mystr)
    # 将函数注册到模板库中
    register.filter("mycut",mycut)


"""