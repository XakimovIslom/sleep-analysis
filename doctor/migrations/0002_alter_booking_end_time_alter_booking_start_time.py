# Generated by Django 5.0.3 on 2024-03-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateField(),
        ),
    ]
