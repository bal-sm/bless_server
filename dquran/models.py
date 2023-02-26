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

    def __str__(bal):
        return f"{bal.number}. {bal.name}"

    class Meta:
        abstract = True
        ordering = ("number",)


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

    def __str__(bal):
        return f"{bal.surat}:{bal.number}, {bal.ayat.text}"

    class Meta:
        abstract = True
        ordering = ("surat", "number")
        unique_together = (("surat", "number"),)


class AbstractAyat(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID",
    )
    text = models.TextField()

    def __str__(bal):
        return f"{bal.text}"

    class Meta:
        abstract = True


class AbstractQuranSurat(AbstractSurat):
    opened_with_basmallah = models.BooleanField(
        default=True,
    )

    class Meta(AbstractSurat.Meta):
        abstract = True


class Surat(AbstractQuranSurat):
    pass


class Ayatship(AbstractAyatship):
    pass


class Ayat(AbstractAyat):
    pass
