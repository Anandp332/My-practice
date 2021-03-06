# Generated by Django 3.2.6 on 2021-09-19 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flatno', models.CharField(max_length=10)),
                ('appartment_name', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Address',
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'not specified')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empdata.address')),
            ],
            options={
                'verbose_name_plural': 'Employee',
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='ContractEmployee',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='empdata.employee')),
                ('payperhour', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'ContractEmployee',
                'db_table': 'contractemployee',
            },
            bases=('empdata.employee',),
        ),
        migrations.CreateModel(
            name='RegularEmployee',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='empdata.employee')),
                ('salary', models.IntegerField()),
                ('bonus', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'RegularEmployee',
                'db_table': 'regularemployee',
            },
            bases=('empdata.employee',),
        ),
    ]
