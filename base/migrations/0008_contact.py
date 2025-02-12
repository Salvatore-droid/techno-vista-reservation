# Generated by Django 5.1.6 on 2025-02-12 19:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_reserve_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField(null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
