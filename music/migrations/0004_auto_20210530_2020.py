# Generated by Django 3.1.2 on 2021-05-30 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20210530_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='lenght',
        ),
        migrations.AddField(
            model_name='song',
            name='length',
            field=models.TimeField(default=0, help_text='Please enter an float value (minutes, seconds)', verbose_name='Length'),
        ),
    ]
