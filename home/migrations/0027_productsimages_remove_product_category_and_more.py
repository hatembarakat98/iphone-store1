# Generated by Django 4.1.4 on 2023-01-17 16:14

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_remove_order_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Covergimage', models.ImageField(null=True, upload_to='placeToUpload')),
                ('Battrayimage', models.ImageField(null=True, upload_to='placeToUpload')),
                ('Coreimage', models.ImageField(null=True, upload_to='placeToUpload')),
                ('Frontimage', models.ImageField(null=True, upload_to='placeToUpload')),
                ('Cameraimage', models.ImageField(null=True, upload_to='placeToUpload')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.AddField(
            model_name='product',
            name='Cat',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='battery',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='camera',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='product',
            name='core',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='coverage',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='front',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='mobile_color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='product',
            name='mobile_color2',
            field=colorfield.fields.ColorField(default='#FC0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='product',
            name='mobile_color3',
            field=colorfield.fields.ColorField(default='#FB0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='product',
            name='mobile_color4',
            field=colorfield.fields.ColorField(default='#FA0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='product',
            name='screan',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='ProductImage',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.productsimages'),
        ),
    ]
