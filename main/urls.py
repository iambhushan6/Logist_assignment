from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.Homehtml.as_view()),

    path('adminpanel/', views.Page2html.as_view()),

    path('registration/', views.Page4html.as_view()),
    
    path('booktruck/', views.BookTruckView.as_view()),

    path('registervehicle/', views.RegisterVehicleView.as_view()),

    # path('trip/', views.Centerlist.as_view()),

    path('customers/', views.CustomersListView.as_view()),

    path('vehicleowners/', views.VehicleOwnersListView.as_view()),

]