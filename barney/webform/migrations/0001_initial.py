# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('address', models.TextField()),
                ('plan', models.TextField()),
                ('validated_address', models.TextField()),
                ('sku', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
