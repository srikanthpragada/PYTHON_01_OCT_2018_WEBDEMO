from django.contrib import admin
from django.urls import path, include
from . import views, job_views, country_views, book_views, class_views


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
    path('languages', views.languages),
    path('books/list', book_views.list_books),
    path('books/add', book_views.add_book),
    path('books/delete/<bookid>/', book_views.delete_book),
    path('books/edit/<bookid>', book_views.edit_book),
    path('books/search_books', book_views.search_books),
    path('books/search', book_views.search_books_form),
    path('ajax_demo', views.ajax_demo),
    path('time', views.ajax_time),
    path('hello/', class_views.HelloView.as_view()),
    path('hello2/', class_views.HelloView2.as_view()),
    path('listbooks/', class_views.ListBooks.as_view()),

 ]
