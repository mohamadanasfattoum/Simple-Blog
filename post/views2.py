# start with generic  classs

from django.views.generic import *
from .models import Post

# ListView, DetailView, CreateView, UpdateView,  DeleteView


class PostList(ListView):
    model = Post
    template_name = "post_list.html"


class PostDetail(DetailView):
    model = Post
    


class CreatePost(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/posts/'
