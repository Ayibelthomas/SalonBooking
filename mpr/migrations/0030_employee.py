# Generated by Django 5.0.1 on 2024-04-12 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpr', '0029_user_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username1', models.CharField(max_length=20)),
                ('Email1', models.EmailField(max_length=254)),
                ('Phonenumber1', models.IntegerField()),
                ('Password1', models.CharField(max_length=20)),
                ('Image1', models.ImageField(null=True, upload_to='Image')),
                ('Address1', models.CharField(max_length=200)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mpr.login')),
            ],
        ),
    ]
