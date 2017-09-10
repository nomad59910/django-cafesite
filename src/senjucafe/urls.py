from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render_to_response
from rest_framework.urlpatterns import format_suffix_patterns
from .views import set_language, IndexView
import django.conf.urls.i18n



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^setlang/$', set_language),
    url(r'^redactor/', include('redactor.urls')),

    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^menu/', include('product.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^basket/', include('basket.urls')),

    url(r'^api/news/', include('news.api.urls')),
    url(r'^api/slider/', include('gallery.api.urls')),
    url(r'^api/basket/', include('basket.api.urls')),
    url(r'^api/product/', include('product.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = format_suffix_patterns(urlpatterns)
