# Generated by Django 4.0.4 on 2022-06-01 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_managers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_manager',
            name='league',
            field=models.CharField(max_length=30),
        ),
    ]
