from django.shortcuts import render_to_response
from .models import *
from django.http import JsonResponse
from django.core.mail import send_mail
from senjucafe.settings import LANGUAGES
from django.views.generic import TemplateView


class MenuView(TemplateView):
    template_name = 'menu/menu.html'

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)

        ingredients = {}
        for ingredient in Ingredients.objects.all():
            if ingredient.type_ingredients.name in ingredients.keys():
                ingredients[ingredient.type_ingredients.name].append(ingredient)
            else:
                ingredients[ingredient.type_ingredients.name] = [ingredient]

        context['ingredients'] = ingredients
        context['dish_types'] = TypeDish.objects.all()
        context['LANGUAGES'] = LANGUAGES
        print("I am hear!")
        return context
