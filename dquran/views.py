from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import viewsets

from .models import Ayatship
from .models import Surat
from .serializers import AyatshipSerializer


def surat_list(request):
    root = Surat.objects.all()
    context = {
        "root": root,
    }
    return render(request, "quran/surat_list.html", context)


def ayatship_list(request, surat_number):
    root = get_list_or_404(Ayatship, surat__number=surat_number)
    context = {
        "root": root,
    }
    return render(request, "quran/ayatship_list.html", context)


def ayat_view(request, surat_number, ayat_number):
    ayatship = get_object_or_404(
        Ayatship,
        surat__number=surat_number,
        number=ayat_number,
    )

    context = {
        "ayatship": ayatship,
    }
    return render(request, "quran/ayat_view.html", context)


class AyatshipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Qur'an to be viewed.
    """

    queryset = Ayatship.objects.all()
    serializer_class = AyatshipSerializer
