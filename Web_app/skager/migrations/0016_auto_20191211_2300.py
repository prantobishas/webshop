# Generated by Django 2.2.7 on 2019-12-11 22:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skager', '0015_auto_20191211_2258'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart2',
            new_name='Cart',
        ),
    ]
