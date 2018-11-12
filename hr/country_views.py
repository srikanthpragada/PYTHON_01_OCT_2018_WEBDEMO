from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime


def select_country(request):
    return render(request, 'select_country.html')


def save_country(request):
    # save country code as cookie
    code = request.POST["code"]
    # create cookie
    response = redirect("/hr/showcountryinfo")
    response.set_cookie("country", code, secure=False,
                        expires=datetime.datetime.now() +
                                datetime.timedelta(days=30))
    return response


def show_country_info(request):
    if 'country' in request.COOKIES:
        country_code = request.COOKIES["country"]
        # Get information about country with given code
        return render(request, 'show_country_info.html',
                      {'code': country_code})
    else:
        return redirect("/hr/selectcountry")
