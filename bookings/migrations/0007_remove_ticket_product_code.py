# Generated by Django 2.2.14 on 2020-11-30 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_auto_20201130_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='Product_code',
        ),
    ]