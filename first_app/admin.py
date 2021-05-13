from django.contrib import admin
from .models import Category, Post, CareersPost

myModels = [Post, CareersPost, Category]

admin.site.register(myModels)
