# Generated by Django 3.2.9 on 2022-06-09 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20220530_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='destallepedido',
            name='estado',
            field=models.CharField(choices=[['IN', 'Inactivo'], ['AC', 'Activo']], default='PE', max_length=2),
        ),
    ]