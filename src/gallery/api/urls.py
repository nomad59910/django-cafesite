from django.conf.urls import url
from .api import SliderListAPI


urlpatterns = [
    url(r'^list/$', SliderListAPI.as_view()),
]
