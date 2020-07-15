from django.db import models

# Create your models here.


class Bets(models.Model):
    owner = models.CharField(max_length=30, null=True)
    amount = models.IntegerField()
    match_id = models.IntegerField()
    home_points = models.IntegerField()
    away_points = models.IntegerField()


class User(models.Model):
    bets = models.ForeignKey(
        Bets, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=30, primary_key=True)
    email = models.CharField(max_length=30, unique=True)
    points = models.IntegerField(default=0)
