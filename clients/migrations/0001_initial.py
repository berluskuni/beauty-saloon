# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f \xd0\xba\xd0\xbb\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0', blank=True)),
                ('number', models.CharField(help_text=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb2 \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb5 0504824567', unique=True, max_length=200, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0', blank=True)),
                ('formula', models.TextField(verbose_name=b'\xd0\xa4\xd0\xbe\xd1\x80\xd0\xbc\xd1\x83\xd0\xbb\xd0\xb0 \xd0\xbe\xd0\xba\xd1\x80\xd0\xb0\xd1\x81\xd0\xba\xd0\xb8 \xd0\xba\xd0\xbb\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0', blank=True)),
            ],
            options={
                'ordering': ['number'],
                'db_table': 'db_clients_app',
                'verbose_name': '\u041a\u043b\u0438\u0435\u043d\u0442\u0441\u043a\u0430\u044f \u0431\u0430\u0437\u0430',
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(help_text=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb2 \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb5 0504824567', max_length=200, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0', blank=True)),
            ],
            options={
                'db_table': 'db_clients_search',
                'verbose_name': '\u041f\u043e\u0438\u0441\u043a \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432',
            },
        ),
    ]
