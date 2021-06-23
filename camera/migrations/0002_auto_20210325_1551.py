# Generated by Django 3.1 on 2021-03-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='descricao',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='camera',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]