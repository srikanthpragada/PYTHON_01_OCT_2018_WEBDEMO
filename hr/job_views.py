from django.shortcuts import render
from django.http import HttpResponse
import sqlite3


def list_jobs(request):
    # connect to db and retrieve details
    con = sqlite3.connect(r"e:\classroom\python\oct1\hr.db")
    cur = con.cursor()
    cur.execute("select * from jobs order by job_id")
    jobs = cur.fetchall()
    con.close()
    return render(request, 'jobs/list.html', {'jobs': jobs})


def add_job(request):
    message = ""
    jobid =""
    jobtitle = ""
    minsal = ""
    if request.method == 'POST':
        jobid = request.POST["jobid"]
        jobtitle = request.POST["jobtitle"]
        minsal = request.POST["minsal"]
        con = sqlite3.connect(r"e:\classroom\python\oct1\hr.db")
        cur = con.cursor()
        try:
            cur.execute("insert into jobs values(?,?,?)", (jobid, jobtitle, minsal))
            con.commit()
            message = "Job has been added successfully!"
        except:
            message = "Sorry! Could not add job. Please try again!"
        finally:
            con.close()

    # Common for GET and POST
    return render(request, 'jobs/add.html',
                  {'message': message,
                   'jobid' : jobid,
                   'jobtitle' : jobtitle,
                   'minsal' : minsal })


def search_jobs(request):
    pass

def delete_job(request):
    pass
