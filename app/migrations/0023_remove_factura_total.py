# Generated by Django 3.2.9 on 2022-06-09 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_destallepedido_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='total',
        ),
    ]
