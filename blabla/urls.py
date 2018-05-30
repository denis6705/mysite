from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('detail/<int:trip_id>',views.detail, name='detail'),
  path('create/', views.create_trip, name='create_trip'),
]
