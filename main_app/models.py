from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=25)
    motto = models.CharField(max_length=50)
    capital = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    game_mode = models.CharField(max_length=25)
    correct = models.IntegerField()
    incorrect = models.IntegerField()
    total_points = models.IntegerField()

    def __str__(self):
        return self.user

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_mode = models.CharField(max_length=25)
    current_state = models.IntegerField()
    incorrect = models.IntegerField()

    def __str__(self):
        return self.user