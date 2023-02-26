from django.urls import path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r"quran/api", views.AyatshipViewSet)

urlpatterns = [
    path("", views.surat_list, name="surat_list"),
    path("<int:surat_number>", views.ayatship_list, name="ayatship_list"),
    path("<int:surat_number>/<int:ayat_number>", views.ayat_view, name="ayat_view"),
]
