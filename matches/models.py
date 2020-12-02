from django.db import models

# Create your models here.

class Match(models.Model):
    season = models.IntegerField()
    city = models.CharField(max_length=300)
    date = models.DateField()
    team1 = models.CharField(max_length=300)
    team2 = models.CharField(max_length=300)
    toss_winner = models.CharField(max_length=300)
    toss_decision = models.CharField(max_length=300)
    result = models.CharField(max_length=300)
    dl_applied = models.BooleanField(default=False)
    winner = models.CharField(max_length=300)
    win_by_runs = models.IntegerField()
    win_by_wickets = models.IntegerField()
    player_of_match = models.CharField(max_length=300)
    venue = models.CharField(max_length=500)
    umpire1 = models.CharField(max_length=300)
    umpire2 = models.CharField(max_length=300)


    def __str__(self):
        return "{0} vs {1}".format(self.team1, self.team2)