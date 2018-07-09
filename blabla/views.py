from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import  TripForm, DetailForm
from .models import Trip
from django.contrib.auth.models import User
from datetime import datetime as dt
def index(request):

  return render(request,'blabla/index.html')
@login_required
def home(request):
  trips = Trip.objects.all().order_by('datetime').filter(datetime__gte=dt.now())
  return render(request, 'blabla/home.html',{'trips':trips})
#-------------detail---------------------------------------------------------------
@login_required
def detail(request,trip_id):
  trip = Trip.objects.get(pk=trip_id)
  if trip.creator == request.user.id:
    return redirect('edit_trip', trip_id)
  trip_form = DetailForm(instance=trip)
  subscribed = (request.user in list(trip.users.all()))
  if not subscribed and trip.free_seats > 0:
      can_subscribe = True
  else:
      can_subscribe = False
  #creator_name = User.objects.get(pk=trip.creator).first_name + ", Номер телефона:"
  creator_name = User.objects.get(pk=trip.creator).first_name
  if not creator_name:
      creator_name = User.objects.get(pk=trip.creator).username
  creator_name += ", Номер телефона:"
  return render(request, 'blabla/detail.html',{'trip_form':trip_form,
                                               'trip_id':trip_id,
                                               'creator_name': creator_name,
                                               'can_subscribe': can_subscribe,
                                               'subscribed': subscribed
                                               })
#----------------------------------------------------------------------------------
@login_required
def my_trips(request):
  trips = Trip.objects.all().filter(creator=request.user.id)
  return render(request, 'blabla/my_trips.html',{'trips':trips})
  
@login_required
def my_subscriptions(request):
  trips = request.user.trip_set.all()
  return render(request, 'blabla/my_subscriptions.html',{'trips':trips})

def delete_trip(request, trip_id):
  t = Trip.objects.get(pk=trip_id)
  if t.creator == request.user.id:
    t.delete()
  return redirect('home')
@login_required
def subscribe(request, trip_id):
    trip = Trip.objects.get(pk=trip_id)
    trip.users.add(request.user)
    trip.free_seats -= 1
    trip.save()
    return redirect('detail',trip_id)
@login_required
def unsubscribe(request, trip_id):
    trip = Trip.objects.get(pk=trip_id)
    trip.users.remove(request.user)
    trip.free_seats += 1
    trip.save()
    return redirect('detail', trip_id)

@login_required
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
@login_required
def edit_trip(request, trip_id):
  if request.method == 'GET':
    trip = Trip.objects.get(pk=trip_id)
    trip_form = TripForm(instance=trip)
    users = trip.users.all()
    return render(request, 'blabla/edit.html', {'trip_form':trip_form, 'trip_id':trip_id, 'users':users})
  elif request.method == 'POST':
    new_trip_form = TripForm(request.POST)
    if new_trip_form.is_valid():
      model = new_trip_form.instance
      model.pk = trip_id
      model.creator = request.user.id
      model.save()
    return redirect('home')
