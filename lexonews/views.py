from django.shortcuts import render
from django.utils import timezone
from .models import Article

def articles(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'lexonews/articles.html', {'articles': articles})
