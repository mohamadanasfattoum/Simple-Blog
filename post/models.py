from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Post(models.Model):
    POST_TYPE_CHOICES = (
        ('question','سؤال'),
        ('post','منشور'),
        ('article','مقالة'),
    )

    p_type =  models.CharField(max_length=500, choices=POST_TYPE_CHOICES, verbose_name='نوع المنشور')
    title =  models.CharField(max_length=500, verbose_name='عنوان المنشور')
    content = models.TextField(max_length=1000, verbose_name='محتوى المنشور')
    likes = models.IntegerField ( default=0 , verbose_name='الاعجاب')
    dislikes = models.IntegerField ( default=0 , verbose_name='عدم الاعجاب')
    date = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User, related_name='post_auther', on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()
    image = models.ImageField(upload_to= 'posts', null=True, verbose_name='الصورة')

    class Meta:
        verbose_name = 'المنشور'
        verbose_name_plural = 'المنشورات'


    def __str__(self):
         return self.title


class Comment(models.Model):
    auther = models.ForeignKey(User, related_name='comment_auther', on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='المنشور')
    comment = models.TextField(max_length=1000, verbose_name='التعليق')
    date = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name = 'التعليق'
        verbose_name_plural = 'التعليقات'

    