# Generated by Django 4.2.6 on 2023-11-20 20:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('movies', '0004_alter_filmwork_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='file_path',
            field=models.TextField(blank=True, null=True, verbose_name='file path'),
        ),
    ]