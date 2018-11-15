from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookForm, AddJobForm
from .models import Book
import sqlite3


def get_job(id):
    con = sqlite3.connect(r"e:\classroom\python\oct1\hr.db")
    cur = con.cursor()
    try:
        cur.execute("select * from jobs where job_id = ?", (id,))
        job = cur.fetchone()
        return job
    except:
        return None
    finally:
        con.close()


def list_books(request):
    return render(request, 'books/list.html',
                  {'books': Book.objects.all()})


def search_jobs(request):
    pass


def delete_book(request, bookid):
    message = ""
    try:
        book = Book.objects.get(id=bookid)
        book.delete()
        message = f"[{book.title}] has been deleted successfully!"
    except:
        message = f"Sorry! Book with id [{bookid}] could not be deleted!"

    return render(request, 'books/delete.html', {'message': message})


def add_book(request):
    message = ""
    if request.method == "GET":
        f = BookForm()
    else:
        f = BookForm(request.POST)  # Bind data from request to form
        if f.is_valid():
            f.save()  # insert using ORM
            f = BookForm()
            message = "Book has been added successfully!"

    # Common for GET and POST
    return render(request, 'books/add.html',
                  {'message': message,
                   'form': f})


def edit_book(request, bookid):
    message = ""
    if request.method == "GET":
        try:
            book = Book.objects.get(id=bookid)
            f = BookForm(instance=book)
        except:
            return render(request, "books/error.html",
                          {'message': f'Book Id [{bookid}] Not Found!'})
    else:
        # post
        book = Book.objects.get(id=bookid)
        f = BookForm(instance=book, data=request.POST)
        try:
            f.save()
            message = "Book has been updated successfully!"
        except:
            message = "Sorry! Could not update book!"

    # Common for GET and POST
    return render(request, 'books/edit.html',
                  {'message': message,
                   'form': f})
