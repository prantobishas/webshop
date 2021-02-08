# Generated by Django 2.2.7 on 2019-12-11 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skager', '0017_cart_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='category',
        ),
        migrations.CreateModel(
            name='Cart2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('price_one', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_many', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
