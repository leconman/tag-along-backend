# Generated by Django 3.1.1 on 2022-07-19 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_users', '0003_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Ambitious',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='BasketballFan',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='BeatlesFan',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='DogLover',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='FilmBuff',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='Gamer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='Homebody',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='MorningPerson',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='NatureLover',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='NightOwl',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='StarWarsFan',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='ThrillSeeker',
            field=models.IntegerField(default=0),
        ),
    ]
