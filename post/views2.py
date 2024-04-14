# start with generic  classs

from django.views.generic import *
from django.urls import reverse
from .models import Post, Comment
from django.utils.text import slugify

# ListView, DetailView, CreateView, UpdateView,  DeleteView


class PostList(ListView):
    model = Post
    template_name = "post_list.html"


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comment = post.comment_post.all()
        context['comment'] = comment
        return context
    


class CreatePost(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/posts/'


class UpdatePost(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'post/edit_post.html'
    # success_url = '/posts/{pk}'
    def get_success_url(self):
        # Retrieve the object being updated
        obj = self.get_object()
        slug = slugify(obj.title)  # Generate the slug using the post title
        
        # Return the URL with the pk parameter
        return reverse('post_detail', kwargs={'slug':slug})


class DeletePost(DeleteView):
    model = Post
    fields = '__all__'
    success_url = '/posts/'

        