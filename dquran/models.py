import uuid

from django.db import models


class AbstractSurat(models.Model):
    number = models.PositiveIntegerField(
        primary_key=True,
    )
    name = models.CharField(
        max_length=1000,
    )
    ayats = models.ManyToManyField(
        "Ayat",
        through="Ayatship",
    )

    class Meta:
        abstract = True


class AbstractAyatship(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID",
    )
    surat = models.ForeignKey(
        "Surat",
        on_delete=models.CASCADE,
    )
    ayat = models.ForeignKey(
        "Ayat",
        on_delete=models.CASCADE,
    )
    number = models.PositiveIntegerField()


class AbstractAyat(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID",
    )
    text = models.TextField()

    def __str__(self):
        return f"{self.surat}:{self.ayat}"

    class Meta:
        abstract = True


class Surat(AbstractSurat):
    pass


class Ayatship(AbstractAyatship):
    pass


class Ayat(AbstractAyat):
    pass


class TranslationVersion(models.Model):
    version = models.CharField(max_length=100)

    def __str__(self):
        return self.version

    class Meta:
        ordering = ["version"]
        verbose_name_plural = "Translation Versions"


class AyatTranslation(models.Model):
    ayat = models.ForeignKey(Ayat, on_delete=models.CASCADE)
    translation_version = models.ForeignKey(
        TranslationVersion, on_delete=models.CASCADE
    )
    translation = models.TextField()

    def __str__(self):
        return f"{self.quran}, {self.translation_version}"

    class Meta:
        ordering = ["ayat", "translation_version"]
        verbose_name_plural = "Translations"
