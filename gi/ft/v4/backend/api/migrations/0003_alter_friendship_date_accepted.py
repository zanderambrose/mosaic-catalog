# Generated by Django 4.1.2 on 2023-01-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_friendship_date_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='date_accepted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
