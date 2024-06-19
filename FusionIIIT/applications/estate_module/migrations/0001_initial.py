# Generated by Django 3.1.5 on 2024-06-19 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dateIssued', models.DateField()),
                ('dateConstructionStarted', models.DateField(blank=True, null=True)),
                ('dateConstructionCompleted', models.DateField(blank=True, null=True)),
                ('dateOperational', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('OS', 'On Schedule'), ('DL', 'Delayed')], default='OS', max_length=2)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('constructionCostEstimated', models.IntegerField(blank=True, null=True)),
                ('constructionCostActual', models.IntegerField(blank=True, null=True)),
                ('numRooms', models.IntegerField(blank=True, null=True)),
                ('numWashrooms', models.IntegerField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='InventoryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rate', models.IntegerField()),
                ('manufacturer', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('workType', models.CharField(choices=[('CW', 'Construction'), ('MW', 'Maintenance')], default='MW', max_length=2)),
                ('contractorName', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('OS', 'On Schedule'), ('DL', 'Delayed')], default='OS', max_length=2)),
                ('dateIssued', models.DateField()),
                ('dateStarted', models.DateField(blank=True, null=True)),
                ('dateCompleted', models.DateField(blank=True, null=True)),
                ('costEstimated', models.IntegerField(blank=True, null=True)),
                ('costActual', models.IntegerField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estate_module.building')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SubWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dateIssued', models.DateField()),
                ('dateStarted', models.DateField(blank=True, null=True)),
                ('dateCompleted', models.DateField(blank=True, null=True)),
                ('costEstimated', models.IntegerField(blank=True, null=True)),
                ('costActual', models.IntegerField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate_module.work')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='InventoryNonConsumable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('dateOrdered', models.DateField()),
                ('dateReceived', models.DateField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('serial_no', models.CharField(max_length=20)),
                ('dateLastVerified', models.DateField()),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estate_module.building')),
                ('inventoryType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate_module.inventorytype')),
                ('issued_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estate_module.work')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryConsumable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('dateOrdered', models.DateField()),
                ('dateReceived', models.DateField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('presentQuantity', models.IntegerField()),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estate_module.building')),
                ('inventoryType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate_module.inventorytype')),
                ('work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estate_module.work')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
    ]
