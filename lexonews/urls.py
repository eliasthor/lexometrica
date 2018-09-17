from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('article/<int:pk>/', views.single_article, name='single_article'),
    path('article/new/', views.new_article, name='new_article'),
]
