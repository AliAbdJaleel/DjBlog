from django.shortcuts import render
from .models import Posts
# Create your views here.


def post_list(request):

    data = Posts.objects.all() # هنا قمنا بانشاء نسخة من الكلاس ونجلب جميع البيانات في لست
    context = {
    'ali': data
    }
    return render(request,'posts/post_list.html',context)


def post_detail(request,post_id):
    data = Posts.objects.get(id=post_id )

    context = {
        'post': data
    }
    return render(request,'posts/post_detail.html',context)
