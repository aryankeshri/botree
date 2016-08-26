# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-26 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_document', models.CharField(max_length=100, verbose_name='Name of Document')),
                ('file', models.FileField(upload_to='pdf')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_project', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='project',
            field=models.ManyToManyField(to='projects.Project'),
        ),
    ]