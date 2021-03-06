# Generated by Django 3.2.9 on 2022-02-28 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('nit', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=70)),
                ('correo', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('contraseña', models.CharField(max_length=100)),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.departamento')),
                ('municipio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Mesero',
            fields=[
                ('documento', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('tipodoc', models.CharField(max_length=2)),
                ('nombre1', models.CharField(max_length=20)),
                ('nombre2', models.CharField(max_length=20)),
                ('apellido1', models.CharField(max_length=20)),
                ('apellido2', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=12)),
                ('genero', models.CharField(choices=[['F', 'Femenino'], ['M', 'Masculino'], ['O', 'Otro']], max_length=1)),
                ('direccion', models.CharField(max_length=30)),
                ('usuario', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=100)),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.departamento')),
                ('municipio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.municipio')),
            ],
        ),
    ]
