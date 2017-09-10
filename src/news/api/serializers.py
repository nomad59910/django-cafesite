from rest_framework import serializers
from news.models import Article
from bs4 import BeautifulSoup


class ArticleDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('title', 'text', 'date', 'image',)


class ArticleSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='news:article',
                                               lookup_field='id')
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False,
                                     read_only=True)

    def _crop_str(self, text, count):
        if len(text) > count:
            text = text[:count] + '...'
        return text

    def get_title(self, obj):
        return self._crop_str(obj.title, 25)

    def get_text(self, obj):
        text = BeautifulSoup(obj.text).text
        return self._crop_str(text, 440)

    class Meta:
        model = Article
        fields = ('title', 'text', 'date', 'image', 'url',)
