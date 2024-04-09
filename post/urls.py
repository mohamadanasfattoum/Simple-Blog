from django.urls import path
from .views import post_list, post_detail, add_post, edit_post, delete_post
from .views2 import PostList, PostDetail, CreatePost, UpdatePost


urlpatterns = [
    #path('posts/',post_list), # views.py
    path('posts/',PostList.as_view()),

    # path('posts/add',add_post), 
    path('posts/add',CreatePost.as_view()),

    # path('posts/<int:post_id>',PostDetail), # views.py
    path('posts/<int:pk>',PostDetail.as_view(), name='post_detail'), # pk oder slug

    # path('posts/<int:post_id>/edit',edit_post),
    path('posts/<int:pk>/edit',UpdatePost.as_view()),


    path('posts/<int:post_id>/delete',delete_post)
]