# Generated by Django 3.2.9 on 2022-05-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20220519_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='estado',
            field=models.CharField(choices=[['IN', 'Inactivo'], ['AC', 'Activo']], max_length=2),
        ),
        migrations.AlterField(
            model_name='mesas',
            name='estado',
            field=models.CharField(choices=[['I', 'Inactivo'], ['A', 'Activo']], max_length=1),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[['IN', 'Inactivo'], ['AC', 'Activo']], max_length=2),
        ),
    ]
