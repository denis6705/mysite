from django.forms import Form, ModelForm
from .models import Trip

class TripForm(ModelForm):
  class Meta:
    model = Trip
    fields = ['trip_from', 'trip_to', 'datetime', 'free_seats', 'car']

