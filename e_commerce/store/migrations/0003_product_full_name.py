# Generated by Django 5.1.5 on 2025-01-27 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='full_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
