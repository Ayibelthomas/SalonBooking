# Generated by Django 5.0.1 on 2024-03-29 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpr', '0024_rename_cpname_onlineauctionbidtable_cname'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlineauctionbidtable',
            name='pname',
            field=models.CharField(default='hospital full management contract', max_length=30),
        ),
    ]
