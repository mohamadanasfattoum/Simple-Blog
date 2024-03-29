from django.db import models



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

    class Meta:
        verbose_name = 'المنشور'
        verbose_name_plural = 'المنشورات'


    def __str__(self):
         return self.title

    