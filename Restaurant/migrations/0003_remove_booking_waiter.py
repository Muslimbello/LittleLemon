# Generated by Django 4.2.7 on 2023-11-12 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_booker_booking_waiter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='waiter',
        ),
    ]