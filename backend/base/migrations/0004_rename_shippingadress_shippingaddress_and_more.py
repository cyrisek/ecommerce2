# Generated by Django 4.1.6 on 2023-06-17 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingAdress',
            new_name='ShippingAddress',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='adress',
            new_name='address',
        ),
    ]
