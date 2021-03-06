# Generated by Django 4.0.4 on 2022-06-01 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
                ('assists', models.IntegerField()),
                ('plus_minus', models.IntegerField()),
                ('power_play_points', models.IntegerField()),
                ('shots', models.IntegerField()),
                ('penalty_minutes', models.IntegerField()),
                ('goals', models.IntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
    ]
