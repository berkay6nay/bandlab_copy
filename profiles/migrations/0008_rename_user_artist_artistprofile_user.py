# Generated by Django 4.2.4 on 2023-08-15 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0007_artistprofile_artist_pic_userprofile_user_pic"),
    ]

    operations = [
        migrations.RenameField(
            model_name="artistprofile",
            old_name="user_artist",
            new_name="user",
        ),
    ]