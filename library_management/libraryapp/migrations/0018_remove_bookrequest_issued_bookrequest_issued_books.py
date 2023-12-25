# Generated by Django 4.2.3 on 2023-08-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0017_bookrequest_issued'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookrequest',
            name='issued',
        ),
        migrations.AddField(
            model_name='bookrequest',
            name='issued_books',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
