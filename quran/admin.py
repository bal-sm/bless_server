from django.contrib import admin

from .models import Quran


@admin.register(Quran)
class QuranAdmin(admin.ModelAdmin):
    pass
