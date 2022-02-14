from django.shortcuts import render
from .models import * 

# Create your views here.


def home(request):
    return render(request, 'transfer/index.html')


def customers(request):
    customers = Customer.objects.all()
    return render(request, 'transfer/customers.html', {'customers':customers})
