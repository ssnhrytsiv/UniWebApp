# Generated by Django 2.1.7 on 2019-03-12 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.BooleanField(default=False),
        ),
    ]
