# Generated by Django 4.1.7 on 2023-03-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_agelimit_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comics',
            name='weight',
            field=models.FloatField(),
        ),
    ]