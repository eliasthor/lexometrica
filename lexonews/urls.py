from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('article/drafts/', views.drafts, name='drafts'),
    path('article/<int:pk>/', views.single_article, name='single_article'),
    path('article/new/', views.new_article, name='new_article'),
    path('article/<int:pk>/edit/', views.edit_article, name='edit_article'),
    path('article/<int:pk>/publish/', views.publish_article, name='publish_article'),
    path('article/<int:pk>/remove/', views.remove_article, name='remove_article'),
]
