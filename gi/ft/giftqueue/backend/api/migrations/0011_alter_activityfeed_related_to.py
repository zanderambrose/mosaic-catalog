# Generated by Django 4.1.2 on 2023-01-17 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_activityfeed_related_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityfeed',
            name='related_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.giftitem'),
        ),
    ]
