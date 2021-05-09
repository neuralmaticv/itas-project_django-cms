from first_app.models import Post
from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from first_app import models
from .forms import postForm, editForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

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

def careersPage(request):
    return render(request, 'careers.html', {})

class blogView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-id']

class postDetailView(DetailView):
    model = Post
    template_name = 'blog_post.html'

class addPostView(CreateView):
    model = Post
    form_class = postForm
    template_name = 'blog_add_post.html'

class editPostView(UpdateView):
    model = Post
    form_class = editForm
    template_name = 'blog_edit_post.html'

class deletePostView(DeleteView):
    model = Post
    template_name = 'blog_delete_post.html'
    success_url = reverse_lazy('blog')

class userRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    