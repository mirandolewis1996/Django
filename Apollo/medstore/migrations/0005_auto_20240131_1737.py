# Generated by Django 2.2.28 on 2024-01-31 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medstore', '0004_auto_20240131_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='status',
            new_name='medic_choice',
        ),
    ]
