from django import forms
from django.forms.models import modelform_factory,modelformset_factory
from .models import Trip
from django.contrib.admin import widgets



#class DateTimeInput(forms.DateTimeInput):
#  input_type = 'datetime'

#class TripForm(forms.ModelForm):
#  class Meta:
#    model = Trip
#    fields = ['trip_from', 'trip_to', 'datetime', 'free_seats', 'car']
#    widgets = {'datetime': forms.DateTimeInput(attrs={'id':'datetimepicker12'})}

TripForm = modelform_factory(Trip, exclude=('creator','users'),
                             widgets = {'datetime': forms.DateTimeInput(attrs={'id':'datetimepicker12',
                                                                              'data-target':'#datetimepicker12',
                                                                               #'data-target-input':'nearest',
                                                                               'data-toggle':'datetimepicker'
                                                                              })})
DetailForm = modelform_factory(Trip, exclude=('creator','users'),
                             widgets = {'datetime':  forms.DateTimeInput(attrs={'type':'button'}),
                                        'free_seats': forms.DateTimeInput(attrs={'type':'button'}),
                                        'trip_from': forms.DateTimeInput(attrs={'type':'button'}),
                                        'trip_to': forms.DateTimeInput(attrs={'type':'button'}),
                                        'car': forms.DateTimeInput(attrs={'type':'button'}),
                                        'phone': forms.DateTimeInput(attrs={'type':'button'}),
                                       })
