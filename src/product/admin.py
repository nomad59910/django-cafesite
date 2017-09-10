from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import *


class DishAdmin(TranslationAdmin):

    filter_horizontal = ('ingredients', )
    search_fields = ['name_ru']
    list_display = ('name_ru', 'price')


class StandardModelAdmin(TranslationAdmin):
    pass

admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredients, StandardModelAdmin)
admin.site.register(TypeDish, StandardModelAdmin)
admin.site.register(TypeIngredients, StandardModelAdmin)
admin.site.register(DishOnMain, StandardModelAdmin)