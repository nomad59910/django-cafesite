from django.contrib import admin
from gallery.models import SlidesMainPage
from modeltranslation.admin import TranslationAdmin


class StandardModelAdmin(TranslationAdmin):
    pass


admin.site.register(SlidesMainPage, StandardModelAdmin)
