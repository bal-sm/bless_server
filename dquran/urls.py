from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.quran_list, name="quran_list"),
    path("view/<int:id>", views.ayat_view, name="ayat_view"),
]
