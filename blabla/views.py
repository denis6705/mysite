from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import  TripForm, DetailForm
from .models import Trip
def index(request):

  return render(request,'blabla/index.html')

def home(request):
  trips = Trip.objects.all().order_by('datetime')
  return render(request, 'blabla/home.html',{'trips':trips})

def detail(request,trip_id):
  trip = Trip.objects.get(pk=trip_id)
  if trip.creator == request.user.id:
    return redirect('edit_trip', trip_id)
  trip_form = DetailForm(instance=trip)
  return render(request, 'blabla/detail.html',{'trip_form':trip_form,
                                               'trip_id':trip_id,
                                               'trip_creator':trip.creator})

def my_trips(request, trip_id):
  trips = Trip.objects.all(creator=request.user.id)
  pass

def my_subscriptions(request):
  pass

def delete_trip(request, trip_id):
  t = Trip.objects.get(pk=trip_id)
  if t.creator == request.user.id:
    t.delete()
  return redirect('home')

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
    return redirect('home')

def edit_trip(request, trip_id):
  if request.method == 'GET':
    trip = Trip.objects.get(pk=trip_id)
    trip_form = TripForm(instance=trip)
    return render(request, 'blabla/edit.html', {'trip_form':trip_form, 'trip_id':trip_id})
  elif request.method == 'POST':
    new_trip_form = TripForm(request.POST)
    if new_trip_form.is_valid():
      model = new_trip_form.instance
      model.pk = trip_id
      model.creator = request.user.id
      model.save()
    return redirect('home')





