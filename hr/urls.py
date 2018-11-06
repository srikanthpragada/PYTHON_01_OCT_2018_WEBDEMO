from django.contrib import admin
from django.urls import path, include
from . import views, job_views


urlpatterns = [
    path('welcome/', views.welcome),
    path('about/', views.about),
    path('jobs/list', job_views.list),
]
