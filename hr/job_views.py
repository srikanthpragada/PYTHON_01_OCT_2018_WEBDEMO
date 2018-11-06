from django.shortcuts import render
from django.http import HttpResponse
import sqlite3


def list(request):
    # connect to db and retrieve details
    con = sqlite3.connect(r"e:\classroom\python\oct1\hr.db")
    cur = con.cursor()
    cur.execute("select * from jobs order by job_id")
    jobs = cur.fetchall()
    con.close()
    return render(request, 'jobs/list.html', {'jobs': jobs})


def add(request):
    pass


def search(request):
    pass
