from django.urls import path
from . import views
#from .views import blogView

urlpatterns = [
    path('',  views.homePage, name = 'home'), 
    path('about/',  views.aboutPage, name = 'about'), 
    path('contact/',  views.contactPage, name = 'contact'), 
    # path('blog/',  views.blogPage, name = 'blog'), 
    path('blog/', views.blogView.as_view(), name='blog'),
    path('blog/post/<int:pk>', views.postDetailView.as_view(), name='blog_post'),
    path('blog/add_post/', views.addPostView.as_view(), name='add_post'),
    path('blog/edit_post/<int:pk>', views.editPostView.as_view(), name='edit_post'),
    path('blog/<int:pk>/delete', views.deletePostView.as_view(), name='delete_post'),
    path('careers/',  views.careersPage, name = 'careers'), 
]
