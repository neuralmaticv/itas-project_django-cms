from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 60)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank = True, null = True)
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title + ' : ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog_post', args=(str(self.id)))
