# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20170326_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='department',
        ),
    ]
