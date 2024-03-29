# Generated by Django 4.1.5 on 2023-03-31 06:42
import uuid

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ayat",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Ayatship",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.PositiveIntegerField()),
                (
                    "ayat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="dquran.ayat"
                    ),
                ),
            ],
            options={
                "ordering": ("surat", "number"),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Surat",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.PositiveIntegerField()),
                ("name", models.CharField(max_length=1000)),
                (
                    "ayats",
                    models.ManyToManyField(through="dquran.Ayatship", to="dquran.ayat"),
                ),
            ],
            options={
                "ordering": ("number",),
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="ayatship",
            name="surat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dquran.surat"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="ayatship",
            unique_together={("surat", "number")},
        ),
    ]
