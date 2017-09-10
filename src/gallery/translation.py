from modeltranslation.translator import translator, TranslationOptions
from .models import SlidesMainPage


class SlidesMainPageTranslationOptions(TranslationOptions):
    fields = ('text', )


translator.register(SlidesMainPage, SlidesMainPageTranslationOptions)
