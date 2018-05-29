from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
  trip_from = models.CharField("Место отправления:",max_length=30)
  trip_to = models.CharField("Место прибытия:",max_length=30)
  datetime = models.DateTimeField()
  free_seats = models.IntegerField()
  car = models.CharField("Машина:",max_length=30)
  users = models.ManyToManyField(User)

  def __str__(self):
    return "%s - %s" % (self.trip_from, self.trip_to)

