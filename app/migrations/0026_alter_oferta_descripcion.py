# Generated by Django 3.2.9 on 2022-06-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_delete_factura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
