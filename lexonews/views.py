from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Article
from .forms import ArticleForm

def articles(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'lexonews/articles.html', {'articles': articles})

def single_article(request, pk):
   article = get_object_or_404(Article, pk=pk)
   return render(request, 'lexonews/single_article.html', {'article': article})

def new_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('single_article', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'lexonews/edit_article.html', {'form': form})

def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('single_article', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'lexonews/edit_article.html', {'form': form})
