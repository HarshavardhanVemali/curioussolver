# Generated by Django 5.1 on 2024-08-20 14:18

import curioussolverapp.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curioussolverapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone_number',
            field=curioussolverapp.models.PhoneNumberField(max_length=15, null=True, region='IN', unique=True),
        ),
    ]
