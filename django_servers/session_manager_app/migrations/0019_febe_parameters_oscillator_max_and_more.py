# Generated by Django 4.2.3 on 2023-07-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_manager_app', '0018_remove_febe_parameters_sb1_pol1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='febe_parameters',
            name='oscillator_max',
            field=models.FloatField(default=47.0),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='oscillator_min',
            field=models.FloatField(default=22.0),
        ),
    ]
