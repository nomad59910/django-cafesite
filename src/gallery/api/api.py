from gallery.models import SlidesMainPage
from .serializers import SlidesMainPageSerializer
from rest_framework.generics import ListAPIView


class SliderListAPI(ListAPIView):
    queryset = SlidesMainPage.objects.all()
    serializer_class = SlidesMainPageSerializer
