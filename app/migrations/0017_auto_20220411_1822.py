# Generated by Django 3.2.9 on 2022-04-11 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_oferta_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='descripcion',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='postulados',
            name='fecha',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]