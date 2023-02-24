from django.contrib import admin

from .models import Ayat
from .models import Ayatship
from .models import Surat


@admin.register(Surat)
class SuratAdmin(admin.ModelAdmin):
    pass


@admin.register(Ayatship)
class AyatshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Ayat)
class AyatAdmin(admin.ModelAdmin):
    pass
