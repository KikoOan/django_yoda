# Generated by Django 4.2.3 on 2023-07-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_manager_app', '0015_febe_parameters_sb1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='febe_parameters',
            name='SB1',
            field=models.BooleanField(),
        ),
    ]
