import uuid

from django.db import models


class AbstractSurat(models.Model):
    number = models.PositiveIntegerField(
        primary_key=True,
    )
    name = models.CharField(
        max_length=1000,
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

    class Meta:
        abstract = True


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


class Ayat(AbstractAyat):
    pass
