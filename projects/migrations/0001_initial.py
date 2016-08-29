# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-29 06:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='pdf', validators=[projects.models.validation_file_extension], verbose_name='Name of Document')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_project', models.CharField(max_length=50, unique=True, verbose_name='Name of Project')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='project',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]
