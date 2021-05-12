from django.contrib import admin
from .models import Post, CareersPost

myModels = [Post, CareersPost]

admin.site.register(myModels)
