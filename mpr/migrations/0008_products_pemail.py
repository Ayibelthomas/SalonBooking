# Generated by Django 5.0.1 on 2024-03-05 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpr', '0007_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pemail',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
