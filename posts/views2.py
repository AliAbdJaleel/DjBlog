


from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView

from .models import Posts

class PostList(ListView):
    model = Posts


class PostDetail(DetailView):

    model = Posts




class PostCreate(CreateView):
    model = Posts
    fields = '__all__'
    success_url = '/posts/'

class EditPost(UpdateView):
    model = Posts
    fields = '__all__'
    success_url = '/posts/'
    template_name = 'posts/edit.html'

class DeletePost(DeleteView):
    model = Posts
    success_url = '/posts/'