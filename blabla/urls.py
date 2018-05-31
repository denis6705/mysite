from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('detail/<int:trip_id>',views.detail, name='detail'),
  path('edit/<int:trip_id>', views.edit_trip, name='edit_trip'),
  path('create/', views.create_trip, name='create_trip'),
]
