from django.http import HttpResponse
from datetime import datetime


def hello(request):
    if "name" in request.GET:
        uname = request.GET["name"]
    else:
        uname = "Unknown"

    return HttpResponse(f"<h1>Welcome to {uname}</h1>")


def wish(request):
    hours = datetime.now().hour
    if hours < 12:
        msg = "Good Morning"
    elif hours < 17:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"

    return HttpResponse(f"<h1>{msg}</h1>")
