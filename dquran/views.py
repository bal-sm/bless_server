from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Quran
from .models import Translation


def quran_list(request):
    root = Quran.objects.all()
    context = {
        "root": root,
    }
    return render(request, "quran/quran_list.html", context)


def ayat_view(request, id):
    ayat = get_object_or_404(Quran, id=id)
    try:
        ayat_translation = Translation.objects.get(quran=ayat)
    except Translation.DoesNotExist:
        ayat_translation = None

    context = {
        "ayat": ayat,
        "ayat_translation": ayat_translation,
    }
    return render(request, "quran/ayat_view.html", context)
