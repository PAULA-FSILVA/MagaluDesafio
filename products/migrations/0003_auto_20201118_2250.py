# Generated by Django 3.1.3 on 2020-11-19 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201119_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id_product',
            field=models.IntegerField(unique=True),
        ),
    ]
