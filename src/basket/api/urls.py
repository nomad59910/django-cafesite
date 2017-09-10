from django.conf.urls import url
from .api import *


urlpatterns = [
    url(r'^cart/add/$', AddProductAPIView.as_view()),
    url(r'^cart/set/$', SetProductAPIView.as_view()),
    url(r'^cart/remove/$', RemoveProductAPIView.as_view()),
    url(r'^cart/get/$', GetDataBasket.as_view()),
]
