# Generated by Django 3.1.4 on 2020-12-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField()),
                ('city', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('team1', models.CharField(max_length=300)),
                ('team2', models.CharField(max_length=300)),
                ('toss_winner', models.CharField(max_length=300)),
                ('toss_decision', models.CharField(max_length=300)),
                ('result', models.CharField(max_length=300)),
                ('dl_applied', models.BooleanField(default=False)),
                ('winner', models.CharField(max_length=300)),
                ('win_by_runs', models.IntegerField()),
                ('win_by_wickets', models.IntegerField()),
                ('player_of_match', models.CharField(max_length=300)),
                ('venue', models.CharField(max_length=500)),
                ('umpire1', models.CharField(max_length=300)),
                ('umpire2', models.CharField(max_length=300)),
            ],
        ),
    ]
