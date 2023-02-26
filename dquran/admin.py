from django.contrib import admin

from .models import Ayat
from .models import Ayatship
from .models import Surat


class AyatshipInline(admin.StackedInline):
    model = Ayatship


@admin.register(Surat)
class SuratAdmin(admin.ModelAdmin):
    inlines = (AyatshipInline,)


@admin.register(Ayatship)
class AyatshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Ayat)
class AyatAdmin(admin.ModelAdmin):
    pass
