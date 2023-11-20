from django.shortcuts import render , redirect
from .models import Posts

from .forms import PostForm
# Create your views here.


def creatpost(request):

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/posts/')
    else:
        form = PostForm
    return render(request,'posts/new.html',{'form':form})


""" def post_list(request):

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
 """


from django.views.generic import ListView , DetailView


class PostList(ListView):
    model = Posts


class PostDetail(DetailView):

    model = Posts