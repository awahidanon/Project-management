# Generated by Django 5.0.1 on 2024-01-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pims', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catagory',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='endDate',
            field=models.DateTimeField(verbose_name=' End Date'),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='startDate',
            field=models.DateTimeField(verbose_name='Start Date'),
        ),
    ]
