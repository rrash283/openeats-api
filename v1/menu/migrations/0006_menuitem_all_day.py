# Generated by Django 2.0.1 on 2018-02-19 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20180219_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='all_day',
            field=models.BooleanField(default=False),
        ),
    ]
