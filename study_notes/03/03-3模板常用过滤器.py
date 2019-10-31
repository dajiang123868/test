#_*_coding:utf-8_*_
"""
1>add
传进来的参数添加到原来的值上面。这个过滤器会尝试将值和参数转换成整形然后进行相加。如果转换成整形过程中失败了，那么会将值和参数进行拼接。如果是字符串，那么会拼接成字符串，如果是列表，那么会拼接成一个列表。
示例代码如下：
{{ value|add:"2" }}
果value是等于4，那么结果将是6。如果value是等于一个普通的字符串，比如abc，那么结果将是abc2。add过滤器的
源代码如下：
def add(value, arg):
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''


2>cut
移除值中所有指定的字符串。类似于python中的replace(args,"")。示例代码如下：
{{ value|cut:" " }}
以上示例将会移除value中所有的空格字符。cut过滤器的源代码如下：
def cut(value, arg):
    safe = isinstance(value, SafeData)
    value = value.replace(arg, '')
    if safe and arg != ';':
        return mark_safe(value)
    return value

3>date
将一个日期按照指定的格式，格式化成字符串。示例代码如下：

# 数据
context = {
    "birthday": datetime.now()
}
# 模版
{{ birthday|date:"Y/m/d" }}

4>default
如果值被评估为False。比如[]，""，None，{}等这些在if判断中为False的值，都会使用default过滤器提供的默认值。
示例代码如下：
{{ value|default:"nothing" }}
如果value是等于一个空的字符串。比如""，那么以上代码将会输出nothing。


5>default_if_none
如果值是None，那么将会使用default_if_none提供的默认值。
这个和default有区别，default是所有被评估为False的都会使用默认值。
而default_if_none则只有这个值是等于None的时候才会使用默认值。
示例代码如下：
{{ value|default_if_none:"nothing" }}
如果value是等于""也即空字符串，那么以上会输出空字符串。
如果value是一个None值，以上代码才会输出nothing。

6>first
返回列表/元组/字符串中的第一个元素。示例代码如下：
{{ value|first }}
如果value是等于['a','b','c']，那么输出将会是a。

7>last
返回列表/元组/字符串中的最后一个元素。示例代码如下：
{{ value|last }}
如果value是等于['a','b','c']，那么输出将会是c。

8>join
类似与Python中的join，将列表/元组/字符串用指定的字符进行拼接。
示例代码如下：
{{ value|join:"/" }}

9>length
获取一个列表/元组/字符串/字典的长度。示例代码如下：
{{ value|length }}

10>lower
将值中所有的字符全部转换成小写。示例代码如下：
{{ value|lower }}
如果value是等于Hello World。那么以上代码将输出hello world。

11>upper
类似于lower，只不过是将指定的字符串全部转换成大写。


12>random
在被给的列表/字符串/元组中随机的选择一个值。示例代码如下：
{{ value|random }}
如果value是等于['a','b','c']，那么以上代码会在列表中随机选择一个。

13>safe
标记一个字符串是安全的。也即会关掉这个字符串的自动转义。示例代码如下：
{{value|safe}}
如果value是一个不包含任何特殊字符的字符串，比如<a>这种，那么以上代码就会把字符串正常的输入。
如果value是一串html代码，那么以上代码将会把这个html代码渲染到浏览器中。


14>slice
类似于Python中的切片操作。示例代码如下：
{{ some_list|slice:"2:" }}
以上代码将会给some_list从2开始做切片操作。

15>stringtags
删除字符串中所有的html标签。示例代码如下：
{{ value|striptags }}
如果value是<strong>hello world</strong>，那么以上代码将会输出hello world。


16>truncatechars
如果给定的字符串长度超过了过滤器指定的长度。那么就会进行切割，并且会拼接三个点来作为省略号。示例代码如下：
{{ value|truncatechars:5 }}
如果value是等于北京欢迎您~，那么输出的结果是北京...。
可能你会想，为什么不会北京欢迎您...呢。
因为三个点也占了三个字符，所以北京+三个点的字符长度就是5

17>truncatechars_html
类似于truncatechars，只不过是不会切割html标签。示例代码如下：
{{ value|truncatechars:5 }}
如果value是等于<p>北京欢迎您~</p>，那么输出将是<p>北京...</p>。

"""""


"""
自定义时间计算过滤器：
有时候经常会在朋友圈、微博中可以看到一条信息发表的时间，并不是具体的时间，而是距离现在多久。
比如刚刚，1分钟前等。这个功能DTL是没有内置这样的过滤器的，因此我们可以自定义一个这样的过滤器。
示例代码如下：
rom datetime import datetime
from django import template
register = template.Library()
def time_since(value):
    if isinstance(value,datetime):
        now = datetime.now()
        timestamp = (now - value).total_seconds()
        if timestamp < 60:
            return "刚刚"
        elif timestamp >= 60 and timestamp < 60*60:
            minutes = int(timestamp / 60)
            return "%s分钟前" % minutes
        elif timestamp >= 60*60 and timestamp < 60*60*24:
            hours = int(timestamp / (60*60))
            return "%s小时前" % hours
        elif timestamp >= 60*60*24 and timestamp < 60*60*24*30:
            days = int(timestamp / (60*60*24))
            return "%s天前" % days
        else:
            return value.strftime("%Y/%m/%d %H:%M")
    else:
        return value
register.filter("time_since",time_since)


在模版中使用的示例代码如下：

{% load time_filter %}
...
{% value|time_since %}
...



为了更加方便的将函数注册到模版库中当作过滤器。也可以使用装饰器来将一个函数包装成过滤器。
示例代码如下：
from django import template
register = template.Library()

@register.filter(name='mycut')
def mycut(value,mystr):
    return value.replace(mystr,"")
"""