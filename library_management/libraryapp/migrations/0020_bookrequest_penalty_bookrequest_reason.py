# Generated by Django 4.2.3 on 2023-08-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0019_remove_bookrequest_issued_books_bookrequest_issued'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrequest',
            name='penalty',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='bookrequest',
            name='reason',
            field=models.CharField(blank=True, choices=[('Damaged', 'Damaged'), ('Overdue', 'Overdue'), ('Lost', 'Lost')], max_length=20, null=True),
        ),
    ]
