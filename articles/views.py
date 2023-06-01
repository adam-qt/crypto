from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .utils import parse_articles
from django.views.generic import ListView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'data'


def update(request):
    parse_articles()
    return HttpResponseRedirect(reverse('articles:articles'))


