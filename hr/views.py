from django.shortcuts import render
from django.http import HttpResponse
from .models import CompanyInfo


# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')


def about(request):
    return render(request, 'about.html', {'info': CompanyInfo()})


def languages(request):
    if 'langs' in request.session:
        langs = request.session['langs']
    else:
        langs = list()  # empty set

    if 'lang' in request.GET:
        lang = request.GET['lang']
        # add lang to langs collection in session
        langs.append(lang)
        request.session["langs"] = langs

    return render(request,"languages.html", {"langs" : langs})