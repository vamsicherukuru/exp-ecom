# Generated by Django 2.2.14 on 2020-11-30 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20201130_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='Product_code',
        ),
    ]
