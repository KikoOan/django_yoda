# Generated by Django 4.2.3 on 2023-07-24 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session_manager_app', '0013_rename_pol_sb_pol_pol_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='febe_parameters',
            name='SB1',
        ),
    ]
