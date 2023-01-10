from django.contrib import admin

from .models import Quran
from .models import Translation
from .models import TranslationVersion


class TranslationInline(admin.StackedInline):
    model = Translation


@admin.register(Quran)
class QuranAdmin(admin.ModelAdmin):
    inlines = (TranslationInline,)


@admin.register(TranslationVersion)
class TranslationVersionAdmin(admin.ModelAdmin):
    pass
