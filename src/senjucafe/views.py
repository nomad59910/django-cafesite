from django.shortcuts import render_to_response
from django.template import RequestContext
import gallery.models as gallery
from product.models import DishOnMain
from news.models import Article
from django import http
from django.utils.http import is_safe_url
from django.core.urlresolvers import translate_url
from django.views.generic.base import TemplateView
from django.utils.translation import (
    LANGUAGE_SESSION_KEY, check_for_language
)
import re

DEFAULT_PACKAGES = ['django.conf']
LANGUAGE_QUERY_PARAMETER = 'language'


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_news(self):
        result = Article.objects.all().order_by('-date')[:3]

        for item in result:
            item.text = re.sub(r'<.*?>', '', item.text)[:400] + "..."

        return result

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['dishs'] = DishOnMain.objects.all()[:4]
        context['slide_img'] = gallery.SlidesMainPage.objects.all()
        context['news'] = self.get_news()
        return context


def set_language(request):
    next = request.GET.get('next', request.GET.get('next'))
    if not is_safe_url(url=next, host=request.get_host()):
        next = request.META.get('HTTP_REFERER')
        if not is_safe_url(url=next, host=request.get_host()):
            next = '/'
    response = http.HttpResponseRedirect(next)
    if request.method == 'GET':
        lang_code = request.GET.get(LANGUAGE_QUERY_PARAMETER)
        if lang_code and check_for_language(lang_code):
            next_trans = translate_url(next, lang_code)
            if next_trans != next:
                response = http.HttpResponseRedirect(next_trans)
            if hasattr(request, 'session'):
                request.session[LANGUAGE_SESSION_KEY] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code,
                                    max_age=settings.LANGUAGE_COOKIE_AGE,
                                    path=settings.LANGUAGE_COOKIE_PATH,
                                    domain=settings.LANGUAGE_COOKIE_DOMAIN)
    return response
