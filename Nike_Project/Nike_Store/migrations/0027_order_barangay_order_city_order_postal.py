# Generated by Django 5.1.7 on 2025-05-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nike_Store', '0026_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='barangay',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='postal',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
