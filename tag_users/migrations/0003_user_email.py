# Generated by Django 3.1.1 on 2022-07-07 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_users', '0002_rename_password_user_password_remove_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Email',
            field=models.CharField(default='', max_length=50),
        ),
    ]
