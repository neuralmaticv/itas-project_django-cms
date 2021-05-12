from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length = 60)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = RichTextField(blank = True, null = True)
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title + ' : ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog')


class CareersPost(models.Model):
    title = models.CharField(max_length = 80)
    location = models.CharField(max_length = 50, default = "Banja Luka")
    profession = models.CharField(max_length = 30, default = "Engineer")
    employmentType = models.CharField(max_length = 30, default = "Full-Time")
    date = models.DateField(auto_now_add = True)
    body = RichTextField(blank = True, null = True)

    def __str__(self):
        return self.title
