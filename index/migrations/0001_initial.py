# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\xbc\xd0\xbe\xd1\x91 \xd0\xb8\xd0\xbc\xd1\x8f', blank=True)),
                ('about_me', ckeditor.fields.RichTextField(null=True, verbose_name=b'\xd0\xbe\xd0\xb1\xd0\xbe \xd0\xbc\xd0\xbd\xd0\xb5', blank=True)),
                ('public_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'salon_about_my',
            },
        ),
        migrations.CreateModel(
            name='CkEditor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, blank=True)),
                ('text_ck', ckeditor.fields.RichTextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'test_cseditor',
            },
        ),
    ]
