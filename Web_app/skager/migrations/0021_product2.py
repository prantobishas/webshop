# Generated by Django 2.2.7 on 2019-12-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skager', '0020_auto_20191211_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('School', 'School'), ('Educatief', 'Educatief'), ("Auto's", "Auto's")], default=None, max_length=64)),
                ('image', models.ImageField(default='default.png', upload_to='product_pics')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
