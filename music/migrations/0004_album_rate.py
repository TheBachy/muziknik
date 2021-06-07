# Generated by Django 3.1.2 on 2021-06-07 18:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20210607_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='rate',
            field=models.FloatField(default=5.0, help_text='Please enter an float value (range 1.0 - 10.0)', null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='Rating'),
        ),
    ]