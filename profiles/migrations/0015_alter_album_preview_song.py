# Generated by Django 4.2.4 on 2023-08-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0014_album_preview_song"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="preview_song",
            field=models.FileField(blank=True, null=True, upload_to="audio/"),
        ),
    ]