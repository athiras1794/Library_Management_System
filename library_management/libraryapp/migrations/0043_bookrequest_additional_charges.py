# Generated by Django 4.2.3 on 2023-09-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0042_problemreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrequest',
            name='additional_charges',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
