# Generated by Django 4.2.3 on 2023-08-22 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0018_remove_bookrequest_issued_bookrequest_issued_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookrequest',
            name='issued_books',
        ),
        migrations.AddField(
            model_name='bookrequest',
            name='issued',
            field=models.BooleanField(default=False),
        ),
    ]
