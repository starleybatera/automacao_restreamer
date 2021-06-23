# Generated by Django 3.1 on 2021-03-25 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('raca', '0001_initial'),
        ('agrupamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacao', models.CharField(max_length=255, unique=True)),
                ('descricao', models.TextField(max_length=255, null=True)),
                ('cod_agrupamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agrupamentos.agrupamento')),
                ('cod_raca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raca.raca')),
            ],
        ),
    ]