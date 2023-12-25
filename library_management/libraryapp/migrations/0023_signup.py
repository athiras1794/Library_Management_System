# Generated by Django 4.2.3 on 2023-08-25 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libraryapp', '0022_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('image', models.ImageField(upload_to='images/')),
                ('approval_status', models.CharField(choices=[('Pending Approval', 'Pending Approval'), ('Approved', 'Approved')], default='Pending Approval', max_length=20)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
