# Generated by Django 3.2.6 on 2023-01-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20210901_1431'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Disease',
        ),
        migrations.DeleteModel(
            name='Farm',
        ),
        migrations.DeleteModel(
            name='FarmarsRigister',
        ),
        migrations.DeleteModel(
            name='imageTest',
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
