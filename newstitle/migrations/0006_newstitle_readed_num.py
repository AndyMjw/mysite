# Generated by Django 2.0 on 2018-11-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newstitle', '0005_newstitle_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstitle',
            name='readed_num',
            field=models.IntegerField(default=0),
        ),
    ]
