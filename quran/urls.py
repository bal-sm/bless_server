from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.quran_list, name="quran_list"),
]
