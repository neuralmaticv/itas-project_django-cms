from first_app.models import Post
from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from .models import Post
from first_app import models

# Create your views here.
def homePage(request):
    return render(request, 'main.html', {})

def aboutPage(request):
    return render(request, 'about.html', {})

def contactPage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject + " | from user " + name, # subject
            message,                    # message
            email,                      # from email
            ['vladocodes@gmail.com'],   # to email
        )

        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})

"""
def blogPage(request):
    return render(request, 'blog.html', {})
"""

class blogView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-id']

class postDetailView(DetailView):
    model = Post
    template_name = 'blog_post.html'

def careersPage(request):
    return render(request, 'careers.html', {})
