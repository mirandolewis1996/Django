# Generated by Django 2.2.28 on 2024-01-31 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medstore', '0002_auto_20240130_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='medic_choice',
            new_name='medichoice',
        ),
    ]
