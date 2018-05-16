

from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=200)

    def __str__(self):
        return self.team_name


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_forename = models.CharField(max_length=20, null=True, blank=True)
    player_surname = models.CharField(max_length=20, null=True, blank=True)
    squad_number = models.IntegerField(default=0)

    def __str__(self):
        return self.player_surname