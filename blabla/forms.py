from django import forms
from .models import Trip
from django.contrib.admin import widgets
from  bootstrap3_datetime.widgets import DateTimePicker


class DateTimeInput(forms.DateTimeInput):
  input_type = 'datetime'

class TripForm(forms.ModelForm):
  class Meta:
    model = Trip
    fields = ['trip_from', 'trip_to', 'datetime', 'free_seats', 'car']
    widgets = {'datetime': DateTimeInput(attrs={'id':'datetimepicker12'})}


class RawTripForm(forms.Form):
  trip_from = forms.CharField()
  trip_to = forms.CharField()
  car = forms.CharField()
  datetime = forms.DateTimeField(
    required=False,
    widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}))
  free_seats = forms.IntegerField()
