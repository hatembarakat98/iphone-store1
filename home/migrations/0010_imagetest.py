# Generated by Django 3.2.3 on 2021-07-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_farm'),
    ]

    operations = [
        migrations.CreateModel(
            name='imageTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testImage', models.ImageField(upload_to='static/testimge')),
            ],
        ),
    ]
