# Generated by Django 2.2.7 on 2019-12-10 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skager', '0007_auto_20191210_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='adress',
            new_name='address',
        ),
    ]
