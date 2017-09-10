from django.conf.urls import url
from django.contrib import admin
import product.views
from .views import MenuView


app_name = 'menu'

urlpatterns = [
    url(r'^$', MenuView.as_view(), name="menu"),
]
