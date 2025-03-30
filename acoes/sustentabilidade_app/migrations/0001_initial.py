# Generated by Django 5.1.7 on 2025-03-19 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioSustentavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('consumo_energia', models.FloatField(help_text='Consumo de energia em kWh/mês')),
                ('consumo_agua', models.FloatField(help_text='Consumo de água em m³/mês')),
                ('residuos', models.FloatField(help_text='Resíduos não recicláveis em kg/semana')),
                ('uso_transporte', models.FloatField(help_text='Distância percorrida em km/semana')),
                ('nota_sustentabilidade', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
