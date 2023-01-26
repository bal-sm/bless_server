from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"quran", views.QuranViewSet)

urlpatterns = [
    path("list/", views.quran_list, name="quran_list"),
    path("view/<int:id>", views.ayat_view, name="ayat_view"),
]
