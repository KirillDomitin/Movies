# Generated by Django 4.2.6 on 2023-11-20 20:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('movies', '0002_alter_filmwork_file_path_alter_genre_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='file_path',
            field=models.TextField(null=True, verbose_name='file path'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(null=True, verbose_name='description'),
        ),
    ]