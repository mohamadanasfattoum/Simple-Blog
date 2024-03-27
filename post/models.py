from django.db import models



class Post(models.Model):
    POST_TYPE_CHOICES = (
        ('question','سؤال'),
        ('post','منشور'),
        ('article','مقالة'),
    )

    p_type =  models.CharField(max_length=500, choices=POST_TYPE_CHOICES, verbose_name='نوع ااماشور')