# Generated by Django 4.2.6 on 2023-11-23 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0008_application'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shelter',
            name='user',
        ),
    ]
