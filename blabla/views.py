from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import TripForm
from .models import Trip

def index(request):

  return render(request,'blabla/index.html')

def home(request):
  #trips = Trip.objects.all()
  trip = Trip.objects.get(pk=1)
  trip_form = TripForm(instance=trip)
  return render(request, 'blabla/home.html',{'form':trip_form})

def login(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
  return redirect('')



