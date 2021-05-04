from django.urls import path
from . import views

urlpatterns = [
    path('',  views.homePage, name = 'home'), 
    path('about/',  views.aboutPage, name = 'about'), 
    path('contact/',  views.contactPage, name = 'contact'), 
    path('blog/',  views.blogPage, name = 'blog'), 
    path('careers/',  views.careersPage, name = 'careers'), 
]
