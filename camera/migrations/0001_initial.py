# Generated by Django 3.1 on 2021-03-25 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agrupamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('agrupamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agrupamentos.agrupamento')),
            ],
        ),
    ]
