# Generated by Django 2.2.5 on 2020-08-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meme_viewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookies',
            name='setCookies',
            field=models.BooleanField(default=False),
        ),
    ]
