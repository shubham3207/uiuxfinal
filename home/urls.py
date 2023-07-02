
from django.urls import path
from .views import *
from . import views
urlpatterns = [
path('',homepage,name='home'),
path('login/',login_view,name='login'),
path('register/',register_view,name='register'),
path('blog_single/<int:id>', blog_single, name='blog_single'),
path('contact',contact,name='contact'),
path('about',about,name='about'),
path('category/<str:category_name>/', views.category_view, name='category_view'),
path('search/', views.search_view, name='search'),
]