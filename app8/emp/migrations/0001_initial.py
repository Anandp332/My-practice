# Generated by Django 3.2.6 on 2021-09-12 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('email', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=40)),
                ('fullname', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('salary', models.FloatField(max_length=40)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]
