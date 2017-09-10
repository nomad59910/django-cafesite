# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from .models import Dish, TypeDish, Ingredients, TypeIngredients, DishOnMain


class DishTranslationOptions(TranslationOptions):
    fields = ('description', 'name', )


class TypeDishTranslationOptions(TranslationOptions):
    fields = ('name', )


class IngredientsTranslationOptions(TranslationOptions):
    fields = ('name', )


class TypeIngredientsTranslationOptions(TranslationOptions):
    fields = ('name', )


class DishOnMainTranslationOptions(TranslationOptions):
    fields = ('dish_text', )


translator.register(Dish, DishTranslationOptions)
translator.register(TypeDish, TypeDishTranslationOptions)
translator.register(Ingredients, IngredientsTranslationOptions)
translator.register(TypeIngredients, TypeDishTranslationOptions)
translator.register(DishOnMain, DishOnMainTranslationOptions)
