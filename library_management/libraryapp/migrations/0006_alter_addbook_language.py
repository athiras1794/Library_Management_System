# Generated by Django 4.2.3 on 2023-08-19 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0005_addbook_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='language',
            field=models.CharField(choices=[('Malayalam', 'Malayalam'), ('English', 'English'), ('Other', 'Other')], default='Malayalam', max_length=20),
        ),
    ]
