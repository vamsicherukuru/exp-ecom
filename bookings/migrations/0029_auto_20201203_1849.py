# Generated by Django 2.2.14 on 2020-12-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0028_auto_20201203_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='hq',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='occupation',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
