from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('detail/<int:trip_id>',views.detail, name='detail'),
  path('edit/<int:trip_id>', views.edit_trip, name='edit_trip'),
  path('create/', views.create_trip, name='create_trip'),
  path('delete/<int:trip_id>', views.delete_trip, name='delete_trip'),
  path('subscribe/<int:trip_id>', views.subscribe, name='subscribe'),
  path('unsubscribe/<int:trip_id>', views.unsubscribe, name='unsubscribe'),
  path('my_subscriptions/', views.my_subscriptions, name='my_subscriptions'),
  path('my_trips/', views.my_trips, name='my_trips'),

]
