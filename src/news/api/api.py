from .serializers import ArticleSerializer, ArticleDetailSerializer
from news.models import *
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination


class ArticleListAPI(ListAPIView):
    queryset = Article.objects.all().order_by('-date')
    serializer_class = ArticleSerializer
    pagination_class = LimitOffsetPagination


class ArticleAPI(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'id'
