from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
  creator = models.IntegerField("Заявитель", default=0)
  trip_from = models.CharField("Место отправления:",max_length=30)
  trip_to = models.CharField("Место прибытия:",max_length=30)
  datetime = models.DateTimeField("Время отбытия")
  free_seats = models.PositiveIntegerField("Свободные места:")
  car = models.CharField("Машина:",max_length=30)
  users = models.ManyToManyField(User,blank=True)
  phone = models.CharField("Номер телефона",default="+7",max_length=16, blank=True)

  def __str__(self):
    return "%s - %s" % (self.trip_from, self.trip_to,)
