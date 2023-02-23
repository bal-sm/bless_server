from django.contrib import admin

from .models import AyatTranslation
from .models import TranslationVersion


class TranslationInline(admin.StackedInline):
    model = AyatTranslation


@admin.register(TranslationVersion)
class TranslationVersionAdmin(admin.ModelAdmin):
    pass
