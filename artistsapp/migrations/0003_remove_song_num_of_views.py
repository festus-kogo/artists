# Generated by Django 4.2.5 on 2023-11-12 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artistsapp', '0002_song_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='num_of_views',
        ),
    ]
