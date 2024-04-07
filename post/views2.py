# start with generic  classs

from django.views.generic import *
from .models import Post



class PostList(ListView):
    model = Post
    template_name = "post_list.html"

