# Generated by Django 4.2.3 on 2023-07-24 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session_manager_app', '0014_remove_febe_parameters_sb1'),
    ]

    operations = [
        migrations.AddField(
            model_name='febe_parameters',
            name='SB1',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='session_manager_app.sb_pol'),
            preserve_default=False,
        ),
    ]
