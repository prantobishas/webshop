# Generated by Django 2.2.7 on 2019-12-11 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skager', '0018_auto_20191211_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorders',
            name='order',
            field=models.ManyToManyField(to='skager.Cart2'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
