from django.shortcuts import render
from django.http import HttpResponse
from .models import CompanyInfo


# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')


def about(request):
    return render(request, 'about.html', {'info': CompanyInfo()})
