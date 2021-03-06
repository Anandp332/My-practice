# Generated by Django 3.2.6 on 2021-09-22 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=10)),
                ('owner_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Car',
                'db_table': 'car',
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mod1.car')),
                ('FuelType', models.CharField(max_length=100)),
                ('Engine_year', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Engine',
                'db_table': 'engine',
            },
        ),
    ]
