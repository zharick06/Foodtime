# Generated by Django 3.2.9 on 2022-04-03 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220403_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='nit',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]