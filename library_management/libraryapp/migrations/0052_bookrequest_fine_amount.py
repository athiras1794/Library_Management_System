# Generated by Django 4.2.3 on 2023-09-14 11:52

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0051_remove_bookrequest_additional_charges_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrequest',
            name='fine_amount',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
    ]
