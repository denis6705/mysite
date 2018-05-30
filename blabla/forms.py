from django.forms import ModelForm
from .models import Trip
from django.contrib.admin import widgets

class TripForm(ModelForm):

  class Meta:
    model = Trip
    fields = ['trip_from', 'trip_to', 'datetime', 'free_seats', 'car']
  def __init__(self, *args, **kwargs):
    super(TripForm, self).__init__(*args, **kwargs)
    self.fields['datetime'].widget = widgets.AdminSplitDateTime()
