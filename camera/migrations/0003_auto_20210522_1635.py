# Generated by Django 3.1 on 2021-05-22 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agrupamentos', '0002_auto_20210522_1635'),
        ('camera', '0002_auto_20210325_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='agrupamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camera', to='agrupamentos.agrupamento'),
        ),
    ]
