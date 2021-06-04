from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog')


class Post(models.Model):
    title = models.CharField(max_length = 60)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = RichTextField(blank = True, null = True)
    date = models.DateField(auto_now_add = True)
    category = models.CharField(max_length = 30, default = 'uncategorized')

    def __str__(self):
        return self.title + ' : ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog')


class CareersPost(models.Model):
    title = models.CharField(max_length = 80)
    location = models.CharField(max_length = 50, default = "location")
    profession = models.CharField(max_length = 30, default = "profession")
    employmentType = models.CharField(max_length = 30, default = "employment type")
    date = models.DateField(auto_now_add = True)
    body = RichTextField(blank = True, null = True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = "comments", on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
