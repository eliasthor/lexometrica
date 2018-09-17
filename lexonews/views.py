from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Article

def articles(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'lexonews/articles.html', {'articles': articles})

def single_article(request, pk):
   article = get_object_or_404(Article, pk=pk)
   return render(request, 'lexonews/single_article.html', {'article': article})
