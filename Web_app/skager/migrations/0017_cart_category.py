# Generated by Django 2.2.7 on 2019-12-11 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skager', '0016_auto_20191211_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='category',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]