# Generated by Django 4.2.4 on 2023-08-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0003_userprofile_user_regular_alter_artistprofile_artist"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="album_pic",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
