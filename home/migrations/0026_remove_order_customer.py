# Generated by Django 3.2.6 on 2023-01-17 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20230117_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]
