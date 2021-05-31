from django.contrib import admin
from .models import Category, Post, CareersPost, Comment

myModels = [Post, CareersPost, Category, Comment]

admin.site.register(myModels)
