# Generated by Django 4.1.6 on 2023-06-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_shippingadress_shippingaddress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='image',
            field=models.CharField(blank=True, default='/sample.jpg', max_length=200, null=True),
        ),
    ]
