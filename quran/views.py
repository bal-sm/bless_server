from django.shortcuts import render

from .models import Quran


def quran_list(request):
    root = Quran.objects.all()
    context = {
        "root": root,
    }
    return render(request, "quran/quran_list.html", context)
