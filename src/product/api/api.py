from product.models import Dish, TypeDish
from .serializers import DishPreviewSerializer, DishSerializer, TypeDishSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView


def convert_list(line):
        if line == '':
            return []
        else:
            return [int(x) for x in line.split(',')]


class DishsListAPIView(ListAPIView):
    serializer_class = DishPreviewSerializer

    def get_queryset(self):

        request = self.request
        queryset = Dish.objects.all()

        if 'type_dishes' in request.GET:
            type_dishes = convert_list(request.GET['type_dishes'])
            queryset = queryset.filter(category__in=type_dishes)

        if 'ingredients' in request.GET:
            ingredient = convert_list(request.GET['ingredients'])
            queryset = queryset.filter(ingredients__id__in=ingredient)

        if 'id' in request.GET:
            ids = convert_list(self.request.GET['id'])
            queryset = queryset.filter(id__in=ids)

        return queryset.distinct()


class DishAPIView(RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    lookup_field = 'id'


class TasksListAPIView(ListAPIView):
    serializer_class = TypeDishSerializer
    queryset = TypeDish.objects.all()
