from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify


class Post(models.Model):
    POST_TYPE_CHOICES = (
        ('question','Question'),
        ('post','Post'),
        ('article','Article'),
    )

    p_type =  models.CharField(max_length=500, choices=POST_TYPE_CHOICES, verbose_name='نوع المنشور')
    title =  models.CharField(max_length=500, verbose_name='Title')
    content = models.TextField(max_length=1000, verbose_name='content')
    date = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User, related_name='post_auther', on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()
    image = models.ImageField(upload_to= 'post', null=True, verbose_name='Image')
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    def __str__(self):
         return self.title

    def save(self, *args, **kwargs):
       self.slug = slugify(self.title)
       super(Post, self).save(*args, **kwargs) # Call the real save() method

class Comment(models.Model):
    auther = models.ForeignKey(User, related_name='comment_auther', on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, related_name='comment_post', on_delete=models.CASCADE, verbose_name='Post')
    comment = models.TextField(max_length=1000, verbose_name='Comment')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
         return str(self.post)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    