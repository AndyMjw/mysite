# Generated by Django 2.0 on 2018-11-27 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newstitle', '0004_auto_20181127_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstitle',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]