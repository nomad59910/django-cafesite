from django.conf.urls import url
from .api import ArticleAPI, ArticleListAPI


urlpatterns = [
    url(r'^list/$', ArticleListAPI.as_view()),
    url(r'^(?P<id>[0-9]+)/$', ArticleAPI.as_view()),
]
