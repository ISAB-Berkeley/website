# Generated by Django 2.0.1 on 2018-02-28 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_eventimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='cover',
            field=models.CharField(default='abc', max_length=60),
            preserve_default=False,
        ),
    ]
