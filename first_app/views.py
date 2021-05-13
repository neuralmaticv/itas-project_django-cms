from typing import List, cast
from first_app.models import Post
from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CareersPost, Category, Post
from first_app import models
from .forms import postForm, editForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


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


class careersView(ListView):
    model = CareersPost
    template_name = 'careers.html'
    ordering = ['-id']


class careersDetailView(DetailView):
    model = CareersPost
    template_name = 'careers_post.html'
    

class blogView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()[:5]
        context = super(blogView, self).get_context_data(*args, **kwargs)
        context["cat_list"] = cat_list
        return context


class blogCatsView(ListView):
    model = Category
    template_name = 'blog_cats.html'


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


def categoryView(request, categories):
    cats = categories.replace('-', ' ')
    category_posts = Post.objects.filter(category = cats)
    context = {'categories': cats, 'category_posts': category_posts}
    return render(request, 'categories.html', context)


class userRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    