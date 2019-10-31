#_*_coding:utf-8_*_
"""
变量:
html中：
{{username}}
# views.py代码
def profile(request):
    return render(request,'profile.html',context={'username':'huangyong'})

1.if标签
if标签相当于Python中的if语句，有elif和else相对应，
但是所有的标签都需要用标签符号（{%%}）进行包裹。
if标签中可以使用==、!=、<、<=、>、>=、in、not in、is、is not等判断运算符。
示例代码如下：
{% if '张三' in person %}
    张三
{% else %}
    李四
{% endif %}

2.for...in...标签：for...in...类似于Python中的for...in...。
可以遍历列表、元组、字符串、字典等一切可以遍历的对象。
示例代码如下：
{% for person in persons %}
     <p>{{ person.name }}</p>
 {% endfor %}

如果想要反向遍历，那么在遍历的时候就加上一个reversed。
示例代码如下：
{% for person in persons reversed %}
     <p>{{ person.name }}</p>
 {% endfor %}

遍历字典的时候，需要使用items、keys和values等方法。
在DTL中，执行一个方法不能使用圆括号的形式。
遍历字典示例代码如下

 {% for key,value in person.items %}
     <p>key：{{ key }}</p>
     <p>value：{{ value }}</p>
 {% endfor %}


在for循环中，DTL提供了一些变量可供使用。这些变量如下：
    forloop.counter：当前循环的下标。以1作为起始值。
    forloop.counter0：当前循环的下标。以0作为起始值。
    forloop.revcounter：当前循环的反向下标值。比如列表有5个元素，那么第一次遍历这个属性是等于5，第二次是4，以此类推。并且是以1作为最后一个元素的下标。
    forloop.revcounter0：类似于forloop.revcounter。不同的是最后一个元素的下标是从0开始。
    forloop.first：是否是第一次遍历。
    forloop.last：是否是最后一次遍历。
    forloop.parentloop：如果有多个循环嵌套，那么这个属性代表的是上一级的for循环。


3.for...in...empty标签：这个标签使用跟for...in...是一样的，只不过是在遍历的对象如果没有元素的情况下，会执行empty中的内容。
示例代码如下：
{% for person in persons %}
     <li>{{ person }}</li>
 {% empty %}
     暂时还没有任何人
 {% endfor %}

4.with标签：在模版中定义变量。
有时候一个变量访问的时候比较复杂，那么可以先把这个复杂的变量缓存到一个变量上，以后就可以直接使用这个变量就可以了。
示例代码如下：
context = {
     "persons": ["张三","李四"]
 }
 {% with lisi=persons.1 %}
     <p>{{ lisi }}</p>
 {% endwith %}


有几点需要强烈的注意：

在with语句中定义的变量，只能在{%with%}{%endwith%}中使用，不能在这个标签外面使用。
定义变量的时候，不能在等号左右两边留有空格。比如{% with lisi = persons.1%}是错误的。
还有另外一种写法同样也是支持的：
  {% with persons.1 as lisi %}
      <p>{{ lisi }}</p>
  {% endwith %}

5.url标签
在模版中，我们经常要写一些url，比如某个a标签中需要定义href属性。
当然如果通过硬编码的方式直接将这个url写死在里面也是可以的。
但是这样对于以后项目维护可能不是一件好事。
因此建议使用这种反转的方式来实现，类似于django中的reverse一样。
示例代码如下：
<a href="{% url 'book:list' %}">图书列表页面</a>

如果url反转的时候需要传递参数，那么可以在后面传递。但是参数分位置参数和关键字参数。位置参数和关键字参数不能同时使用。
示例代码如下：
 # path部分
 path('detail/<book_id>/',views.book_detail,name='detail')
 # url反转，使用位置参数
 <a href="{% url 'book:detail' 1 %}">图书详情页面</a>
 # url反转，使用关键字参数
 <a href="{% url 'book:detail' book_id=1 %}">图书详情页面</a>
如果想要在使用url标签反转的时候要传递查询字符串的参数，那么必须要手动在在后面添加。示例代码如下：
<a href="{% url 'book:detail' book_id=1 %}?page=1">图书详情页面</a>
如果需要传递多个参数，那么通过空格的方式进行分隔。示例代码如下：
<a href="{% url 'book:detail' book_id=1 page=2 %}">图书详情页面</a>


6.spaceless标签：移除html标签中的空白字符。包括空格、tab键、换行等。
示例代码如下：
{% spaceless %}
     <p>
         <a href="foo/">Foo</a>
     </p>
 {% endspaceless %}

渲染后：
  <p><a href="foo/">Foo</a></p>
spaceless只会移除html标签之间的空白字符。而不会移除标签与文本之间的空白字符。


7.autoescape标签：开启和关闭这个标签内元素的自动转义功能。
自动转义是可以将一些特殊的字符。
比如<转义成html语法能识别的字符，比如<会被转义成&lt;，而>会被自动转义成&gt;。
模板中默认是已经开启了自动转义的。autoescape的
示例代码如下：
# 传递的上下文信息
 context = {
     "info":"<a href='www.baidu.com'>百度</a>"
 }

 # 模板中开启自动转义
 {% autoescape on %}
     {{ info }}
 {% endautoescape %}

  # 模板中关闭自动转义
 {% autoescape off %}
     {{ info }}
 {% endautoescape %}

 8.verbatim标签：默认在DTL模板中是会去解析那些特殊字符的。
 比如{%和%}以及{{等。如果你在某个代码片段中不想使用DTL的解析引擎。那么你可以把这个代码片段放在verbatim标签中。
 示例代码下：
 {% verbatim %}
     {{if dying}}Still alive.{{/if}}
 {% endverbatim %}
"""