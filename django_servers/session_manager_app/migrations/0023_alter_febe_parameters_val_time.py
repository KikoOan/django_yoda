# Generated by Django 4.2.3 on 2023-08-28 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_manager_app', '0022_febe_parameters_aim_febe_parameters_cal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='febe_parameters',
            name='val_time',
            field=models.FloatField(default=10),
        ),
    ]
