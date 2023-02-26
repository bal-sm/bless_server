from rest_framework import serializers

from .models import Ayatship


class AyatshipSerializer(serializers.HyperlinkedModelSerializer):
    surat_number = serializers.CharField(source="surat.number")
    surat_name = serializers.CharField(source="surat.name")
    ayat_text = serializers.CharField(source="ayat.text")

    class Meta:
        model = Ayatship
        fields = ("surat_number", "surat_name", "number", "ayat_text")
