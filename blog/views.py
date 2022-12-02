from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.

def listArticle(request):
    articles = Article.objects.filter(published = True)
    return render(request, 'blog/list_article.html', {"articles":articles})

def detailArticle(request, id):
    article = get_object_or_404(Article,pk = id, published =True )
    return render(request, 'blog/detail_article.html', {"article":article})