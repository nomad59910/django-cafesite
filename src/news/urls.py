from django.conf.urls import url
from news.views import ArticleDetailView, ArticleListView


app_name = 'news'

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name="article-list"),
    url(r'^(?P<id>[0-9]+)/$', ArticleDetailView.as_view(), name="article"),
]
