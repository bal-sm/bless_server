from rest_framework import serializers

from .models import Quran


class QuranSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quran
        fields = ["surat", "ayat", "text"]
