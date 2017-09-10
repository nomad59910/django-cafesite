from django.conf.urls import url
from .views import ShowBasketView, OrderCompletedView


app_name = 'basket'

urlpatterns = [
    url(r'^completed/$', OrderCompletedView.as_view(), name="success-order"),
    url(r'^$', ShowBasketView.as_view(), name="ordering"),
]
