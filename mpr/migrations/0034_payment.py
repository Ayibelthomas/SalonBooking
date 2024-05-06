# Generated by Django 5.0.1 on 2024-04-12 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpr', '0033_alter_request_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=20)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mpr.employee')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mpr.user')),
            ],
        ),
    ]