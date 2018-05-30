from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RawTripForm
from .models import Trip

def index(request):

  return render(request,'blabla/index.html')

def home(request):
  trips = Trip.objects.all()
  return render(request, 'blabla/home.html',{'trips':trips})

def detail(request,trip_id):
  trip = Trip.objects.get(pk=trip_id)
  return render(request, 'blabla/detail.html',{'trip':trip})

def create_trip(request):
  if request.method == 'GET':
    trip_form = RawTripForm()
    return render(request, 'blabla/create_trip.html', {'trip_form':trip_form})
  else:
    trip_form = TripForm(request)


def login(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
  return redirect('')



