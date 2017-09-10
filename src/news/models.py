from django.db import models
from redactor.fields import RedactorField
from uuid import uuid4
import os


def path_and_rename(instance, filename):
    print("instance:", instance)
    upload_to = 'news'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class Article(models.Model):
    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = RedactorField(max_length=10000, verbose_name="Текст")
    date = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(verbose_name='Изображение', upload_to=path_and_rename)

    def __str__(self):
        return self.title
