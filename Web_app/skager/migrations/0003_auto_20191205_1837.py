# Generated by Django 2.2.7 on 2019-12-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skager', '0002_product_toyslist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', upload_to='product_pics'),
        ),
    ]