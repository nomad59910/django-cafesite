from django.conf.urls import url
from .api import DishAPIView, TasksListAPIView, DishsListAPIView


urlpatterns = [
    url(r'^dish/(?P<id>[0-9]+)/$', DishAPIView.as_view()),
    url(r'^dish/list/$', DishsListAPIView.as_view()),
    url(r'^task/list/$', TasksListAPIView.as_view()),
]
