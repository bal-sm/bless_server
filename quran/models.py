from django.db import models


class Quran(models.Model):
    surat = models.IntegerField()
    ayat = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f"{self.surat}:{self.ayat}"

    class Meta:
        ordering = ["surat", "ayat"]
        verbose_name_plural = "Qur'an"


class TranslationVersion(models.Model):
    version = models.CharField(max_length=100)

    def __str__(self):
        return self.version

    class Meta:
        ordering = ["version"]
        verbose_name_plural = "Translation Versions"


class Translation(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE)
    translation_version = models.ForeignKey(
        TranslationVersion, on_delete=models.CASCADE
    )
    translation = models.TextField()

    def __str__(self):
        return f"{self.quran}, {self.translation_version}"

    class Meta:
        ordering = ["quran", "translation_version"]
        verbose_name_plural = "Translations"
