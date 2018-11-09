from django import forms
# import django.forms as forms


class AddJobForm(forms.Form):
    jobid = forms.CharField(label="Job ID", max_length=10)
    jobtitle = forms.CharField(max_length=20, label="Job Title")
    minsal = forms.IntegerField(label="Minimum Salary")
