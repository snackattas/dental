# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 00:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('address', models.TextField()),
                ('public_email', models.EmailField(max_length=254)),
                ('accept_appointment_types', multiselectfield.db.fields.MultiSelectField(choices=[('Bonding', 'Bonding'), ('Braces', 'Braces'), ('Bridges', 'Bridges'), ('Implants', 'Implants'), ('Crowns', 'Crowns'), ('Caps', 'Caps'), ('Dentures', 'Dentures'), ('Extractions', 'Extractions'), ('Gum Surgery', 'Gum Surgery'), ('Oral Cancer Examination', 'Oral Cancer Examination'), ('Root Canal', 'Root Canal'), ('Teeth Whitening', 'Teeth Whitening'), ('Veneers', 'Veneers')], max_length=135)),
                ('accept_dental_plans', models.TextField()),
                ('accept_uninsured', models.BooleanField()),
                ('accept_walkins', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='agent',
            name='facility',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='agents.Facility'),
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
