from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car/<int:pk>/', views.car_detail, name='car-detail'),
    path('my-listings/', views.my_listings, name='my-listings'),
    path('add-car/', views.add_car, name='add-car'),
    path('edit-car/<int:pk>/', views.edit_car, name='edit-car'),
    path('delete-car/<int:pk>/', views.delete_car, name='delete-car'),
]