# Generated by Django 4.2.4 on 2023-08-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_popular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
