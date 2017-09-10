from django.db import models
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    upload_to = 'slide_photo'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class SlidesMainPage(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to=path_and_rename, help_text="Рекомендуемый размер 1642x810.")
    text = models.TextField(max_length=100, verbose_name="Текст")

    def __str__(self):
        index = 1
        for slide in SlidesMainPage.objects.all():
            if slide == self:
                break
            index += 1
        return "Изображение №" + str(index)

    class Meta:
        verbose_name = 'Изображение для сладера'
        verbose_name_plural = 'Изображения для сладера'
