# Generated by Django 5.1.5 on 2025-01-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_alter_profile_cart_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cart_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
