from django.urls import path, re_path
from .views import listArticle, detailArticle


urlpatterns =[
    path('',listArticle, name = 'list_articles' ),
    path('articles/<int:id>',detailArticle, name = 'detail_article' ),
]