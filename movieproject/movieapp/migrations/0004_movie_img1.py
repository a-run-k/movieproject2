# Generated by Django 4.2.6 on 2023-10-31 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_remove_movie_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img1',
            field=models.ImageField(default=2, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
