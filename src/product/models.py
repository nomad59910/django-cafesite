from django.db import models
from uuid import uuid4
import os


def path_and_rename(instance, filename):
    upload_to = 'photo'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


class Dish(models.Model):

    name = models.CharField(max_length=18, verbose_name="Название")
    price = models.IntegerField(verbose_name="Стоимость")
    description = models.TextField(max_length=500, verbose_name="Описание")
    category = models.ForeignKey("TypeDish", verbose_name='Тип')
    ingredients = models.ManyToManyField("Ingredients",
                                         verbose_name='Ингредиенты')
    image = models.ImageField(verbose_name='Изображение',
                              upload_to=path_and_rename,
                              help_text="Рекомендуемый размер 550x550.")

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name


class TypeDish(models.Model):

    name = models.CharField(max_length=40, verbose_name="Название")

    class Meta:
        verbose_name = 'Тип блюда'
        verbose_name_plural = 'Типы блюд'

    def __str__(self):
        return self.name


class Ingredients(models.Model):

    name = models.CharField(max_length=40, verbose_name='Название')
    type_ingredients = models.ForeignKey("TypeIngredients",
                                         verbose_name='Тип ингредиента')

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return self.name


class TypeIngredients(models.Model):

    name = models.CharField(max_length=40, verbose_name="Название")

    class Meta:
        verbose_name = 'Тип ингридиента'
        verbose_name_plural = 'Типы ингридиентов'

    def __str__(self):
        return self.name


class DishOnMain(models.Model):

    dish = models.OneToOneField("Dish", verbose_name="Блюдо")
    dish_text = models.TextField(max_length=120, verbose_name="Текст")

    class Meta:
        verbose_name = 'Блюдо на главной'
        verbose_name_plural = 'Блюда на главной'

    def __str__(self):
        return self.dish.name
