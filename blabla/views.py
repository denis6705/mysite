from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RawTripForm, TripForm
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
    trip_form = TripForm()
    return render(request, 'blabla/create_trip.html', {'trip_form':trip_form})
  elif request.method == 'POST':
    trip_form = TripForm(request.POST)
    if trip_form.is_valid():
      model = trip_form.instance
      model.creator = request.user.id
      model.save()
    return render(request, 'blabla/create_trip.html', {'trip_form':TripForm()})

def edit_trip(request, trip_id):
  if request.method == 'GET':
    trip = Trip.objects.get(pk=trip_id)
    trip_form = TripForm(instance=trip)
    return render(request, 'blabla/edit.html', {'trip_form':trip_form})
  elif requst.method == 'POST':
    model

def login(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
  return redirect('')



