from django.shortcuts import render , redirect
from .models import Posts , Comment
from .forms import PostForm , CommentForm
# Create your views here.


def creatpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.auther = request.user
            myform.save()
            return redirect('/posts/')
    else:
        form = PostForm
    return render(request,'posts/posts_form.html',{'form':form})

def Editpost(request,pk):
    post = Posts.objects.get(id=pk )
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.auther = request.user
            myform.save()
            return redirect('/posts/')
    else:
        form = PostForm(instance=post)
    return render(request,'posts/edit.html',{'form':form})


def deletePost(request,pk):
    post = Posts.objects.get(id=pk)
    if request.method == 'POST':
      post.delete()
      return redirect('/posts/')
    return render(request,'posts/posts_confirm_delete.html',{'post':post})
    


def post_list(request):
    data = Posts.objects.all() # هنا قمنا بانشاء نسخة من الكلاس ونجلب جميع البيانات في لست
    context = {
    'ali': data
    }
    return render(request,'posts/posts_list.html',context)


def post_detail(request,pk):
    data = Posts.objects.get(id=pk )
    comments = Comment.objects.filter(post=data)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.post = data
            myform.save()

    else:
        form = CommentForm()

    context = {
        'post': data ,
        'comments': comments ,
        'form' : form
    }
    return render(request,'posts/posts_detail.html',context)






