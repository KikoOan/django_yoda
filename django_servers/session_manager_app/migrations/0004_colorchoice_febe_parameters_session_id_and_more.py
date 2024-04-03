# Generated by Django 4.2.3 on 2023-07-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_manager_app', '0003_febe_parameters_sb_oscillator_sb_pol'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('red', 'Red'), ('green', 'Green'), ('blue', 'Blue')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='febe_parameters',
            name='session_id',
            field=models.CharField(default=2, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='febe_parameters',
            name='febe_id',
            field=models.CharField(choices=[('febe1', 'Febe1'), ('febe2', 'Febe2'), ('febe3', 'Febe3'), ('febe4', 'Febe4')], max_length=10),
        ),
    ]