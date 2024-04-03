# Generated by Django 4.2.3 on 2023-07-24 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_manager_app', '0017_rename_sb1_febe_parameters_sb1_pol1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='febe_parameters',
            name='SB1_POL1',
        ),
        migrations.RemoveField(
            model_name='febe_parameters',
            name='SB1_POL2',
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='all_sb_pol1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='all_sb_pol2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb2_pol1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb2_pol2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb3_pol1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb3_pol2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb4_pol1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb4_pol2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb5_pol1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb5_pol2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb6_pol1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb6_pol2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb7_pol1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb7_pol2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb8_pol1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb8_pol2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb1_pol1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='sb1_pol2',
            field=models.BooleanField(default=False),
        ),
    ]