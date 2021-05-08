from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Post

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'add-post-form'}),
            'author': forms.Select(attrs={'class': 'add-post-form'}),
            'body': forms.Textarea(attrs={'class': 'add-post-form'}),
        }

class editForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'add-post-form'}),
            'body': forms.Textarea(attrs={'class': 'add-post-form'}),
        }
