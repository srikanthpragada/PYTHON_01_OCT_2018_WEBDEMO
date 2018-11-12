from django.contrib import admin
from django.urls import path, include
from . import views, job_views, country_views

urlpatterns = [
    path('welcome/', views.welcome),
    path('about/', views.about),
    path('jobs/list', job_views.list_jobs),
    path('jobs/add', job_views.add_job),
    path('jobs/edit/<jobid>', job_views.edit_job),
    path('jobs/add_form', job_views.add_job_form),
    path('jobs/delete/<jobid>/', job_views.delete_job),
    path('selectcountry', country_views.select_country),
    path('savecountry', country_views.save_country),
    path('showcountryinfo', country_views.show_country_info),


 ]
