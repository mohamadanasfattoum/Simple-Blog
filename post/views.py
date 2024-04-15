from django.shortcuts import render , redirect
from .models import Post , Comment
from .form import PostForm
# redirect to go to another page

def post_list(request):
    posts_data = Post.objects.all()
    return render (request,'post_list.html', {'posts':posts_data})


def post_detail(request,post_id):
    post_data = Post.objects.get(id=post_id)
    comment_data = Comment.objects.filter(post=post_data) # used filter to just comment for the same post(post data in template = post_data)
    return render (request,'post_detail.html', {'post':post_data, 'comment':comment_data})
    

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('/posts/')

    else:
        form = PostForm()
    
    return render (request, 'add_post.html', {'form':form})



def edit_post(request, slug):
    post_data = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post_data)
        if form.is_valid():
            form.save()
            return redirect (f'/posts/{post_data.slug}')
    else:
        form = PostForm(instance=post_data) # we need instance to edit the same data 
    
    return render (request, 'post/edit_post.html', {'form':form})



def delete_post(request, post_id):
    post_data = Post.objects.get(id=post_id)
    post_data.delete()

    return redirect ('/posts/')


# L-13
# The Comment objects related to the post_data are retrieved and stored in the comment_data variable. 
# The filter method is used to retrieve only the comments associated with the same post.