# Generated by Django 4.2.3 on 2023-07-24 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_manager_app', '0011_delete_colorchoice_rename_pol_1_sb_pol_pol_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='febe_parameters',
            name='sb_pol_1',
            field=models.BooleanField(),
        ),
    ]
