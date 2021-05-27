from django.shortcuts import render
from django.views import View
from main import models
from django.views.generic import(
    TemplateView,
    DetailView,
    View,
    CreateView,
    FormView,
    ListView,
)

# Create your views here.

class Homehtml(View):
        def get(self,request):
            return render(request,'main/home.html')
            
class Page2html(View):
        def get(self,request):
            return render(request,'main/page2.html')

class Page4html(View):
        def get(self,request):
            return render(request,'main/page4.html')

class BookTruckView(CreateView):
    model = models.BookVehicle
    template_name = 'main/booktruck.html'
    fields = '__all__'
    success_url ='/'

class RegisterVehicleView(CreateView):
    model = models.RegisterVehicle
    template_name = 'main/registervehicle.html'
    fields = '__all__'
    success_url ='/'
