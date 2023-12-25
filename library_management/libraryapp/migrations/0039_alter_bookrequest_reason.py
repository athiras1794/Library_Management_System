# Generated by Django 4.2.3 on 2023-09-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0038_alter_bookrequest_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrequest',
            name='reason',
            field=models.CharField(blank=True, choices=[('Damaged', 'Damaged'), ('Overdue', 'Overdue'), ('Lost', 'Lost')], max_length=20, null=True),
        ),
    ]
