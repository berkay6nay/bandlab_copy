# Generated by Django 4.2.4 on 2023-08-25 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0013_artistprofile_follower"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="preview_song",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]