# Generated by Django 5.2 on 2025-05-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nike_Store', '0002_user_username_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=10),
        ),
    ]
