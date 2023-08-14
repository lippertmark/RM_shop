# Generated by Django 4.2.4 on 2023-08-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount_of_orders',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]
