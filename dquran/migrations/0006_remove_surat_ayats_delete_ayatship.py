# Generated by Django 4.1.5 on 2023-02-24 04:26
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dquran", "0005_delete_ayattranslation_delete_translationversion"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="surat",
            name="ayats",
        ),
        migrations.DeleteModel(
            name="Ayatship",
        ),
    ]
