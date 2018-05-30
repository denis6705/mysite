from django import forms
from .models import Trip
from django.contrib.admin import widgets
from  bootstrap3_datetime.widgets import DateTimePicker
class TripForm(forms.ModelForm):

  class Meta:
    model = Trip
    fields = ['trip_from', 'trip_to', 'datetime', 'free_seats', 'car']



class RawTripForm(forms.Form):
  trip_from = forms.CharField()
  trip_to = forms.CharField()
  car = forms.CharField()
  datetime = forms.DateTimeField()
  free_seats = forms.IntegerField()
