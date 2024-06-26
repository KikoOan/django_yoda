# Generated by Django 4.2.3 on 2023-07-24 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session_manager_app', '0012_alter_febe_parameters_sb_pol_1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sb_pol',
            old_name='pol',
            new_name='pol_1',
        ),
        migrations.RemoveField(
            model_name='febe_parameters',
            name='sb_pol_1',
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='SB1',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='session_manager_app.sb_pol'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sb_pol',
            name='pol_2',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
