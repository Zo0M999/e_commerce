# Generated by Django 5.1.5 on 2025-01-29 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_profile_cart_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cart_data',
            field=models.JSONField(default=dict),
        ),
    ]
