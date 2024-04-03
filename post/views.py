from django.shortcuts import render
from .models import Post
def post_list(request):
    posts_data = Post.objects.all()
    return render (request,'post_list.html', {'posts':posts_data})


def post_detail(request,post_id):
    post_data = Post.objects.get(id=post_id)
    return render (request,'post_detail.html', {'post':post_data})
    