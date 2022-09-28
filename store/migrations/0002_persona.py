# Generated by Django 4.1.1 on 2022-09-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=12)),
                ('fecha_n', models.DateField()),
                ('correo', models.EmailField(max_length=150)),
                ('genero', models.CharField(max_length=10)),
            ],
        ),
    ]