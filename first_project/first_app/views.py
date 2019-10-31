from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import reverse


def book_detail(request):
    book_id = request.GET.get('id')
    print(type(book_id))
    text = "您输入的书籍id是：%s"%book_id
    return HttpResponse(text)


def book_list(request):
    text = "三国演义\n水浒传\n西游记\n红楼梦"
    return HttpResponse(text)


def books(request,page=0):
    # 默认第一页
    book_list = [
        '三国演义',
        '水浒传',
        '西游记',
        '红楼梦'
    ]
    return HttpResponse(book_list[page])

def index(request):
    return HttpResponse('这是主页')

def article_list(request,categories):
    print("categories:%s"%categories)
    print(reverse('book:list',kwargs={"categories":categories}))
    text = '您填写的分类是：%s' % categories
    return HttpResponse(text)