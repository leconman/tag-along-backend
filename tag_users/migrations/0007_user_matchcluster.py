# Generated by Django 4.0.5 on 2022-08-01 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_users', '0006_alter_user_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='MatchCluster',
            field=models.IntegerField(default=-1),
        ),
    ]
