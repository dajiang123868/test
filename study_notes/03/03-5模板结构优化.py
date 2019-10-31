#_*_coding:utf-8_*_
"""
引入模版:
{% include 'header.html' %}  header.html为被引入文件名

include标签寻找路径的方式。也是跟render渲染模板的函数是一样的。
默认include标签包含模版，会自动的使用主模版中的上下文，也即可以自动的使用主模版中的变量。如果想传入一些其他的参数，那么可以使用with语句。示例代码如下：
# header.html
<p>用户名：{{ username }}</p>
# main.html
{% include "header.html" with username='huangyong' %}




模板继承：
{% block name %}  {% endblock %} 定义模板快
{{ block.super }} 继承模板块
{% extends "base.html" %} base.html为被继承的模板
需要注意的是：extends标签必须放在模版的第一行。
子模板中的代码必须放在block中，否则将不会被渲染。



"""