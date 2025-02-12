# Generated by Django 5.0.6 on 2024-06-02 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('street_number', models.CharField(max_length=16)),
                ('city_code', models.CharField(max_length=18)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=32)),
                ('customer_id', models.BigIntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('birthday', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.address')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('last_activity', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('appuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.appuser')),
            ],
        ),
    ]
