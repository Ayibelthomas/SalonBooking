# Generated by Django 5.0.1 on 2024-04-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpr', '0032_alter_request_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='Datetime',
            field=models.DateField(null=True),
        ),
    ]