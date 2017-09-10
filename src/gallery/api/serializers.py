from rest_framework import serializers
from gallery.models import SlidesMainPage


class SlidesMainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlidesMainPage
        fields = ('image', 'text', )
