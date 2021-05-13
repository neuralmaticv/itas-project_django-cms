from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Category, Post

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for i in choices:
    choice_list.append(i)

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'add-post-form'}),
            'author': forms.Select(attrs={'class': 'add-post-form'}),
            'category': forms.Select(choices = choice_list, attrs={'class': 'add-post-form'}),
            'body': forms.Textarea(attrs={'class': 'add-post-form'}),
        }

class editForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'add-post-form'}),
            'category': forms.Select(choices = choice_list, attrs={'class': 'add-post-form'}),
            'body': forms.Textarea(attrs={'class': 'add-post-form'}),
        }
