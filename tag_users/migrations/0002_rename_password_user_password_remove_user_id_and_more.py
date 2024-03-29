# Generated by Django 4.0.5 on 2022-07-07 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='Password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='Ambitious',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='DogLover',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='EasyGoing',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='Gamer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='StarWarsFan',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='Username',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
