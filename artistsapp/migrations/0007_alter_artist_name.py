# Generated by Django 4.2.5 on 2023-11-13 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistsapp', '0006_alter_song_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
