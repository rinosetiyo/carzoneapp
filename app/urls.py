from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('services/', views.services, name="services"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('cars/', views.cars, name="cars"),
    path('cars/<int:id>', views.car_detail, name="car_detail"),
    path('search/', views.search, name="search"),
    path('inquiry/', views.inquiry, name="inquiry"),
    path('contact/', views.contact, name="contact"),
]