from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Bets(models.Model):
    amount = models.IntegerField(default=0)
    match_id = models.IntegerField()
    home_points = models.IntegerField()
    away_points = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
    	return f"{self.author} bets on {self.home_points}-{self.away_points} with {self.amount}"