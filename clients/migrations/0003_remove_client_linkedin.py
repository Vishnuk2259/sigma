# Generated by Django 5.0.2 on 2024-05-17 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='linkedin',
        ),
    ]