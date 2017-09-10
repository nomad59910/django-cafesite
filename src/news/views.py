from .models import Article
from django.shortcuts import render_to_response
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView


class ArticleDetailView(DetailView):
    template_name = 'news/new.html'
    model = Article
    pk_url_kwarg = 'id'


class ArticleListView(TemplateView):
    template_name = 'news/news.html'
