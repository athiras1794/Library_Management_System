# Generated by Django 4.2.3 on 2023-09-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0037_bookrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrequest',
            name='reason',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
