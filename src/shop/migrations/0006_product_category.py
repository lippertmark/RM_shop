# Generated by Django 4.2.4 on 2023-08-07 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_old_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Cosméticos antiedad', 'Cosméticos antiedad'), ('Dieta - Pérdida de peso', 'Dieta - Pérdida de peso'), ('Diabetes', 'Diabetes'), ('Articulaciones', 'Articulaciones'), ('Prostatitis', 'Prostatitis'), ('Cistitis', 'Cistitis'), ('Aumento', 'Aumento'), ('Parásitos', 'Parásitos'), ('Hipertensión', 'Hipertensión'), ('Cabello', 'Cabello'), ('Varices', 'Varices'), ('Audición', 'Audición'), ('Sombrero Blanco', 'Sombrero Blanco')], default='Aumento', max_length=255),
        ),
    ]
