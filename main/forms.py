from django import forms
from django.forms import widgets
from main import models

class RegisterVehicleForm(forms.ModelForm):
    
    class Meta:
        model = models.RegisterVehicle
        fields = "__all__"
        
class BookVehicleForm(forms.ModelForm):
    
    class Meta:
        widgets = {'datetime': widgets.DateTimeInput()}
        model = models.BookVehicle
        fields = "__all__"

class TripForm(forms.ModelForm):
    
    class Meta:
        # widgets = {'datetime': widgets.DateTimeInput()}
        model = models.Trip
        fields = "__all__"

