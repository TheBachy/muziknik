# Generated by Django 3.1.2 on 2021-06-09 14:28

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20210609_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='music',
            field=models.FileField(blank=True, null=True, upload_to=music.models.attachment_path, verbose_name='Song file'),
        ),
    ]