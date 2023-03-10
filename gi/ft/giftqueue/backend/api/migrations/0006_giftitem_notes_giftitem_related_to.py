# Generated by Django 4.1.2 on 2023-01-15 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_registryuser_relationships'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftitem',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='giftitem',
            name='related_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.celebrationday'),
        ),
    ]
