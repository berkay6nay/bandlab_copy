# Generated by Django 4.2.4 on 2023-08-04 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0004_album_album_pic"),
    ]

    operations = [
        migrations.RenameField(
            model_name="artistprofile",
            old_name="name",
            new_name="artist_name",
        ),
        migrations.RenameField(
            model_name="artistprofile",
            old_name="artist",
            new_name="user_artist",
        ),
    ]