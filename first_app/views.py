from django.db.models import Q
from first_app.models import Post
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CareersPost, Category, Comment, Post
from .forms import postForm, editForm, commentForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


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

        email = EmailMessage(
            subject + " | from user " + name, # subject
            message,                    # message
            email,                      # from email
            ['vladocodes@gmail.com'],   # to email
            reply_to = [email],
        )

        email.send()

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

    def get_queryset(self):
        object_list = Post.objects.all()
        query = self.request.GET.get('search')
        
        if query:
            object_list = object_list.filter(
                Q(title__contains = query) | 
                Q(body__contains = query))
        
        return object_list.order_by('-id')


class blogCatsView(ListView):
    model = Category
    template_name = 'blog_cats.html'


class postDetailView(DetailView):
    model = Post
    template_name = 'blog_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = commentForm()

        return context

    def post(self, request, *args, **kwargs):
        try: 
            validate_email(request.POST.get('email'))
            new_comment = Comment(name = self.request.POST.get('name'),
                        body = request.POST.get('body'),     
                        email = request.POST.get('email'),
                        post = self.get_object())
            new_comment.save()
        except ValidationError:
            new_comment = None

        return self.get(self, request, *args, **kwargs)  
 

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
    category_posts = Post.objects.filter(category = cats).order_by('-id')
    context = {'categories': cats, 'category_posts': category_posts}
    return render(request, 'categories.html', context)


class userRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
