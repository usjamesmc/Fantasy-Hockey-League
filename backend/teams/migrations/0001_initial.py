# Generated by Django 4.0.4 on 2022-06-01 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leagues', '0001_initial'),
        ('team_managers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ranking', models.IntegerField()),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.league')),
                ('team_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team_managers.team_manager')),
            ],
        ),
    ]
