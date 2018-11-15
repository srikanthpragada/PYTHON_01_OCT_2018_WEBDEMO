from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddJobForm
import sqlite3


def insert_job(id, title, minsal):
    con = sqlite3.connect(r"e:\classroom\python\oct1\hr.db")
    cur = con.cursor()
    try:
        cur.execute("insert into jobs values(?,?,?)", (id, title, minsal))
        con.commit()
        message = "Job has been added successfully!"
    except:
        message = "Sorry! Could not add job. Please try again!"
    finally:
        con.close()

    return message


def get_job(id):
    con = sqlite3.connect(r"e:\classroom\python\oct1\hr.db")
    cur = con.cursor()
    try:
        cur.execute("select * from jobs where job_id = ?",(id,))
        job = cur.fetchone()
        return job
    except:
        return None
    finally:
        con.close()



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
    jobid = ""
    jobtitle = ""
    minsal = ""
    if request.method == 'POST':
        jobid = request.POST["jobid"]
        jobtitle = request.POST["jobtitle"]
        minsal = request.POST["minsal"]
        message = insert_job(jobid, jobtitle, minsal)

    # Common for GET and POST
    return render(request, 'jobs/add.html',
                  {'message': message,
                   'jobid': jobid,
                   'jobtitle': jobtitle,
                   'minsal': minsal})


def search_jobs(request):
    pass


def delete_job(request, jobid):
    print("Job id ", jobid)
    return render(request, 'jobs/delete.html',
                  {'message': f"Job [{jobid}] has been deleted!"})
    # delete job with given jobid from JOBS table
    # return redirect('/hr/jobs/list')


def add_job_form(request):
    message = ""
    if request.method == "GET":
        f = AddJobForm()
    else:
        f = AddJobForm(request.POST)  # Bind data from request to form
        if f.is_valid():
            jobid = f.cleaned_data["jobid"]
            jobtitle = f.cleaned_data["jobtitle"]
            minsal = f.cleaned_data["minsal"]
            message = insert_job(jobid,jobtitle,minsal)
            f = AddJobForm()

    # Common for GET and POST
    return render(request, 'jobs/add.html',
                  {'message': message,
                   'form': f})


def edit_job(request,jobid):
     message = ""
     if request.method == "GET":
        job = get_job(jobid)
        if not job is None:
            f = AddJobForm({'jobid' : job[0],  'jobtitle' : job[1],
                             'minsal' : job[2]})
        else:
            return render(request, "jobs/error.html",
                            {'message' : 'Job Id Not Found!'})
     else:
         # post
         # Create form and bind data from request.POST
         # Validate and update JOBS table and set message
         pass

     # Common for GET and POST
     return render(request, 'jobs/edit.html',
                      {'message': message,
                       'form': f})