# Generated by Django 4.2.6 on 2023-10-27 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('qtd_paginas', models.IntegerField(unique=True)),
                ('capa_livro', models.ImageField(upload_to='')),
                ('autor_livro', models.CharField(max_length=255)),
                ('sacado', models.CharField(max_length=255)),
                ('qtd_livros', models.CharField(max_length=255)),
                ('genero', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.genero')),
            ],
        ),
    ]
