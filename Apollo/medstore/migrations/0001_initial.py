# Generated by Django 2.2.28 on 2024-01-30 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(help_text='Enter the disease', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medic_name', models.CharField(help_text='Enter the disease', max_length=100)),
                ('medic_price', models.PositiveIntegerField(help_text='medicine price')),
                ('medic_choice', models.CharField(blank=True, choices=[('tablet', 't'), ('syrup', 's')], default='t', help_text='Select the medicne type', max_length=1)),
                ('disease', models.ManyToManyField(help_text='Select the disease', to='medstore.Disease')),
            ],
        ),
    ]
